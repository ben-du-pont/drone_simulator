import numpy as np
from typing import List, Dict, Tuple, Optional, Union, Any, Set
import logging
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
import csv
from datetime import datetime

# Import refactored components
from online_uwb_initialisation.core.anchor_data import AnchorData, AnchorStatus
from online_uwb_initialisation.core.measurement_processor import MeasurementProcessor, MeasurementProcessorConfig
from online_uwb_initialisation.core.estimation_interface import EstimationFactory, EstimationConfig, EstimationResult
from online_uwb_initialisation.core.metrics_calculator import MetricsCalculator, MetricsResult
from online_uwb_initialisation.core.trajectory_manager import TrajectoryManager, TrajectoryState
from online_uwb_initialisation.core.config_params import UwbInitializationConfig

from online_uwb_initialisation.core.trajectory_optimisation import TrajectoryOptimizer

# Set up logging
logger = logging.getLogger(__name__)


class UwbInitializationPipeline:
    """Pipeline for online UWB anchor initialization.
    
    This class coordinates the collection of range measurements, estimation of anchor 
    positions, and trajectory optimization for UWB anchor initialization.
    """
    
    def __init__(self, config: Optional[UwbInitializationConfig] = None):
        """Initialize the UWB initialization pipeline.
        
        Args:
            config: Configuration parameters for the pipeline
        """
        # Initialize configuration
        self.config = config or UwbInitializationConfig()
        
        # Current drone position
        self.drone_position = np.zeros(3)
        
        # Initialize components
        self._init_components()
        
        # Anchor data storage
        self.anchor_data: Dict[str, AnchorData] = {}
    
    def _init_components(self) -> None:
        """Initialize pipeline components with the current configuration."""
        # Create measurement processor
        measurement_config = MeasurementProcessorConfig(
            distance_to_anchor_ratio_threshold=self.config.measurement.distance_to_anchor_ratio_threshold,
            number_of_redundant_measurements=self.config.measurement.number_of_redundant_measurements,
            distance_rejection_threshold=self.config.measurement.distance_rejection_threshold,
            outlier_z_score_threshold=self.config.outlier.z_score_threshold,
            outlier_count_threshold=self.config.outlier.outlier_count_threshold,
            outlier_removal_method=self.config.least_squares.outlier_removing.name
        )
        self.measurement_processor = MeasurementProcessor(measurement_config)
        
        # Create estimation configuration
        estimation_config = EstimationConfig(
            use_linear_bias=self.config.least_squares.use_linear_bias,
            use_constant_bias=self.config.least_squares.use_constant_bias,
            normalised=self.config.least_squares.normalised,
            regularise=self.config.least_squares.regularise,
            reweighting_iterations=self.config.least_squares.reweighting_iterations,
            weighting_function=self.config.least_squares.weighting_function,
            huber_delta=self.config.least_squares.huber_delta,
            tukey_c=self.config.least_squares.tukey_c,
            welsch_c=self.config.least_squares.welsch_c,
            max_iterations=20,  # Default for nonlinear methods
            tolerance=1e-6       # Default for nonlinear methods
        )
        
        # Create metrics calculator
        self.metrics_calculator = MetricsCalculator()
        
        # Create trajectory optimizer and manager
        self.trajectory_optimizer = TrajectoryOptimizer(
            metric_type=self.config.trajectory.trajectory_optimisation_method.name
        )
        
        self.trajectory_manager = TrajectoryManager(
            trajectory_optimizer=self.trajectory_optimizer,
            optimization_method=self.config.trajectory.trajectory_optimisation_method,
            link_method=self.config.trajectory.link_method
        )
    
    def get_anchor_data(self, anchor_id: str) -> AnchorData:
        """Get data for a specific anchor, creating it if it doesn't exist.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            AnchorData for the specified anchor
        """
        if anchor_id not in self.anchor_data:
            self.anchor_data[anchor_id] = AnchorData(anchor_id=anchor_id)
        return self.anchor_data[anchor_id]
    
    def measurement_callback(self, drone_position: Union[List[float], np.ndarray], 
                           distance: float, anchor_id: str) -> Optional[List[np.ndarray]]:
        """Process a new measurement and update the initialization state.
        
        This method is called whenever a new range measurement is received from an anchor.
        It updates the anchor's data, performs estimation if enough measurements are available,
        and generates optimal trajectories when appropriate.
        
        Args:
            drone_position: Current position of the drone [x, y, z]
            distance: Measured distance to the anchor
            anchor_id: ID of the anchor
            
        Returns:
            Optional list of waypoints if a trajectory was generated, None otherwise
        """
        # Update current drone position
        self.drone_position = np.array(drone_position)
        
        # Get or create anchor data
        anchor_data = self.get_anchor_data(anchor_id)
        
        # Process the measurement based on the anchor's status
        if anchor_data.status == AnchorStatus.UNSEEN:
            # First time seeing this anchor
            if self.process_new_anchor_measurement(anchor_data, drone_position, distance):
                anchor_data.status = AnchorStatus.SEEN
            return None
            
        elif anchor_data.status == AnchorStatus.SEEN:
            # Already seen this anchor, but still collecting measurements
            if not self.process_seen_anchor_measurement(anchor_data, drone_position, distance):
                return None
                
            # Check if we have enough measurements to apply stopping criteria
            if self.check_stopping_criteria(anchor_data):
                # Stopping criteria met, generate trajectory optimization
                return self.handle_stopping_criteria_met(anchor_data)
            
            return None
            
        elif anchor_data.status == AnchorStatus.STOPPING_CRITERION_TRIGGERED:
            # Stopping criteria were previously met, but we couldn't optimize yet
            if self.process_measurement(anchor_data, drone_position, distance):
                if self.trajectory_manager.state == TrajectoryState.ON_OPTIMAL_TRAJECTORY:
                    # Currently optimizing another anchor, just queue this one
                    logger.info(f"Added anchor {anchor_id} to optimization queue")
                    self.trajectory_manager.add_anchor_to_optimization_queue(
                        anchor_id, anchor_data.position
                    )
                    return None
                
                # Check if this anchor is the closest one to optimize
                closest_anchor = self.trajectory_manager.find_closest_anchor_in_queue(self.drone_position)
                if closest_anchor is not None and closest_anchor != anchor_id:
                    logger.info(f"Anchor {anchor_id} not closest, skipping optimization")
                    return None
                
                # Generate optimal trajectory for this anchor
                return self.optimize_trajectory_for_anchor(anchor_data)
            
            return None
            
        elif anchor_data.status == AnchorStatus.OPTIMISED_TRAJECTORY:
            # Currently following an optimized trajectory for this anchor
            if self.process_measurement_optimal_trajectory(anchor_data, drone_position, distance):
                # Check if we've completed the optimal trajectory
                if self.trajectory_manager.check_trajectory_completion(drone_position):
                    # Finalize the anchor initialization
                    self.finalize_anchor_initialization(anchor_data)
                
            return None
            
        elif anchor_data.status == AnchorStatus.INITIALISED:
            # Anchor is already initialized, nothing to do
            return None
            
        else:
            logger.warning(f"Unknown anchor status for anchor {anchor_id}: {anchor_data.status}")
            return None
    
    def process_new_anchor_measurement(self, anchor_data: AnchorData, 
                                     drone_position: Union[List[float], np.ndarray], 
                                     distance: float) -> bool:
        """Process a measurement for a newly detected anchor.
        
        Args:
            anchor_data: Data for the anchor
            drone_position: Current position of the drone [x, y, z]
            distance: Measured distance to the anchor
            
        Returns:
            True if the measurement was accepted, False otherwise
        """
        return self.process_measurement(anchor_data, drone_position, distance)
    
    def process_seen_anchor_measurement(self, anchor_data: AnchorData, 
                                      drone_position: Union[List[float], np.ndarray], 
                                      distance: float) -> bool:
        """Process a measurement for an anchor that has been seen before.
        
        Args:
            anchor_data: Data for the anchor
            drone_position: Current position of the drone [x, y, z]
            distance: Measured distance to the anchor
            
        Returns:
            True if the measurement was accepted and further processing should occur, False otherwise
        """
        if not self.process_measurement(anchor_data, drone_position, distance):
            return False
            
        # If we don't have enough measurements yet, skip further processing
        if anchor_data.num_measurements_pre_estimation <= 15:
            # Add placeholder metrics to keep arrays aligned with measurement count
            anchor_data.append_placeholder_metrics()
            return False
            
        # We have enough measurements, perform estimation
        return self.perform_estimation(anchor_data)
    
    def process_measurement(self, anchor_data: AnchorData, 
                          drone_position: Union[List[float], np.ndarray], 
                          distance: float) -> bool:
        """Process a measurement using the measurement processor.
        
        Args:
            anchor_data: Data for the anchor
            drone_position: Current position of the drone [x, y, z]
            distance: Measured distance to the anchor
            
        Returns:
            True if the measurement was accepted, False otherwise
        """
        return self.measurement_processor.process_measurement(
            anchor_data, tuple(drone_position), distance
        )
    
    def process_measurement_optimal_trajectory(self, anchor_data: AnchorData, 
                                            drone_position: Union[List[float], np.ndarray], 
                                            distance: float) -> bool:
        """Process a measurement during the optimal trajectory phase.
        
        Args:
            anchor_data: Data for the anchor
            drone_position: Current position of the drone [x, y, z]
            distance: Measured distance to the anchor
            
        Returns:
            True if the measurement was accepted, False otherwise
        """
        return self.measurement_processor.process_measurement_optimal_trajectory(
            anchor_data, tuple(drone_position), distance
        )
    
    def perform_estimation(self, anchor_data: AnchorData) -> bool:
        """Perform position estimation for an anchor.
        
        Args:
            anchor_data: Data for the anchor
            
        Returns:
            True if estimation was successful, False otherwise
        """
        # Get all measurements
        measurements = anchor_data.get_all_measurements()
        
        # Create estimator based on rough estimate method
        method = self.config.least_squares.rough_estimate_method
        method_str = method.name.lower()
        
        estimation_config = EstimationConfig(
            use_linear_bias=self.config.least_squares.use_linear_bias,
            use_constant_bias=self.config.least_squares.use_constant_bias,
            normalised=self.config.least_squares.normalised,
            regularise=self.config.least_squares.regularise,
            reweighting_iterations=self.config.least_squares.reweighting_iterations,
            weighting_function=self.config.least_squares.weighting_function
        )
        
        estimator = EstimationFactory.create_estimator(method_str, estimation_config)
        
        # Get initial weights if available
        weights = None
        if len(anchor_data.linear_ls_weights) > 0 and len(anchor_data.linear_ls_weights[-1]) > 0:
            weights = anchor_data.linear_ls_weights[-1]
        
        # Perform estimation
        try:
            result = estimator.estimate(measurements, weights=weights)
            
            # Apply trimmed estimation if enabled
            if self.config.least_squares.use_trimmed_reweighted and method != "simple_linear":
                trim_estimator = EstimationFactory.create_estimator("trimmed_reweighted", estimation_config)
                trimmed_result = trim_estimator.estimate(measurements, initial_guess=result.estimator, weights=weights)
                result = trimmed_result
            
            # Update anchor data with estimation results
            anchor_data.update_estimator(result.estimator, result.covariance_matrix)
            
            # Update weights for next iteration
            if len(result.residuals) > 0:
                new_weights = estimator.update_weights(result.residuals)
                anchor_data.linear_ls_weights.append(new_weights.tolist())
            
            # Handle outlier filtering if enabled
            if self.config.least_squares.outlier_removing != "None" and len(result.residuals) > 0:
                if self.measurement_processor.filter_outliers(anchor_data, result.residuals):
                    # If outliers were removed, skip further processing this round
                    logger.info(f"Outliers removed for anchor {anchor_data.anchor_id}")
                    return False
            
            # Compute and update quality metrics
            self.update_quality_metrics(anchor_data, result)
            
            return True
            
        except Exception as e:
            logger.error(f"Error in estimation for anchor {anchor_data.anchor_id}: {e}")
            # Add placeholder metrics to keep arrays aligned
            anchor_data.append_placeholder_metrics()
            return False
    
    def update_quality_metrics(self, anchor_data: AnchorData, result: EstimationResult) -> None:
        """Update quality metrics for an anchor based on estimation results.
        
        Args:
            anchor_data: Data for the anchor
            result: Estimation results
        """
        # Compute distance between consecutive estimates
        if len(anchor_data.estimator_rough_linear) >= 3:
            prev_position = anchor_data.estimator_rough_linear[:3]
            curr_position = result.estimator[:3]
            distance_delta = np.linalg.norm(curr_position - prev_position)
            anchor_data.consecutive_distances_vector.append(distance_delta)
        else:
            anchor_data.consecutive_distances_vector.append(float('inf'))
        
        # Update other metrics
        gdop = result.gdop if hasattr(result, 'gdop') else self.metrics_calculator.compute_gdop(
            anchor_data.get_all_measurements(), result.position
        )
        
        fim = result.fim if hasattr(result, 'fim') else self.metrics_calculator.compute_fim(
            anchor_data.get_all_measurements(), result.estimator
        )
        
        # Append metrics to anchor data
        anchor_data.GDOP.append(gdop)
        anchor_data.FIM.append(fim)
        anchor_data.residuals.append(np.mean(np.abs(result.residuals)))
        anchor_data.condition_number.append(result.condition_number)
        anchor_data.covariances.append(result.position_uncertainty if hasattr(result, 'position_uncertainty') else np.ones(3) * float('inf'))
        anchor_data.verification_vector.append(result.verification_value)
        anchor_data.residual_vector.append(result.residuals)
    
    def check_stopping_criteria(self, anchor_data: AnchorData) -> bool:
        """Check if stopping criteria are met for an anchor.
        
        Args:
            anchor_data: Data for the anchor
            
        Returns:
            True if stopping criteria are met, False otherwise
        """
        stopping_criteria = self.config.stopping_criteria.stopping_criteria
        
        # Always check number of measurements first
        if "nb_measurements" in stopping_criteria:
            if anchor_data.num_measurements_pre_estimation > self.config.stopping_criteria.number_of_measurements_thresh:
                logger.info(f"Stopping criterion 'nb_measurements' met for anchor {anchor_data.anchor_id}")
                return True
            elif stopping_criteria == ["nb_measurements"]:
                # If only checking for number of measurements, stop here
                return False
        
        # Need at least 2 iterations to check for convergence
        if len(anchor_data.GDOP) < 2:
            return False
        
        def check_criterion_convergence(values, ratio_threshold):
            """Check if a criterion has converged."""
            if len(values) < 2:
                return False
                
            current, previous = values[-1], values[-2]
            
            # Handle special cases
            if np.isinf(previous) or np.isnan(previous) or previous == 0:
                return False
                
            if np.isinf(current) or np.isnan(current):
                return False
                
            ratio = abs(current - previous) / abs(previous)
            return ratio < ratio_threshold
            
        def check_criterion_threshold(values, threshold, lower_is_better=True):
            """Check if a criterion has reached a threshold."""
            if len(values) < 1:
                return False
                
            value = values[-1]
            
            if np.isinf(value) or np.isnan(value):
                return False
                
            if lower_is_better:
                return value < threshold
            else:
                return value > threshold
        
        # Check each criterion in the stopping criteria list
        for criterion in stopping_criteria:
            if criterion == "nb_measurements":
                # Already checked above
                continue
                
            elif criterion == "GDOP":
                if not check_criterion_convergence(anchor_data.GDOP, 
                                                self.config.stopping_criteria.GDOP_ratio_thresh):
                    anchor_data.GDOP_convergence_counter = 0
                    continue
                    
                anchor_data.GDOP_convergence_counter += 1
                
                if (anchor_data.GDOP_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(anchor_data.GDOP, 
                                               self.config.stopping_criteria.GDOP_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'GDOP' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "FIM":
                # Use the inverse determinant of FIM (smaller is better)
                fim_det_inv = [1/np.linalg.det(fim) if np.linalg.det(fim) > 0 else float('inf') 
                             for fim in anchor_data.FIM[-2:]]
                             
                if not check_criterion_convergence(fim_det_inv, 
                                                self.config.stopping_criteria.FIM_ratio_thresh):
                    anchor_data.FIM_convergence_counter = 0
                    continue
                    
                anchor_data.FIM_convergence_counter += 1
                
                if (anchor_data.FIM_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(fim_det_inv, 
                                               self.config.stopping_criteria.FIM_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'FIM' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "residuals":
                if not check_criterion_convergence(anchor_data.residuals, 
                                                self.config.stopping_criteria.residuals_ratio_thresh):
                    anchor_data.residuals_convergence_counter = 0
                    continue
                    
                anchor_data.residuals_convergence_counter += 1
                
                if (anchor_data.residuals_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(anchor_data.residuals, 
                                               self.config.stopping_criteria.residuals_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'residuals' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "covariances":
                # Use maximum position uncertainty
                max_covs = [np.max(cov[:3]) for cov in anchor_data.covariances[-2:]]
                
                if not check_criterion_convergence(max_covs, 
                                                self.config.stopping_criteria.covariance_ratio_thresh):
                    anchor_data.covariances_convergence_counter = 0
                    continue
                    
                anchor_data.covariances_convergence_counter += 1
                
                if (anchor_data.covariances_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(max_covs, 
                                               self.config.stopping_criteria.covariance_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'covariances' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "condition_number":
                if not check_criterion_convergence(anchor_data.condition_number, 
                                                self.config.stopping_criteria.condition_number_ratio_thresh):
                    anchor_data.condition_number_convergence_counter = 0
                    continue
                    
                anchor_data.condition_number_convergence_counter += 1
                
                if (anchor_data.condition_number_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(anchor_data.condition_number, 
                                               self.config.stopping_criteria.condition_number_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'condition_number' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "verification_vector":
                if not check_criterion_convergence(anchor_data.verification_vector, 
                                                self.config.stopping_criteria.verification_vector_ratio_thresh):
                    anchor_data.verification_vector_convergence_counter = 0
                    continue
                    
                anchor_data.verification_vector_convergence_counter += 1
                
                if (anchor_data.verification_vector_convergence_counter <= 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    continue
                    
                if not check_criterion_threshold(anchor_data.verification_vector, 
                                               self.config.stopping_criteria.verification_vector_thresh):
                    continue
                    
                logger.info(f"Stopping criterion 'verification_vector' met for anchor {anchor_data.anchor_id}")
                return True
                
            elif criterion == "consecutive_distances_vector":
                # Check if position estimate has converged
                if anchor_data.consecutive_distances_vector[-1] < self.config.stopping_criteria.convergence_postion_thresh:
                    anchor_data.consecutive_distances_vector_convergence_counter += 1
                else:
                    anchor_data.consecutive_distances_vector_convergence_counter = 0
                    continue
                
                if (anchor_data.consecutive_distances_vector_convergence_counter > 
                    self.config.stopping_criteria.convergence_counter_threshold):
                    logger.info(f"Stopping criterion 'consecutive_distances_vector' met for anchor {anchor_data.anchor_id}")
                    return True
        
        # No stopping criteria met
        return False
    
    def handle_stopping_criteria_met(self, anchor_data: AnchorData) -> Optional[List[np.ndarray]]:
        """Handle the case when stopping criteria are met for an anchor.
        
        Args:
            anchor_data: Data for the anchor
            
        Returns:
            Optional list of waypoints if a trajectory was generated, None otherwise
        """
        logger.info(f"Stopping criteria met for anchor {anchor_data.anchor_id}")
        
        # Set the anchor status to indicate stopping criteria were met
        anchor_data.status = AnchorStatus.STOPPING_CRITERION_TRIGGERED
        
        # Refine estimate with nonlinear optimization
        self.refine_estimate_nonlinear(anchor_data)
        
        # Add to optimization queue if currently busy
        if self.trajectory_manager.state == TrajectoryState.ON_OPTIMAL_TRAJECTORY:
            self.trajectory_manager.add_anchor_to_optimization_queue(
                anchor_data.anchor_id, anchor_data.position
            )
            logger.info(f"Added anchor {anchor_data.anchor_id} to optimization queue")
            return None
            
        # Check if this is the closest anchor to optimize
        closest_anchor = self.trajectory_manager.find_closest_anchor_in_queue(self.drone_position)
        if closest_anchor is not None and closest_anchor != anchor_data.anchor_id:
            self.trajectory_manager.add_anchor_to_optimization_queue(
                anchor_data.anchor_id, anchor_data.position
            )
            logger.info(f"Anchor {anchor_data.anchor_id} not closest, added to queue")
            return None
            
        # Generate optimal trajectory for this anchor
        return self.optimize_trajectory_for_anchor(anchor_data)
    
    def refine_estimate_nonlinear(self, anchor_data: AnchorData) -> None:
        """Refine the anchor position estimate using nonlinear optimization.
        
        Args:
            anchor_data: Data for the anchor
        """
        # Get all measurements
        measurements = anchor_data.get_all_measurements()
        
        # Set up nonlinear estimation config
        estimation_config = EstimationConfig(
            use_linear_bias=self.config.least_squares.use_linear_bias,
            use_constant_bias=self.config.least_squares.use_constant_bias,
            normalised=self.config.least_squares.normalised,
            max_iterations=20,
            tolerance=1e-6
        )
        
        # Create estimator based on nonlinear optimization type
        nl_method = self.config.least_squares.non_linear_optimisation_type
        nl_method_str = nl_method.name.lower()
        
        # Map from internal enum to EstimationMethod names
        method_mapping = {
            "irls": "nonlinear_irls",
            "lm": "nonlinear_lm",
            "em": "nonlinear_em",
            "mm": "nonlinear_mm" 
        }
        
        estimator_method = method_mapping.get(nl_method_str, "nonlinear_mm")
        estimator = EstimationFactory.create_estimator(estimator_method, estimation_config)
        
        try:
            # Use current rough estimate as initial guess
            result = estimator.estimate(measurements, initial_guess=anchor_data.estimator)
            
            # Update anchor data with refined estimate
            anchor_data.update_estimator(result.estimator, result.covariance_matrix, is_non_linear=True)
            
            logger.info(f"Refined estimate for anchor {anchor_data.anchor_id} using {nl_method_str}")
            
        except Exception as e:
            logger.error(f"Error in nonlinear refinement for anchor {anchor_data.anchor_id}: {e}")
    
    def optimize_trajectory_for_anchor(self, anchor_data: AnchorData) -> List[np.ndarray]:
        """Generate an optimal trajectory for an anchor.
        
        Args:
            anchor_data: Data for the anchor
            
        Returns:
            List of waypoints for the optimal trajectory
        """
        # Get previous measurement positions
        previous_measurements = []
        for pos in anchor_data.positions_pre_rough_estimate:
            previous_measurements.append(np.array(pos))
            
        # Generate optimal trajectory
        full_waypoints = self.trajectory_manager.generate_optimal_trajectory(
            anchor_data.anchor_id,
            anchor_data.position,
            self.drone_position,
            previous_measurements
        )
        
        # Update anchor status
        anchor_data.status = AnchorStatus.OPTIMISED_TRAJECTORY
        anchor_data.optimal_waypoints = [tuple(wp) for wp in self.trajectory_manager.current_optimal_waypoints]
        
        # Update trajectory manager state
        self.trajectory_manager.state = TrajectoryState.ON_OPTIMAL_TRAJECTORY
        
        logger.info(f"Generated optimal trajectory for anchor {anchor_data.anchor_id} with {len(full_waypoints)} waypoints")
        return full_waypoints
    
    def finalize_anchor_initialization(self, anchor_data: AnchorData) -> None:
        """Finalize the initialization of an anchor after collecting all measurements.
        
        Args:
            anchor_data: Data for the anchor
        """
        # Get all measurements
        measurements = anchor_data.get_all_measurements()
        
        # Perform final nonlinear estimation
        self.refine_estimate_nonlinear(anchor_data)
        
        # Set the anchor status to initialized
        anchor_data.status = AnchorStatus.INITIALISED
        
        # Update trajectory manager state
        self.trajectory_manager.state = TrajectoryState.OPEN_TO_MEASUREMENTS
        self.trajectory_manager.current_optimal_waypoints = []
        
        logger.info(f"Finalized initialization for anchor {anchor_data.anchor_id}")
    
    def set_initial_mission(self, waypoints: List[Union[Tuple[float, float, float], np.ndarray]]) -> None:
        """Set the initial mission waypoints.
        
        Args:
            waypoints: List of mission waypoints [x, y, z]
        """
        self.trajectory_manager.set_initial_mission(waypoints)
    
    def calculate_position_error(self, real_position: np.ndarray, estimated_position: np.ndarray) -> float:
        """Calculate the error between estimated and real anchor positions.
        
        Args:
            real_position: Real ground truth position of the anchor
            estimated_position: Estimated position of the anchor
            
        Returns:
            Euclidean distance between the positions
        """
        return float(np.linalg.norm(np.array(real_position) - np.array(estimated_position)))
    
    def save_measurements_to_csv(self, anchor_id: str, filename: str) -> None:
        """Save the measurements for an anchor to a CSV file.
        
        Args:
            anchor_id: ID of the anchor
            filename: Path to the CSV file
        """
        anchor_data = self.get_anchor_data(anchor_id)
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["anchor_id", "distance", "x", "y", "z"])
            
            # Write pre-rough estimate measurements
            for distance, position in zip(
                anchor_data.distances_pre_rough_estimate, 
                anchor_data.positions_pre_rough_estimate
            ):
                x, y, z = position
                writer.writerow([anchor_id, distance, x, y, z])
            
            # Add separator
            writer.writerow([])
            
            # Write post-rough estimate measurements
            for distance, position in zip(
                anchor_data.distances_post_rough_estimate, 
                anchor_data.positions_post_rough_estimate
            ):
                x, y, z = position
                writer.writerow([anchor_id, distance, x, y, z])
        
        logger.info(f"Saved measurements for anchor {anchor_id} to {filename}")
    
    def update_config(self, config_dict: Dict[str, Any]) -> None:
        """Update configuration parameters from a dictionary.
        
        Args:
            config_dict: Dictionary of configuration parameters
        """
        self.config = UwbInitializationConfig.from_dict(config_dict)
        self._init_components()
        logger.info("Updated configuration parameters")
    
    def reset_measurements_post_rough_initialisation(self, anchor_id: str) -> None:
        """Reset the measurements collected after rough estimation.
        
        Args:
            anchor_id: ID of the anchor
        """
        anchor_data = self.get_anchor_data(anchor_id)
        anchor_data.status = AnchorStatus.OPTIMISED_TRAJECTORY
        anchor_data.distances_post_rough_estimate = []
        anchor_data.positions_post_rough_estimate = []
        anchor_data.estimator = anchor_data.estimator_rough_non_linear
        anchor_data.covariance_matrix = []
        
        logger.info(f"Reset post-rough estimation measurements for anchor {anchor_id}")
    
    def reset_all_measurements(self, anchor_id: str) -> None:
        """Reset all measurements for an anchor.
        
        Args:
            anchor_id: ID of the anchor
        """
        if anchor_id in self.anchor_data:
            self.anchor_data[anchor_id] = AnchorData(anchor_id=anchor_id)
            logger.info(f"Reset all measurements for anchor {anchor_id}")
    
    def get_anchor_status(self, anchor_id: str) -> str:
        """Get the status of an anchor.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            Status of the anchor as a string
        """
        if anchor_id not in self.anchor_data:
            return "unseen"
            
        return self.anchor_data[anchor_id].status.name.lower()
    
    def get_anchor_position(self, anchor_id: str) -> Optional[np.ndarray]:
        """Get the current estimated position of an anchor.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            Current estimated position of the anchor, or None if not available
        """
        if anchor_id not in self.anchor_data:
            return None
            
        return self.anchor_data[anchor_id].position
    
    def get_anchor_bias(self, anchor_id: str) -> Tuple[float, float]:
        """Get the current estimated bias terms for an anchor.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            Tuple of (constant_bias, linear_bias), or (0.0, 1.0) if not available
        """
        if anchor_id not in self.anchor_data:
            return (0.0, 1.0)
            
        return (self.anchor_data[anchor_id].bias, self.anchor_data[anchor_id].linear_bias)
    
    def get_anchor_estimator(self, anchor_id: str) -> Optional[np.ndarray]:
        """Get the current estimator for an anchor.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            Current estimator [x, y, z, constant_bias, linear_bias], or None if not available
        """
        if anchor_id not in self.anchor_data:
            return None
            
        return self.anchor_data[anchor_id].estimator
    
    def get_anchor_measurement_count(self, anchor_id: str) -> Tuple[int, int]:
        """Get the number of measurements for an anchor.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            Tuple of (pre_estimation_count, post_estimation_count)
        """
        if anchor_id not in self.anchor_data:
            return (0, 0)
            
        anchor_data = self.anchor_data[anchor_id]
        return (anchor_data.num_measurements_pre_estimation, anchor_data.num_measurements_post_estimation)
    
    def get_anchors_by_status(self, status: Union[str, AnchorStatus]) -> List[str]:
        """Get a list of anchor IDs with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of anchor IDs with the specified status
        """
        if isinstance(status, str):
            try:
                status = AnchorStatus[status.upper()]
            except KeyError:
                logger.warning(f"Invalid status: {status}")
                return []
                
        return [
            anchor_id for anchor_id, data in self.anchor_data.items()
            if data.status == status
        ]
    
    def get_optimization_queue(self) -> Dict[str, np.ndarray]:
        """Get the current optimization queue.
        
        Returns:
            Dictionary mapping anchor IDs to their estimated positions
        """
        return self.trajectory_manager.anchor_to_optimise_queue.copy()
    
    def get_trajectory_state(self) -> str:
        """Get the current trajectory state.
        
        Returns:
            Current trajectory state as a string
        """
        return self.trajectory_manager.state.name.lower()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the pipeline state to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the pipeline state
        """
        anchor_dict = {}
        for anchor_id, data in self.anchor_data.items():
            anchor_dict[anchor_id] = data.to_dict()
            
        return {
            "config": self.config.to_dict(),
            "drone_position": self.drone_position.tolist(),
            "anchor_data": anchor_dict,
            "trajectory_state": self.get_trajectory_state(),
            "optimization_queue": {k: v.tolist() for k, v in self.get_optimization_queue().items()},
            "current_optimal_waypoints": [wp.tolist() for wp in self.trajectory_manager.current_optimal_waypoints],
            "current_link_waypoints": [wp.tolist() for wp in self.trajectory_manager.current_link_waypoints],
            "passed_waypoints": [wp.tolist() for wp in self.trajectory_manager.passed_waypoints],
            "remaining_waypoints": [wp.tolist() for wp in self.trajectory_manager.remaining_waypoints]
        }
    
    @classmethod
    def from_dict(cls, state_dict: Dict[str, Any]) -> 'UwbInitializationPipeline':
        """Create a pipeline instance from a serialized state.
        
        Args:
            state_dict: Dictionary representation of the pipeline state
            
        Returns:
            Initialized UwbInitializationPipeline instance
        """
        # Create pipeline with config
        config = UwbInitializationConfig.from_dict(state_dict.get("config", {}))
        pipeline = cls(config)
        
        # Set drone position
        pipeline.drone_position = np.array(state_dict.get("drone_position", [0, 0, 0]))
        
        # Load anchor data
        for anchor_id, data_dict in state_dict.get("anchor_data", {}).items():
            pipeline.anchor_data[anchor_id] = AnchorData.from_dict(anchor_id, data_dict)
        
        # Set trajectory state
        trajectory_state = state_dict.get("trajectory_state", "open_to_measurements")
        if trajectory_state == "on_optimal_trajectory":
            pipeline.trajectory_manager.state = TrajectoryState.ON_OPTIMAL_TRAJECTORY
        else:
            pipeline.trajectory_manager.state = TrajectoryState.OPEN_TO_MEASUREMENTS
        
        # Load optimization queue
        for anchor_id, position in state_dict.get("optimization_queue", {}).items():
            pipeline.trajectory_manager.add_anchor_to_optimization_queue(anchor_id, np.array(position))
        
        # Load waypoints
        pipeline.trajectory_manager.current_optimal_waypoints = [
            np.array(wp) for wp in state_dict.get("current_optimal_waypoints", [])
        ]
        pipeline.trajectory_manager.current_link_waypoints = [
            np.array(wp) for wp in state_dict.get("current_link_waypoints", [])
        ]
        pipeline.trajectory_manager.passed_waypoints = [
            np.array(wp) for wp in state_dict.get("passed_waypoints", [])
        ]
        pipeline.trajectory_manager.remaining_waypoints = [
            np.array(wp) for wp in state_dict.get("remaining_waypoints", [])
        ]
        
        return pipeline
