#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os
import time
import json
import argparse
import itertools
from pathlib import Path
from copy import deepcopy
import logging
from typing import Dict, List, Tuple, Any, Optional, Union
import multiprocessing as mp
from tqdm import tqdm
import matplotlib.pyplot as plt

# Import pipeline components
from online_uwb_initialisation.core.uwb_online_initialisation_pipeline import UwbInitializationPipeline
from online_uwb_initialisation.core.config_params import (
    UwbInitializationConfig, RoughEstimateMethod, OutlierRemovalMethod, 
    NonLinearOptimizationType, TrajectoryOptimizationMethod, LinkMethod
)
from online_uwb_initialisation.core.anchor_data import AnchorStatus
from drone_uwb_simulator.UWB_protocol import Anchor, BiasModel, NoiseModel
from drone_uwb_simulator.drone_dynamics import Waypoint, Trajectory

# Setup logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("uwb_monte_carlo")


class UwbSimulationRunner:
    """Runs Monte Carlo simulations for UWB anchor localization pipeline."""
    
    def __init__(self, output_dir: str = "simulation_results", seed: Optional[int] = 42):
        """Initialize the simulation runner.
        
        Args:
            output_dir: Directory to save results
            seed: Random seed for reproducibility
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.seed = seed
        
        if seed is not None:
            np.random.seed(seed)
        
        # Default configuration
        self.config = UwbInitializationConfig()
        
        # Default anchor position and parameters
        self.anchor_position = np.array([2.0, 3.0, 0.0])  # Example position
        self.anchor_bias_model = BiasModel(constant_bias=0.1, linear_bias=1.02)
        self.anchor_noise_model = NoiseModel(variance=0.2, outlier_probability=0.05)

        # Initialize anchors list for multi-anchor simulations
        self.anchors = []
        
        logger.info(f"Initialized simulation runner with output directory: {output_dir}")

    def generate_trajectory(self, 
                         trajectory_type: str = "random", 
                         num_points: int = 100,
                         bounds: List[Tuple[float, float]] = None) -> List[np.ndarray]:
        """Generate a trajectory for data collection.
        
        Args:
            trajectory_type: Type of trajectory ("random", "spiral", "grid", "circular")
            num_points: Number of points in the trajectory
            bounds: Optional bounds for the trajectory [(x_min, x_max), (y_min, y_max), (z_min, z_max)]
            
        Returns:
            List of 3D points forming the trajectory
        """
        if bounds is None:
            bounds = [(-5, 5), (-5, 5), (0, 2)]
        
        trajectory = []
        
        if trajectory_type == "random":
            # Generate random points within bounds
            for _ in range(num_points):
                x = np.random.uniform(bounds[0][0], bounds[0][1])
                y = np.random.uniform(bounds[1][0], bounds[1][1])
                z = np.random.uniform(bounds[2][0], bounds[2][1])
                trajectory.append(np.array([x, y, z]))
                
        elif trajectory_type == "spiral":
            # Generate spiral trajectory
            t = np.linspace(0, 6*np.pi, num_points)
            radius_scale = min(bounds[0][1] - bounds[0][0], bounds[1][1] - bounds[1][0]) / 2
            
            for i in range(num_points):
                r = radius_scale * (1 - t[i] / (6*np.pi))
                x = r * np.cos(t[i])
                y = r * np.sin(t[i])
                z = bounds[2][0] + (bounds[2][1] - bounds[2][0]) * (t[i] / (6*np.pi))
                trajectory.append(np.array([x, y, z]))
                
        elif trajectory_type == "grid":
            # Generate grid trajectory
            grid_size = int(np.sqrt(num_points))
            x_vals = np.linspace(bounds[0][0], bounds[0][1], grid_size)
            y_vals = np.linspace(bounds[1][0], bounds[1][1], grid_size)
            z = (bounds[2][0] + bounds[2][1]) / 2
            
            points_added = 0
            for i, x in enumerate(x_vals):
                # Serpentine pattern
                row_y_vals = y_vals if i % 2 == 0 else y_vals[::-1]
                for y in row_y_vals:
                    trajectory.append(np.array([x, y, z]))
                    points_added += 1
                    if points_added >= num_points:
                        break
                if points_added >= num_points:
                    break
                    
        elif trajectory_type == "circular":
            # Generate circular trajectory at different heights
            radius = min(bounds[0][1] - bounds[0][0], bounds[1][1] - bounds[1][0]) / 2
            z_vals = np.linspace(bounds[2][0], bounds[2][1], int(np.sqrt(num_points)))
            points_per_circle = max(3, num_points // len(z_vals))
            
            for z in z_vals:
                theta_vals = np.linspace(0, 2*np.pi, points_per_circle, endpoint=False)
                for theta in theta_vals:
                    x = radius * np.cos(theta)
                    y = radius * np.sin(theta)
                    trajectory.append(np.array([x, y, z]))
                    if len(trajectory) >= num_points:
                        break
                if len(trajectory) >= num_points:
                    break
        
        # Ensure we have exactly num_points
        if len(trajectory) > num_points:
            trajectory = trajectory[:num_points]
        
        logger.info(f"Generated {len(trajectory)} points for {trajectory_type} trajectory")
        return trajectory

    def generate_measurements(self, 
                        trajectory,
                        anchor_position: Optional[np.ndarray] = None,
                        bias_model: Optional[BiasModel] = None,
                        noise_model: Optional[NoiseModel] = None) -> Tuple[List[Tuple[float, float, float]], List[float]]:
        """Generate distance measurements for a trajectory.
        
        Args:
            trajectory: List of 3D points or a Trajectory object
            anchor_position: Position of the anchor (default: self.anchor_position)
            bias_model: Bias model for measurements (default: self.anchor_bias_model)
            noise_model: Noise model for measurements (default: self.anchor_noise_model)
            
        Returns:
            Tuple of (positions, distances) where positions are 3D points and distances are measurements
        """
        if anchor_position is None:
            anchor_position = self.anchor_position
            
        if bias_model is None:
            bias_model = self.anchor_bias_model
            
        if noise_model is None:
            noise_model = self.anchor_noise_model
        
        # Create an anchor object for measurement simulation
        anchor = Anchor(
            anchor_id="test_anchor",
            position=anchor_position,
            bias_model=bias_model,
            noise_model=noise_model
        )
        
        # Check if trajectory is a Trajectory object
        if hasattr(trajectory, 'get_all_points'):
            logger.info("Converting Trajectory object to list of points")
            points = trajectory.get_all_points()
        # Check for spline attributes that might be present in Trajectory
        elif hasattr(trajectory, 'spline_x') and hasattr(trajectory, 'spline_y') and hasattr(trajectory, 'spline_z'):
            logger.info("Extracting points from trajectory splines")
            points = []
            for i in range(len(trajectory.spline_x)):
                points.append(np.array([trajectory.spline_x[i], trajectory.spline_y[i], trajectory.spline_z[i]]))
        else:
            # Assume trajectory is already a list of points
            points = trajectory
        
        positions = []
        distances = []
        
        for point in points:
            try:
                measurement = anchor.measure_distance(point)
                
                # Make sure we're using the measured distance with noise and bias
                if isinstance(measurement, float):
                    measured_distance = measurement
                else:
                    measured_distance = measurement.measured_distance
                    
                positions.append(tuple(point))
                distances.append(measured_distance)
            except Exception as e:
                logger.error(f"Error measuring distance at point {point}: {e}")
        
        logger.info(f"Generated {len(distances)} distance measurements")
        return positions, distances

    def save_trajectory_and_measurements(self, 
                                       positions: List[Tuple[float, float, float]], 
                                       distances: List[float],
                                       anchor_position: np.ndarray,
                                       bias_model: BiasModel,
                                       noise_model: NoiseModel,
                                       filename: str = "measurements.csv") -> str:
        """Save trajectory and measurements to CSV for reproducibility.
        
        Args:
            positions: List of 3D points
            distances: List of distance measurements
            anchor_position: True position of the anchor
            bias_model: Bias model used
            noise_model: Noise model used
            filename: Filename to save to
            
        Returns:
            Path to the saved file
        """
        file_path = self.output_dir / filename
        
        # Create DataFrame with positions and distances
        df = pd.DataFrame({
            "x": [p[0] for p in positions],
            "y": [p[1] for p in positions],
            "z": [p[2] for p in positions],
            "distance": distances
        })
        
        # Save dataframe to CSV
        df.to_csv(file_path, index=False)
        
        # Save metadata about the measurements
        metadata = {
            "anchor_position": anchor_position.tolist(),
            "constant_bias": bias_model.constant_bias,
            "linear_bias": bias_model.linear_bias,
            "noise_variance": noise_model.variance,
            "outlier_probability": noise_model.outlier_probability,
            "outlier_range": noise_model.outlier_range,
            "num_measurements": len(distances)
        }
        
        metadata_path = file_path.with_suffix('.json')
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        logger.info(f"Saved {len(distances)} measurements to {file_path}")
        logger.info(f"Saved metadata to {metadata_path}")
        
        return str(file_path)

    def load_trajectory_and_measurements(self, filename: str) -> Tuple[List[Tuple[float, float, float]], List[float], Dict[str, Any]]:
        """Load trajectory and measurements from CSV.
        
        Args:
            filename: Filename to load from
            
        Returns:
            Tuple of (positions, distances, metadata)
        """
        # Convert to Path object for better path handling
        file_path = Path(filename)
        
        # Check if the path already includes the output directory to avoid duplication
        # This is a specific fix for paths like "simulation_results/measurements.csv"
        output_dir_str = str(self.output_dir)
        if output_dir_str in str(file_path) or file_path.is_absolute():
            # Path already contains output dir or is absolute, use it as is
            pass
        else:
            # Path is just a filename, add output dir
            file_path = self.output_dir / file_path
        
        # Log the final path we're using
        logger.info(f"Loading trajectory and measurements from {file_path}")
        
        # Load measurements
        df = pd.read_csv(file_path)
        positions = [(row.x, row.y, row.z) for _, row in df.iterrows()]
        distances = df.distance.tolist()
        
        # Load metadata
        metadata_path = file_path.with_suffix('.json')
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
            
        logger.info(f"Loaded {len(distances)} measurements from {file_path}")
        return positions, distances, metadata

    def randomize_environment(self, randomize_anchor_params=True, randomize_positions=False):
        """Randomize the simulation environment by adjusting anchor parameters and positions.
        
        Args:
            randomize_anchor_params: Whether to randomize anchor bias and noise parameters
            randomize_positions: Whether to randomize anchor positions (only for multiple anchors)
        """
        logger.info("Randomizing environment")
        
        # Initialize anchors list if empty
        if not hasattr(self, 'anchors') or not self.anchors:
            self.anchors = [
                Anchor(
                    anchor_id="1",
                    position=self.anchor_position,
                    bias_model=self.anchor_bias_model,
                    noise_model=self.anchor_noise_model
                )
            ]
        
        # Randomize anchor parameters
        for index, anchor in enumerate(self.anchors):
            if randomize_anchor_params:
                # Random bias parameters (similar to your quick_uwb_initialisation_sim approach)
                constant_bias = np.random.uniform(0, 0.3)
                linear_bias = np.random.uniform(1, 1.03)
                noise_variance = np.random.uniform(0, 0.2)
                outlier_probability = np.random.uniform(0, 0.2)
                
                # Update anchor models
                anchor.bias_model = BiasModel(constant_bias=constant_bias, linear_bias=linear_bias)
                anchor.noise_model = NoiseModel(
                    variance=noise_variance, 
                    outlier_probability=outlier_probability
                )
                
                logger.info(f"Randomized anchor {anchor.anchor_id} parameters: "
                            f"bias={constant_bias:.3f}, linear_bias={linear_bias:.3f}, "
                            f"noise={noise_variance:.3f}, outlier_prob={outlier_probability:.3f}")
            
            if randomize_positions and len(self.anchors) > 1:
                # Only randomize positions if we have multiple anchors
                bounds = [(-5, 5), (-5, 5), (0, 3)]  # Default bounds
                
                # Generate a random position within bounds
                x = np.random.uniform(bounds[0][0], bounds[0][1])
                y = np.random.uniform(bounds[1][0], bounds[1][1])
                z = np.random.uniform(bounds[2][0], bounds[2][1])
                
                anchor.position = np.array([x, y, z])
                
                logger.info(f"Randomized anchor {anchor.anchor_id} position: [{x:.2f}, {y:.2f}, {z:.2f}]")
        
        # If this is a single anchor setup, update the class variables
        if len(self.anchors) == 1:
            self.anchor_position = self.anchors[0].position
            self.anchor_bias_model = self.anchors[0].bias_model
            self.anchor_noise_model = self.anchors[0].noise_model
        
        return self.anchors

    def setup_environment_drone_halle(self):
        """Set up the predefined drone halle environment with specific anchor positions.
        
        This replicates the environment setup from quick_uwb_initialisation_sim.py
        """
        logger.info("Setting up drone halle environment")
        
        # Drone halle predefined anchor positions
        anchor_positions = [
            [-2.502, -1.725, 0.223], 
            [3.052, -1.378, 0.888], 
            [-2.764, 1.080, 1.988], 
            [0.870, 3.464, 2.129]
        ]
        
        # Clear existing anchors
        self.anchors = []
        
        # Create anchors with randomized parameters
        for anchor_id, position in enumerate(anchor_positions, 1):
            # Randomize the anchor parameters
            constant_bias = np.random.uniform(-0.05, 0.05)
            linear_bias = np.random.uniform(1, 1.02)
            noise_variance = np.random.uniform(0.0, 0.1)
            outlier_probability = np.random.uniform(0.0, 0.1)
            
            anchor = Anchor(
                anchor_id=str(anchor_id),
                position=np.array(position),
                bias_model=BiasModel(constant_bias=constant_bias, linear_bias=linear_bias),
                noise_model=NoiseModel(
                    variance=noise_variance,
                    outlier_probability=outlier_probability
                )
            )
            self.anchors.append(anchor)
        
        # Update the class variables to match the first anchor (for compatibility)
        if self.anchors:
            self.anchor_position = self.anchors[0].position
            self.anchor_bias_model = self.anchors[0].bias_model
            self.anchor_noise_model = self.anchors[0].noise_model
        
        return self.anchors

    def setup_trajectory_drone_halle(self):
        """Set up the predefined trajectory for the drone halle environment.
        
        This replicates the trajectory setup from quick_uwb_initialisation_sim.py
        """
        logger.info("Setting up drone halle trajectory")
        
        # Define key waypoints
        trajectory_height = 1
        start_position = [2, -2.8, 0]
        hover_position = [2, -2.8, trajectory_height]
        intermediate_position = [2, -1.7, trajectory_height]
        opposite_position = [-1.25, 2.8, trajectory_height]
        hover_position2 = [1.25, -2.8, trajectory_height]
        end_position = [1.25, -2.8, 0]
        
        waypoints = [
            start_position, hover_position, intermediate_position, 
            opposite_position, hover_position2, end_position
        ]
        
        # Create Waypoint objects
        waypoint_objects = [Waypoint(*wp) for wp in waypoints]
        
        # Create trajectory
        drone_trajectory = Trajectory(dt=0.1, speed=0.05)
        drone_trajectory.construct_trajectory(waypoint_objects, method="linear")
        
        return drone_trajectory, waypoints

    def create_config_variations(self, variation_type: str) -> List[UwbInitializationConfig]:
        """Create variations of the configuration for testing.
        
        Args:
            variation_type: Type of variation to create
                ("linear_methods", "stopping_criteria", "nonlinear_methods", "trajectory_methods")
            
        Returns:
            List of configuration variations
        """
        configs = []
        
        if variation_type == "linear_methods":
            # Test different linear estimation methods
            rough_estimate_methods = [
                RoughEstimateMethod.SIMPLE_LINEAR,
                RoughEstimateMethod.LINEAR_REWEIGHTED
            ]
            
            outlier_removing_methods = [
                OutlierRemovalMethod.NONE,
                OutlierRemovalMethod.IMMEDIATE,
                OutlierRemovalMethod.COUNTER
            ]
            
            use_linear_bias_options = [True, False]
            use_constant_bias_options = [True, False]
            use_trimmed_reweighted_options = [True, False]
            
            # Skip invalid combinations (need at least one type of bias)
            for method, outlier_method, use_linear, use_constant, use_trimmed in itertools.product(
                rough_estimate_methods, outlier_removing_methods,
                use_linear_bias_options, use_constant_bias_options, use_trimmed_reweighted_options
            ):
                # Skip invalid combinations (need at least one type of bias)
                if not use_linear and not use_constant:
                    continue
                    
                # Create config variation
                config = deepcopy(self.config)
                config.least_squares.rough_estimate_method = method
                config.least_squares.outlier_removing = outlier_method
                config.least_squares.use_linear_bias = use_linear
                config.least_squares.use_constant_bias = use_constant
                config.least_squares.use_trimmed_reweighted = use_trimmed
                
                configs.append(config)
                
        elif variation_type == "stopping_criteria":
            # Test different stopping criteria
            available_criteria = [
                ["nb_measurements"],
                ["GDOP"],
                ["residuals"],
                ["condition_number"],
                ["covariances"],
                ["internal_constraint"],
                ["consecutive_distances_vector"],
                ["nb_measurements", "GDOP"],
                ["nb_measurements", "residuals"],
                ["nb_measurements", "condition_number"],
                ["GDOP", "residuals"],
                ["GDOP", "condition_number"]
            ]
            
            threshold_variations = [
                # Measurements threshold
                {"number_of_measurements_thresh": val}
                for val in [20, 30, 40, 50]
            ] + [
                # GDOP threshold
                {"GDOP_thresh": val}
                for val in [2.0, 3.0, 4.0, 5.0]
            ] + [
                # Residuals threshold
                {"residuals_thresh": val}
                for val in [50.0, 100.0, 150.0, 200.0]
            ]
            
            for criteria in available_criteria:
                for threshold_var in threshold_variations:
                    # Only apply relevant thresholds to the criteria
                    relevant = False
                    for key in threshold_var.keys():
                        criterion = key.split('_thresh')[0].lower()
                        if any(crit.lower() == criterion for crit in criteria):
                            relevant = True
                    
                    if not relevant:
                        continue
                        
                    config = deepcopy(self.config)
                    config.stopping_criteria.stopping_criteria = criteria
                    
                    # Apply threshold variation
                    for key, value in threshold_var.items():
                        setattr(config.stopping_criteria, key, value)
                    
                    configs.append(config)
                
        elif variation_type == "nonlinear_methods":
            # Test different nonlinear estimation methods
            nonlinear_methods = [
                NonLinearOptimizationType.LM,
                NonLinearOptimizationType.IRLS,
                NonLinearOptimizationType.GMM,
                NonLinearOptimizationType.EM
            ]
            
            for method in nonlinear_methods:
                config = deepcopy(self.config)
                config.least_squares.non_linear_optimisation_type = method
                configs.append(config)
                
        elif variation_type == "trajectory_methods":
            # Test different trajectory optimization methods
            trajectory_methods = [
                TrajectoryOptimizationMethod.GDOP,
                TrajectoryOptimizationMethod.FIM
            ]
            
            link_methods = [
                LinkMethod.STRICT_RETURN,
                LinkMethod.RETURN_TO_INITIAL,
                LinkMethod.STRAIGHT_TO_WAYPOINT,
                LinkMethod.RETURN_TO_CLOSEST,
                LinkMethod.HYBRID_RETURN,
                LinkMethod.OPTIMAL
            ]
            
            for traj_method, link_method in itertools.product(trajectory_methods, link_methods):
                config = deepcopy(self.config)
                config.trajectory.trajectory_optimisation_method = traj_method
                config.trajectory.link_method = link_method
                configs.append(config)
        
        logger.info(f"Created {len(configs)} configuration variations for {variation_type}")
        return configs

    def run_linear_methods_comparison(self, 
                                    measurements_file: str, 
                                    num_runs: int = 5,
                                    configs: Optional[List[UwbInitializationConfig]] = None) -> str:
        """Run comparison of different linear estimation methods.
        
        Args:
            measurements_file: Path to measurements file
            num_runs: Number of runs for each configuration
            configs: Optional list of configurations (if None, creates variations)
            
        Returns:
            Path to the results file
        """
        if configs is None:
            configs = self.create_config_variations("linear_methods")
            
        # Load measurements and metadata
        positions, distances, metadata = self.load_trajectory_and_measurements(measurements_file)
        anchor_position = np.array(metadata["anchor_position"])
        
        # Results structure
        results = []
        
        # Run tests for each config
        for config_idx, config in enumerate(tqdm(configs, desc="Testing linear methods")):
            method_name = config.least_squares.rough_estimate_method.name
            outlier_method = config.least_squares.outlier_removing.name
            use_linear = config.least_squares.use_linear_bias
            use_constant = config.least_squares.use_constant_bias
            use_trimmed = config.least_squares.use_trimmed_reweighted
            
            # Log configuration details
            logger.info(f"Testing config {config_idx+1}/{len(configs)}: "
                       f"{method_name}, Outlier: {outlier_method}, "
                       f"Linear bias: {use_linear}, Constant bias: {use_constant}, "
                       f"Trimmed: {use_trimmed}")
            
            # Run multiple times to account for randomness
            for run in range(num_runs):
                # Create a new pipeline instance with this config
                pipeline = UwbInitializationPipeline(config)
                anchor_id = "test_anchor"
                
                # Properly initialize trajectory manager
                initial_position = np.array([positions[0][0], positions[0][1], positions[0][2]])
                pipeline.trajectory_manager.passed_waypoints = [initial_position]
                
                # Create a basic mission plan from the measurement positions
                waypoints = [np.array([pos[0], pos[1], pos[2]]) for pos in positions[1:]]
                pipeline.trajectory_manager.set_initial_mission(waypoints)

                # Feed each measurement to the pipeline
                measurement_indices = []
                gdop_values = []
                residuals = []
                condition_numbers = []
                position_errors = []
                constant_bias_errors = []
                linear_bias_errors = []
                
                # Feed all measurements at once
                for i, (pos, dist) in enumerate(zip(positions, distances)):
                    # Process the measurement
                    # Update the trajectory manager with current position
                    current_position = np.array([pos[0], pos[1], pos[2]])
                    pipeline.trajectory_manager.update_passed_waypoint(current_position)
                    pipeline.measurement_callback(pos, dist, anchor_id)
                    
                    # Get the anchor data
                    if anchor_id in pipeline.anchor_data:
                        anchor_data = pipeline.anchor_data[anchor_id]
                        
                        # Record metrics if available
                        if len(anchor_data.GDOP) > 0:
                            # Record metrics
                            measurement_indices.append(i + 1)  # 1-based index
                            gdop_values.append(anchor_data.GDOP[-1])
                            
                            if len(anchor_data.residuals) > 0:
                                residuals.append(anchor_data.residuals[-1])
                            else:
                                residuals.append(float('nan'))
                                
                            if len(anchor_data.condition_number) > 0:
                                condition_numbers.append(anchor_data.condition_number[-1])
                            else:
                                condition_numbers.append(float('nan'))
                                
                            # Calculate errors if estimate available
                            if len(anchor_data.estimator_rough_linear) >= 5:
                                est_pos = anchor_data.estimator_rough_linear[:3]
                                est_const_bias = anchor_data.estimator_rough_linear[3]
                                est_linear_bias = anchor_data.estimator_rough_linear[4]
                                
                                # Calculate errors
                                pos_error = np.linalg.norm(est_pos - anchor_position)
                                const_bias_error = abs(est_const_bias - metadata["constant_bias"])
                                linear_bias_error = abs(est_linear_bias - metadata["linear_bias"])
                                
                                position_errors.append(pos_error)
                                constant_bias_errors.append(const_bias_error)
                                linear_bias_errors.append(linear_bias_error)
                            else:
                                position_errors.append(float('nan'))
                                constant_bias_errors.append(float('nan'))
                                linear_bias_errors.append(float('nan'))
                
                # Record the final results
                results.append({
                    "run": run + 1,
                    "method": method_name,
                    "outlier_method": outlier_method,
                    "use_linear_bias": use_linear,
                    "use_constant_bias": use_constant,
                    "use_trimmed_reweighted": use_trimmed,
                    "final_position_error": position_errors[-1] if position_errors else float('nan'),
                    "final_constant_bias_error": constant_bias_errors[-1] if constant_bias_errors else float('nan'),
                    "final_linear_bias_error": linear_bias_errors[-1] if linear_bias_errors else float('nan'),
                    "final_gdop": gdop_values[-1] if gdop_values else float('nan'),
                    "final_residual": residuals[-1] if residuals else float('nan'),
                    "final_condition_number": condition_numbers[-1] if condition_numbers else float('nan'),
                    "measurement_indices": measurement_indices,
                    "position_errors": position_errors,
                    "constant_bias_errors": constant_bias_errors,
                    "linear_bias_errors": linear_bias_errors,
                    "gdop_values": gdop_values,
                    "residuals": residuals,
                    "condition_numbers": condition_numbers
                })
        
        # Create summary results
        summary_results = []
        for config_idx, config in enumerate(configs):
            method_name = config.least_squares.rough_estimate_method.name
            outlier_method = config.least_squares.outlier_removing.name
            use_linear = config.least_squares.use_linear_bias
            use_constant = config.least_squares.use_constant_bias
            use_trimmed = config.least_squares.use_trimmed_reweighted
            
            # Filter results for this configuration
            config_results = [r for r in results if 
                             r["method"] == method_name and
                             r["outlier_method"] == outlier_method and
                             r["use_linear_bias"] == use_linear and
                             r["use_constant_bias"] == use_constant and
                             r["use_trimmed_reweighted"] == use_trimmed]
            
            # Calculate average metrics
            avg_position_error = np.mean([r["final_position_error"] for r in config_results])
            avg_constant_bias_error = np.mean([r["final_constant_bias_error"] for r in config_results])
            avg_linear_bias_error = np.mean([r["final_linear_bias_error"] for r in config_results])
            
            # Calculate standard deviations
            std_position_error = np.std([r["final_position_error"] for r in config_results])
            std_constant_bias_error = np.std([r["final_constant_bias_error"] for r in config_results])
            std_linear_bias_error = np.std([r["final_linear_bias_error"] for r in config_results])
            
            summary_results.append({
                "method": method_name,
                "outlier_method": outlier_method,
                "use_linear_bias": use_linear,
                "use_constant_bias": use_constant,
                "use_trimmed_reweighted": use_trimmed,
                "avg_position_error": avg_position_error,
                "avg_constant_bias_error": avg_constant_bias_error,
                "avg_linear_bias_error": avg_linear_bias_error,
                "std_position_error": std_position_error,
                "std_constant_bias_error": std_constant_bias_error,
                "std_linear_bias_error": std_linear_bias_error
            })
        
        # Save results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = self.output_dir / f"linear_methods_results_{timestamp}.csv"
        summary_file = self.output_dir / f"linear_methods_summary_{timestamp}.csv"
        
        # Save detailed results
        pd.DataFrame(results).to_csv(results_file, index=False)
        
        # Save summary results
        pd.DataFrame(summary_results).to_csv(summary_file, index=False)
        
        logger.info(f"Saved linear methods results to {results_file}")
        logger.info(f"Saved linear methods summary to {summary_file}")
        
        # Save time series data for each configuration
        for config_idx, config in enumerate(configs):
            method_name = config.least_squares.rough_estimate_method.name
            outlier_method = config.least_squares.outlier_removing.name
            use_linear = config.least_squares.use_linear_bias
            use_constant = config.least_squares.use_constant_bias
            use_trimmed = config.least_squares.use_trimmed_reweighted
            
            # Create a readable config name
            config_name = f"{method_name}_{outlier_method}_L{int(use_linear)}C{int(use_constant)}T{int(use_trimmed)}"
            
            # Filter results for this configuration
            config_results = [r for r in results if 
                             r["method"] == method_name and
                             r["outlier_method"] == outlier_method and
                             r["use_linear_bias"] == use_linear and
                             r["use_constant_bias"] == use_constant and
                             r["use_trimmed_reweighted"] == use_trimmed]
            
            # Save time series data for each run
            for run_idx, run_result in enumerate(config_results):
                timeseries_data = []
                for i in range(len(run_result["measurement_indices"])):
                    timeseries_data.append({
                        "measurement_index": run_result["measurement_indices"][i],
                        "position_error": run_result["position_errors"][i],
                        "constant_bias_error": run_result["constant_bias_errors"][i],
                        "linear_bias_error": run_result["linear_bias_errors"][i],
                        "gdop": run_result["gdop_values"][i],
                        "residual": run_result["residuals"][i],
                        "condition_number": run_result["condition_numbers"][i]
                    })
                
                # Save to CSV
                timeseries_file = self.output_dir / f"linear_timeseries_{config_name}_run{run_idx+1}_{timestamp}.csv"
                pd.DataFrame(timeseries_data).to_csv(timeseries_file, index=False)
        
        return str(results_file)

    def run_stopping_criteria_comparison(self, 
                                       measurements_file: str,
                                       num_runs: int = 5,
                                       configs: Optional[List[UwbInitializationConfig]] = None) -> str:
        """Run comparison of different stopping criteria settings.
        
        Args:
            measurements_file: Path to measurements file
            num_runs: Number of runs for each configuration
            configs: Optional list of configurations (if None, creates variations)
            
        Returns:
            Path to the results file
        """
        if configs is None:
            configs = self.create_config_variations("stopping_criteria")
            
        # Load measurements and metadata
        positions, distances, metadata = self.load_trajectory_and_measurements(measurements_file)
        anchor_position = np.array(metadata["anchor_position"])
        
        # Results structure
        results = []
        
        # Run tests for each config
        for config_idx, config in enumerate(tqdm(configs, desc="Testing stopping criteria")):
            criteria = config.stopping_criteria.stopping_criteria
            
            # Extract the relevant thresholds as a string
            threshold_str = ""
            for criterion in criteria:
                if criterion == "nb_measurements":
                    threshold_str += f"NM{config.stopping_criteria.number_of_measurements_thresh}_"
                elif criterion == "GDOP":
                    threshold_str += f"G{config.stopping_criteria.GDOP_thresh}_"
                elif criterion == "residuals":
                    threshold_str += f"R{config.stopping_criteria.residuals_thresh}_"
                elif criterion == "condition_number":
                    threshold_str += f"CN{config.stopping_criteria.condition_number_thresh}_"
                    
            threshold_str = threshold_str.rstrip('_')
            
            # Log configuration details
            logger.info(f"Testing config {config_idx+1}/{len(configs)}: "
                       f"Criteria: {criteria}, Thresholds: {threshold_str}")
            
            # Run multiple times to account for randomness
            for run in range(num_runs):
                # Create a new pipeline instance with this config
                pipeline = UwbInitializationPipeline(config)
                anchor_id = "test_anchor"
                
                # Feed measurements and track when stopping criteria are met
                stopping_criteria_met = False
                stopping_measurement_idx = -1
                num_measurements_at_stopping = 0
                
                for i, (pos, dist) in enumerate(zip(positions, distances)):
                    # Process the measurement
                    result = pipeline.measurement_callback(pos, dist, anchor_id)
                    
                    # Check if stopping criteria were met
                    if not stopping_criteria_met and result is not None:
                        stopping_criteria_met = True
                        stopping_measurement_idx = i
                        
                        if anchor_id in pipeline.anchor_data:
                            anchor_data = pipeline.anchor_data[anchor_id]
                            num_measurements_at_stopping = anchor_data.num_measurements_pre_estimation
                            
                            # Calculate errors at stopping point
                            if len(anchor_data.estimator_rough_linear) >= 5:
                                est_pos = anchor_data.estimator_rough_linear[:3]
                                est_const_bias = anchor_data.estimator_rough_linear[3]
                                est_linear_bias = anchor_data.estimator_rough_linear[4]
                                
                                # Calculate errors
                                pos_error = np.linalg.norm(est_pos - anchor_position)
                                const_bias_error = abs(est_const_bias - metadata["constant_bias"])
                                linear_bias_error = abs(est_linear_bias - metadata["linear_bias"])
                                
                                # Record the results
                                results.append({
                                    "run": run + 1,
                                    "criteria": "_".join(criteria),
                                    "thresholds": threshold_str,
                                    "stopping_measurement_idx": stopping_measurement_idx,
                                    "num_measurements_at_stopping": num_measurements_at_stopping,
                                    "position_error": pos_error,
                                    "constant_bias_error": const_bias_error,
                                    "linear_bias_error": linear_bias_error
                                })
                            break
                
                # If stopping criteria were never met, record that
                if not stopping_criteria_met:
                    results.append({
                        "run": run + 1,
                        "criteria": "_".join(criteria),
                        "thresholds": threshold_str,
                        "stopping_measurement_idx": -1,
                        "num_measurements_at_stopping": 0,
                        "position_error": float('nan'),
                        "constant_bias_error": float('nan'),
                        "linear_bias_error": float('nan')
                    })
        
        # Create summary results
        summary_results = []
        for config_idx, config in enumerate(configs):
            criteria = "_".join(config.stopping_criteria.stopping_criteria)
            
            # Extract thresholds
            threshold_str = ""
            for criterion in config.stopping_criteria.stopping_criteria:
                if criterion == "nb_measurements":
                    threshold_str += f"NM{config.stopping_criteria.number_of_measurements_thresh}_"
                elif criterion == "GDOP":
                    threshold_str += f"G{config.stopping_criteria.GDOP_thresh}_"
                elif criterion == "residuals":
                    threshold_str += f"R{config.stopping_criteria.residuals_thresh}_"
                elif criterion == "condition_number":
                    threshold_str += f"CN{config.stopping_criteria.condition_number_thresh}_"
                    
            threshold_str = threshold_str.rstrip('_')
            
            # Filter results for this configuration
            config_results = [r for r in results if 
                             r["criteria"] == criteria and
                             r["thresholds"] == threshold_str]
            
            # Calculate average metrics, skipping NaN values
            valid_results = [r for r in config_results if not np.isnan(r["position_error"])]
            
            if valid_results:
                avg_stopping_idx = np.mean([r["stopping_measurement_idx"] for r in valid_results])
                avg_num_measurements = np.mean([r["num_measurements_at_stopping"] for r in valid_results])
                avg_position_error = np.mean([r["position_error"] for r in valid_results])
                avg_constant_bias_error = np.mean([r["constant_bias_error"] for r in valid_results])
                avg_linear_bias_error = np.mean([r["linear_bias_error"] for r in valid_results])
                
                # Calculate standard deviations
                std_stopping_idx = np.std([r["stopping_measurement_idx"] for r in valid_results])
                std_num_measurements = np.std([r["num_measurements_at_stopping"] for r in valid_results])
                std_position_error = np.std([r["position_error"] for r in valid_results])
                std_constant_bias_error = np.std([r["constant_bias_error"] for r in valid_results])
                std_linear_bias_error = np.std([r["linear_bias_error"] for r in valid_results])
                
                # Count how many times criteria were met
                criteria_met_count = len(valid_results)
            else:
                avg_stopping_idx = float('nan')
                avg_num_measurements = float('nan')
                avg_position_error = float('nan')
                avg_constant_bias_error = float('nan')
                avg_linear_bias_error = float('nan')
                std_stopping_idx = float('nan')
                std_num_measurements = float('nan')
                std_position_error = float('nan')
                std_constant_bias_error = float('nan')
                std_linear_bias_error = float('nan')
                criteria_met_count = 0
                
            summary_results.append({
                "criteria": criteria,
                "thresholds": threshold_str,
                "avg_stopping_idx": avg_stopping_idx,
                "avg_num_measurements": avg_num_measurements,
                "avg_position_error": avg_position_error,
                "avg_constant_bias_error": avg_constant_bias_error,
                "avg_linear_bias_error": avg_linear_bias_error,
                "std_stopping_idx": std_stopping_idx,
                "std_num_measurements": std_num_measurements,
                "std_position_error": std_position_error,
                "std_constant_bias_error": std_constant_bias_error,
                "std_linear_bias_error": std_linear_bias_error,
                "criteria_met_count": criteria_met_count,
                "total_runs": num_runs
            })
        
        # Save results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = self.output_dir / f"stopping_criteria_results_{timestamp}.csv"
        summary_file = self.output_dir / f"stopping_criteria_summary_{timestamp}.csv"
        
        # Save detailed results
        pd.DataFrame(results).to_csv(results_file, index=False)
        
        # Save summary results
        pd.DataFrame(summary_results).to_csv(summary_file, index=False)
        
        logger.info(f"Saved stopping criteria results to {results_file}")
        logger.info(f"Saved stopping criteria summary to {summary_file}")
        
        return str(results_file)

    def run_nonlinear_methods_comparison(self, 
                                      measurements_file: str, 
                                      num_runs: int = 5,
                                      configs: Optional[List[UwbInitializationConfig]] = None) -> str:
        """Run comparison of different nonlinear estimation methods.
        
        Args:
            measurements_file: Path to measurements file
            num_runs: Number of runs for each configuration
            configs: Optional list of configurations (if None, creates variations)
            
        Returns:
            Path to the results file
        """
        if configs is None:
            configs = self.create_config_variations("nonlinear_methods")
            
        # Load measurements and metadata
        positions, distances, metadata = self.load_trajectory_and_measurements(measurements_file)
        anchor_position = np.array(metadata["anchor_position"])
        
        # Results structure
        results = []
        
        # Run tests for each config
        for config_idx, config in enumerate(tqdm(configs, desc="Testing nonlinear methods")):
            method_name = config.least_squares.non_linear_optimisation_type.name
            
            # Log configuration details
            logger.info(f"Testing config {config_idx+1}/{len(configs)}: {method_name}")
            
            # Run multiple times to account for randomness
            for run in range(num_runs):
                # Create a new pipeline instance with this config
                pipeline = UwbInitializationPipeline(config)
                anchor_id = "test_anchor"
                
                # Feed each measurement to the pipeline
                for pos, dist in zip(positions, distances):
                    pipeline.measurement_callback(pos, dist, anchor_id)
                
                # Check if the anchor data exists
                if anchor_id in pipeline.anchor_data:
                    anchor_data = pipeline.anchor_data[anchor_id]
                    
                    # Trigger stopping criteria and nonlinear refinement
                    if anchor_data.status == AnchorStatus.SEEN:
                        # Manually trigger stopping criteria
                        anchor_data.status = AnchorStatus.STOPPING_CRITERION_TRIGGERED
                        
                        # Refine the estimate using nonlinear method
                        pipeline.refine_estimate_nonlinear(anchor_data)
                    
                    # Calculate errors if nonlinear estimate available
                    if len(anchor_data.estimator_rough_non_linear) >= 5:
                        est_pos = anchor_data.estimator_rough_non_linear[:3]
                        est_const_bias = anchor_data.estimator_rough_non_linear[3]
                        est_linear_bias = anchor_data.estimator_rough_non_linear[4]
                        
                        # Calculate errors
                        pos_error = np.linalg.norm(est_pos - anchor_position)
                        const_bias_error = abs(est_const_bias - metadata["constant_bias"])
                        linear_bias_error = abs(est_linear_bias - metadata["linear_bias"])
                        
                        # Get linear errors for comparison
                        if len(anchor_data.estimator_rough_linear) >= 5:
                            linear_est_pos = anchor_data.estimator_rough_linear[:3]
                            linear_pos_error = np.linalg.norm(linear_est_pos - anchor_position)
                            improvement = linear_pos_error - pos_error
                        else:
                            linear_pos_error = float('nan')
                            improvement = float('nan')
                        
                        # Record time for refinement if available
                        refinement_time = getattr(anchor_data, 'refinement_time', float('nan'))
                        
                        # Record the results
                        results.append({
                            "run": run + 1,
                            "method": method_name,
                            "position_error": pos_error,
                            "constant_bias_error": const_bias_error,
                            "linear_bias_error": linear_bias_error,
                            "linear_position_error": linear_pos_error,
                            "improvement": improvement,
                            "num_measurements": anchor_data.num_measurements_pre_estimation,
                            "refinement_time": refinement_time
                        })
                    else:
                        # Record failure
                        results.append({
                            "run": run + 1,
                            "method": method_name,
                            "position_error": float('nan'),
                            "constant_bias_error": float('nan'),
                            "linear_bias_error": float('nan'),
                            "linear_position_error": float('nan'),
                            "improvement": float('nan'),
                            "num_measurements": anchor_data.num_measurements_pre_estimation,
                            "refinement_time": float('nan')
                        })
        
        # Create summary results
        summary_results = []
        for config_idx, config in enumerate(configs):
            method_name = config.least_squares.non_linear_optimisation_type.name
            
            # Filter results for this configuration
            config_results = [r for r in results if r["method"] == method_name]
            
            # Calculate average metrics
            valid_results = [r for r in config_results if not np.isnan(r["position_error"])]
            
            if valid_results:
                avg_position_error = np.mean([r["position_error"] for r in valid_results])
                avg_constant_bias_error = np.mean([r["constant_bias_error"] for r in valid_results])
                avg_linear_bias_error = np.mean([r["linear_bias_error"] for r in valid_results])
                avg_improvement = np.mean([r["improvement"] for r in valid_results 
                                         if not np.isnan(r["improvement"])])
                avg_refinement_time = np.mean([r["refinement_time"] for r in valid_results
                                             if not np.isnan(r["refinement_time"])])
                
                # Calculate standard deviations
                std_position_error = np.std([r["position_error"] for r in valid_results])
                std_constant_bias_error = np.std([r["constant_bias_error"] for r in valid_results])
                std_linear_bias_error = np.std([r["linear_bias_error"] for r in valid_results])
                std_improvement = np.std([r["improvement"] for r in valid_results
                                        if not np.isnan(r["improvement"])])
                std_refinement_time = np.std([r["refinement_time"] for r in valid_results
                                            if not np.isnan(r["refinement_time"])])
                
                # Count successful refinements
                success_count = len(valid_results)
            else:
                avg_position_error = float('nan')
                avg_constant_bias_error = float('nan')
                avg_linear_bias_error = float('nan')
                avg_improvement = float('nan')
                avg_refinement_time = float('nan')
                std_position_error = float('nan')
                std_constant_bias_error = float('nan')
                std_linear_bias_error = float('nan')
                std_improvement = float('nan')
                std_refinement_time = float('nan')
                success_count = 0
                
            summary_results.append({
                "method": method_name,
                "avg_position_error": avg_position_error,
                "avg_constant_bias_error": avg_constant_bias_error,
                "avg_linear_bias_error": avg_linear_bias_error,
                "avg_improvement": avg_improvement,
                "avg_refinement_time": avg_refinement_time,
                "std_position_error": std_position_error,
                "std_constant_bias_error": std_constant_bias_error,
                "std_linear_bias_error": std_linear_bias_error,
                "std_improvement": std_improvement,
                "std_refinement_time": std_refinement_time,
                "success_count": success_count,
                "total_runs": num_runs
            })
        
        # Save results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = self.output_dir / f"nonlinear_methods_results_{timestamp}.csv"
        summary_file = self.output_dir / f"nonlinear_methods_summary_{timestamp}.csv"
        
        # Save detailed results
        pd.DataFrame(results).to_csv(results_file, index=False)
        
        # Save summary results
        pd.DataFrame(summary_results).to_csv(summary_file, index=False)
        
        logger.info(f"Saved nonlinear methods results to {results_file}")
        logger.info(f"Saved nonlinear methods summary to {summary_file}")
        
        return str(results_file)

    def run_trajectory_methods_comparison(self, 
                                       measurements_file: str, 
                                       num_runs: int = 5,
                                       configs: Optional[List[UwbInitializationConfig]] = None) -> str:
        """Run comparison of different trajectory optimization methods.
        
        Args:
            measurements_file: Path to measurements file
            num_runs: Number of runs for each configuration
            configs: Optional list of configurations (if None, creates variations)
            
        Returns:
            Path to the results file
        """
        if configs is None:
            configs = self.create_config_variations("trajectory_methods")
            
        # Load measurements and metadata
        positions, distances, metadata = self.load_trajectory_and_measurements(measurements_file)
        anchor_position = np.array(metadata["anchor_position"])
        
        # Results structure
        results = []
        
        # Run tests for each config
        for config_idx, config in enumerate(tqdm(configs, desc="Testing trajectory methods")):
            traj_method = config.trajectory.trajectory_optimisation_method.name
            link_method = config.trajectory.link_method.name
            
            # Log configuration details
            logger.info(f"Testing config {config_idx+1}/{len(configs)}: "
                       f"Trajectory: {traj_method}, Link: {link_method}")
            
            # Run multiple times to account for randomness
            for run in range(num_runs):
                # Create a new pipeline instance with this config
                pipeline = UwbInitializationPipeline(config)
                anchor_id = "test_anchor"
                
                # Feed each measurement to the pipeline to get initial linear estimate
                for pos, dist in zip(positions[:50], distances[:50]):  # Use subset for initial estimation
                    pipeline.measurement_callback(pos, dist, anchor_id)
                
                # Get the anchor data after initial measurements
                if anchor_id in pipeline.anchor_data:
                    anchor_data = pipeline.anchor_data[anchor_id]
                    
                    # Manually trigger stopping criteria to force trajectory optimization
                    if anchor_data.status == AnchorStatus.SEEN:
                        anchor_data.status = AnchorStatus.STOPPING_CRITERION_TRIGGERED
                        
                        # Get initial estimate
                        initial_pos = anchor_data.estimator_rough_linear[:3]
                        initial_pos_error = np.linalg.norm(initial_pos - anchor_position)
                        
                        # Run trajectory optimization
                        start_time = time.time()
                        
                        # Set up dummy waypoints for the trajectory manager
                        pipeline.trajectory_manager.remaining_waypoints = [
                            np.array([5.0, 5.0, 5.0]), np.array([6.0, 6.0, 5.0])
                        ]
                        
                        # Get current position (last measurement point)
                        current_pos = positions[49]
                        
                        # Get previous measurement positions
                        previous_measurements = [np.array(p) for p in positions[:50]]
                        
                        # Generate optimal trajectory
                        optimized_waypoints = pipeline.trajectory_manager.generate_optimal_trajectory(
                            anchor_id, anchor_data.estimator_rough_linear[:3], current_pos, previous_measurements
                        )
                        
                        # Calculate time taken
                        traj_time = time.time() - start_time
                        
                        # Continue simulation with optimized trajectory if available
                        if optimized_waypoints and len(optimized_waypoints) > 0:
                            # Record trajectory statistics
                            num_waypoints = len(optimized_waypoints)
                            avg_step_size = np.mean([
                                np.linalg.norm(optimized_waypoints[i] - optimized_waypoints[i-1])
                                for i in range(1, len(optimized_waypoints))
                            ]) if len(optimized_waypoints) > 1 else 0
                            
                            # Calculate total path length
                            total_length = sum([
                                np.linalg.norm(optimized_waypoints[i] - optimized_waypoints[i-1])
                                for i in range(1, len(optimized_waypoints))
                            ]) if len(optimized_waypoints) > 1 else 0
                            
                            # Feed measurements along the optimized trajectory
                            # Simulate taking measurements at each waypoint
                            for waypoint in optimized_waypoints:
                                # Create an anchor for simulating measurements
                                anchor = Anchor(
                                    anchor_id="test_anchor",
                                    position=anchor_position,
                                    bias_model=BiasModel(
                                        constant_bias=metadata["constant_bias"],
                                        linear_bias=metadata["linear_bias"]
                                    ),
                                    noise_model=NoiseModel(
                                        variance=metadata["noise_variance"],
                                        outlier_probability=metadata["outlier_probability"]
                                    )
                                )
                                
                                # Simulate a measurement at this waypoint
                                measurement = anchor.measure_distance(waypoint)
                                if isinstance(measurement, float):
                                    measured_distance = measurement
                                else:
                                    measured_distance = measurement.measured_distance
                                
                                # Feed to pipeline
                                pipeline.measurement_callback(waypoint, measured_distance, anchor_id)
                            
                            # Get final estimate after trajectory optimization
                            if anchor_id in pipeline.anchor_data:
                                anchor_data = pipeline.anchor_data[anchor_id]
                                
                                if len(anchor_data.estimator) >= 5:
                                    final_pos = anchor_data.estimator[:3]
                                    final_pos_error = np.linalg.norm(final_pos - anchor_position)
                                    improvement = initial_pos_error - final_pos_error
                                else:
                                    final_pos_error = float('nan')
                                    improvement = float('nan')
                            else:
                                final_pos_error = float('nan')
                                improvement = float('nan')
                                
                            # Record trajectory metrics
                            results.append({
                                "run": run + 1,
                                "trajectory_method": traj_method,
                                "link_method": link_method,
                                "initial_position_error": initial_pos_error,
                                "final_position_error": final_pos_error,
                                "improvement": improvement,
                                "num_waypoints": num_waypoints,
                                "avg_step_size": avg_step_size,
                                "total_length": total_length,
                                "optimization_time": traj_time
                            })
                        else:
                            # Record failure
                            results.append({
                                "run": run + 1,
                                "trajectory_method": traj_method,
                                "link_method": link_method,
                                "initial_position_error": initial_pos_error,
                                "final_position_error": float('nan'),
                                "improvement": float('nan'),
                                "num_waypoints": 0,
                                "avg_step_size": 0,
                                "total_length": 0,
                                "optimization_time": traj_time
                            })
        
        # Create summary results
        summary_results = []
        for config_idx, config in enumerate(configs):
            traj_method = config.trajectory.trajectory_optimisation_method.name
            link_method = config.trajectory.link_method.name
            
            # Filter results for this configuration
            config_results = [r for r in results if 
                             r["trajectory_method"] == traj_method and
                             r["link_method"] == link_method]
            
            # Calculate average metrics
            valid_results = [r for r in config_results if not np.isnan(r["final_position_error"])]
            
            if valid_results:
                avg_initial_error = np.mean([r["initial_position_error"] for r in valid_results])
                avg_final_error = np.mean([r["final_position_error"] for r in valid_results])
                avg_improvement = np.mean([r["improvement"] for r in valid_results])
                avg_num_waypoints = np.mean([r["num_waypoints"] for r in valid_results])
                avg_step_size = np.mean([r["avg_step_size"] for r in valid_results])
                avg_total_length = np.mean([r["total_length"] for r in valid_results])
                avg_optimization_time = np.mean([r["optimization_time"] for r in valid_results])
                
                # Calculate standard deviations
                std_initial_error = np.std([r["initial_position_error"] for r in valid_results])
                std_final_error = np.std([r["final_position_error"] for r in valid_results])
                std_improvement = np.std([r["improvement"] for r in valid_results])
                std_num_waypoints = np.std([r["num_waypoints"] for r in valid_results])
                std_step_size = np.std([r["avg_step_size"] for r in valid_results])
                std_total_length = np.std([r["total_length"] for r in valid_results])
                std_optimization_time = np.std([r["optimization_time"] for r in valid_results])
                
                # Count successful optimizations
                success_count = len(valid_results)
            else:
                avg_initial_error = float('nan')
                avg_final_error = float('nan')
                avg_improvement = float('nan')
                avg_num_waypoints = float('nan')
                avg_step_size = float('nan')
                avg_total_length = float('nan')
                avg_optimization_time = float('nan')
                std_initial_error = float('nan')
                std_final_error = float('nan')
                std_improvement = float('nan')
                std_num_waypoints = float('nan')
                std_step_size = float('nan')
                std_total_length = float('nan')
                std_optimization_time = float('nan')
                success_count = 0
                
            summary_results.append({
                "trajectory_method": traj_method,
                "link_method": link_method,
                "avg_initial_error": avg_initial_error,
                "avg_final_error": avg_final_error,
                "avg_improvement": avg_improvement,
                "avg_num_waypoints": avg_num_waypoints,
                "avg_step_size": avg_step_size,
                "avg_total_length": avg_total_length,
                "avg_optimization_time": avg_optimization_time,
                "std_initial_error": std_initial_error,
                "std_final_error": std_final_error,
                "std_improvement": std_improvement,
                "std_num_waypoints": std_num_waypoints,
                "std_step_size": std_step_size,
                "std_total_length": std_total_length,
                "std_optimization_time": std_optimization_time,
                "success_count": success_count,
                "total_runs": num_runs
            })
        
        # Save results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = self.output_dir / f"trajectory_methods_results_{timestamp}.csv"
        summary_file = self.output_dir / f"trajectory_methods_summary_{timestamp}.csv"
        
        # Save detailed results
        pd.DataFrame(results).to_csv(results_file, index=False)
        
        # Save summary results
        pd.DataFrame(summary_results).to_csv(summary_file, index=False)
        
        logger.info(f"Saved trajectory methods results to {results_file}")
        logger.info(f"Saved trajectory methods summary to {summary_file}")
        
        return str(results_file)

    def run_multi_anchor_simulation(self, num_runs=10, randomize_env=True, env_type="random"):
        """Run multi-anchor simulation with multiple randomized environments.
        
        Args:
            num_runs: Number of simulation runs with different environments
            randomize_env: Whether to randomize environment parameters between runs
            env_type: Type of environment setup ("random" or "drone_halle")
            
        Returns:
            Path to results file
        """
        logger.info(f"Running multi-anchor simulation with {num_runs} environments")
        
        # Results storage
        results = []
        
        # Run simulations
        for run in range(num_runs):
            logger.info(f"Starting run {run+1}/{num_runs}")
            
            # Set up environment
            if env_type == "drone_halle":
                self.setup_environment_drone_halle()
                trajectory, waypoints = self.setup_trajectory_drone_halle()
                trajectory = trajectory.get_all_points()
            else:
                if randomize_env:
                    self.randomize_environment(
                        randomize_anchor_params=True,
                        randomize_positions=(len(self.anchors) > 1)
                    )
                trajectory = self.generate_trajectory(
                    trajectory_type="spiral", 
                    num_points=100
                )
            
            # Process each anchor
            for anchor in self.anchors:
                anchor_id = anchor.anchor_id
                logger.info(f"Processing anchor {anchor_id}")
                
                # Generate measurements
                positions, distances = self.generate_measurements(
                    trajectory=trajectory,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model
                )
                
                # Save measurements for reproducibility
                measurements_file = self.save_trajectory_and_measurements(
                    positions=positions,
                    distances=distances,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model,
                    filename=f"measurements_run{run+1}_anchor{anchor_id}.csv"
                )
                
                # Run the pipeline with different configurations
                configs = self.create_config_variations("linear_methods")
                
                # Limit to a few key configurations for efficiency
                if len(configs) > 4:
                    # Pick representative configurations
                    configs = configs[::len(configs)//4][:4]
                
                for config_idx, config in enumerate(tqdm(configs, desc=f"Testing configurations for anchor {anchor_id}")):
                    method_name = config.least_squares.rough_estimate_method.name
                    outlier_method = config.least_squares.outlier_removing.name
                    
                    # Create a pipeline instance with this config
                    pipeline = UwbInitializationPipeline(config)
                    
                    # Feed each measurement to the pipeline
                    for pos, dist in zip(positions, distances):
                        pipeline.measurement_callback(pos, dist, anchor_id)
                    
                    # Check if the anchor data exists
                    if anchor_id in pipeline.anchor_data:
                        anchor_data = pipeline.anchor_data[anchor_id]
                        
                        # Calculate errors if estimate available
                        if len(anchor_data.estimator_rough_linear) >= 5:
                            est_pos = anchor_data.estimator_rough_linear[:3]
                            est_const_bias = anchor_data.estimator_rough_linear[3]
                            est_linear_bias = anchor_data.estimator_rough_linear[4]
                            
                            # Calculate errors
                            pos_error = np.linalg.norm(est_pos - anchor.position)
                            const_bias_error = abs(est_const_bias - anchor.bias_model.constant_bias)
                            linear_bias_error = abs(est_linear_bias - anchor.bias_model.linear_bias)
                            
                            # Record results
                            results.append({
                                "run": run + 1,
                                "anchor_id": anchor_id,
                                "method": method_name,
                                "outlier_method": outlier_method,
                                "position_error": pos_error,
                                "constant_bias_error": const_bias_error,
                                "linear_bias_error": linear_bias_error,
                                "anchor_position": anchor.position.tolist(),
                                "estimated_position": est_pos.tolist(),
                                "constant_bias": anchor.bias_model.constant_bias,
                                "linear_bias": anchor.bias_model.linear_bias,
                                "noise_variance": anchor.noise_model.variance,
                                "outlier_probability": anchor.noise_model.outlier_probability,
                                "num_measurements": len(positions)
                            })
                        else:
                            logger.warning(f"No linear estimate available for anchor {anchor_id}")
                    else:
                        logger.warning(f"Anchor {anchor_id} not found in pipeline data")
        
        # Save results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = self.output_dir / f"multi_anchor_results_{timestamp}.csv"
        pd.DataFrame(results).to_csv(results_file, index=False)
        
        logger.info(f"Saved multi-anchor results to {results_file}")
        
        return str(results_file)

    def run_simulation_batch(self, batch_name="comprehensive", num_runs=10):
        """Run a predefined batch of simulations.
        
        Args:
            batch_name: Name of the batch configuration to run
            num_runs: Number of runs per configuration
            
        Returns:
            Dict of results paths for each component
        """
        results = {}
        
        if batch_name == "comprehensive":
            # Run all major simulation types with optimal settings
            logger.info("Running comprehensive simulation batch")
            
            # 1. Multi-anchor simulation with random environment
            logger.info("Running multi-anchor simulation with random environments")
            results["multi_anchor_random"] = self.run_multi_anchor_simulation(
                num_runs=num_runs, 
                randomize_env=True,
                env_type="random"
            )
            
            # 2. Multi-anchor simulation with drone halle environment
            logger.info("Running multi-anchor simulation with drone halle environment")
            results["multi_anchor_drone_halle"] = self.run_multi_anchor_simulation(
                num_runs=num_runs,
                randomize_env=True,
                env_type="drone_halle"
            )
            
            # 3. Linear methods comparison
            logger.info("Running linear methods comparison")
            # Generate a single consistent environment for comparing methods
            self.randomize_environment()
            trajectory = self.generate_trajectory(trajectory_type="spiral")
            positions, distances = self.generate_measurements(trajectory)
            
            # FIX: Use an absolute path or just the filename, not a relative path
            measurements_filename = "measurements.csv"
            measurements_file = self.save_trajectory_and_measurements(
                positions, distances, self.anchor_position, 
                self.anchor_bias_model, self.anchor_noise_model,
                filename=measurements_filename
            )
            
            print(f"Saved measurements file: {measurements_file}")
            print(f"Output directory: {self.output_dir}")
            print(f"Absolute path to check: {Path(measurements_file).absolute()}")

            # Now measurements_file should be an absolute path string
            # Make sure to use it directly in the next calls
            results["linear_methods"] = self.run_linear_methods_comparison(
                measurements_file=measurements_file,  # Use the absolute path returned by save_trajectory_and_measurements
                num_runs=1  # Using 1 here as we're comparing methods, not environments
            )
            
            # Also use the same absolute path for other calls
            results["stopping_criteria"] = self.run_stopping_criteria_comparison(
                measurements_file=measurements_file,
                num_runs=1
            )
            
            # 4. Stopping criteria comparison
            logger.info("Running stopping criteria comparison")
            results["stopping_criteria"] = self.run_stopping_criteria_comparison(
                measurements_file=measurements_file,
                num_runs=1  # Using 1 here as we're comparing criteria, not environments
            )
            
            # 5. Nonlinear methods comparison
            logger.info("Running nonlinear methods comparison")
            results["nonlinear_methods"] = self.run_nonlinear_methods_comparison(
                measurements_file=measurements_file,
                num_runs=1  # Using 1 here as we're comparing methods, not environments
            )
            
            # 6. Trajectory methods comparison
            logger.info("Running trajectory methods comparison")
            results["trajectory_methods"] = self.run_trajectory_methods_comparison(
                measurements_file=measurements_file,
                num_runs=1  # Using 1 here as we're comparing methods, not environments
            )
        
        elif batch_name == "drone_halle":
            # Focus on drone halle environment with realistic parameters
            logger.info("Running drone halle simulation batch")
            
            # Set up drone halle environment
            self.setup_environment_drone_halle()
            trajectory, _ = self.setup_trajectory_drone_halle()
            
            # Run full pipeline on each anchor
            anchor_results = []
            for anchor in self.anchors:
                logger.info(f"Processing anchor {anchor.anchor_id}")
                
                # Generate measurements
                positions, distances = self.generate_measurements(
                    trajectory=trajectory,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model
                )
                
                # Save measurements
                measurements_file = self.save_trajectory_and_measurements(
                    positions=positions,
                    distances=distances,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model,
                    filename=f"drone_halle_anchor{anchor.anchor_id}.csv"
                )
                
                # Run linear methods comparison for this anchor
                result_file = self.run_linear_methods_comparison(
                    measurements_file=measurements_file,
                    num_runs=1
                )
                
                anchor_results.append({
                    "anchor_id": anchor.anchor_id,
                    "position": anchor.position.tolist(),
                    "constant_bias": anchor.bias_model.constant_bias,
                    "linear_bias": anchor.bias_model.linear_bias,
                    "noise_variance": anchor.noise_model.variance,
                    "outlier_probability": anchor.noise_model.outlier_probability,
                    "result_file": result_file
                })
            
            # Save anchor results summary
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            summary_file = self.output_dir / f"drone_halle_summary_{timestamp}.json"
            with open(summary_file, 'w') as f:
                json.dump(anchor_results, f, indent=2)
            
            results["drone_halle"] = str(summary_file)
        
        elif batch_name == "noise_sensitivity":
            # Focus on sensitivity to noise parameters
            logger.info("Running noise sensitivity simulation batch")
            
            # Define noise parameter ranges
            noise_variances = [0.0, 0.05, 0.1, 0.2, 0.3]
            outlier_probs = [0.0, 0.05, 0.1, 0.2]
            
            # Generate a consistent trajectory
            trajectory = self.generate_trajectory(trajectory_type="spiral")
            
            # Results storage
            noise_results = []
            
            # Run simulations for each noise configuration
            for variance in noise_variances:
                for outlier_prob in outlier_probs:
                    logger.info(f"Testing noise variance={variance}, outlier probability={outlier_prob}")
                    
                    # Update noise model
                    self.anchor_noise_model = NoiseModel(
                        variance=variance,
                        outlier_probability=outlier_prob
                    )
                    
                    # Generate measurements
                    positions, distances = self.generate_measurements(
                        trajectory=trajectory,
                        noise_model=self.anchor_noise_model
                    )
                    
                    # Save measurements
                    measurements_file = self.save_trajectory_and_measurements(
                        positions=positions,
                        distances=distances,
                        anchor_position=self.anchor_position,
                        bias_model=self.anchor_bias_model,
                        noise_model=self.anchor_noise_model,
                        filename=f"noise_v{variance}_op{outlier_prob}.csv"
                    )
                    
                    # Run a simplified linear methods comparison
                    config = UwbInitializationConfig()
                    pipeline = UwbInitializationPipeline(config)
                    anchor_id = "test_anchor"
                    
                    # Feed measurements
                    for pos, dist in zip(positions, distances):
                        pipeline.measurement_callback(pos, dist, anchor_id)
                    
                    # Get results
                    if anchor_id in pipeline.anchor_data:
                        anchor_data = pipeline.anchor_data[anchor_id]
                        
                        if len(anchor_data.estimator_rough_linear) >= 5:
                            est_pos = anchor_data.estimator_rough_linear[:3]
                            est_const_bias = anchor_data.estimator_rough_linear[3]
                            est_linear_bias = anchor_data.estimator_rough_linear[4]
                            
                            # Calculate errors
                            pos_error = np.linalg.norm(est_pos - self.anchor_position)
                            const_bias_error = abs(est_const_bias - self.anchor_bias_model.constant_bias)
                            linear_bias_error = abs(est_linear_bias - self.anchor_bias_model.linear_bias)
                            
                            # Record results
                            noise_results.append({
                                "noise_variance": variance,
                                "outlier_probability": outlier_prob,
                                "position_error": pos_error,
                                "constant_bias_error": const_bias_error,
                                "linear_bias_error": linear_bias_error,
                                "num_measurements": len(positions)
                            })
                        else:
                            logger.warning("No linear estimate available")
                    else:
                        logger.warning(f"Anchor {anchor_id} not found in pipeline data")
            
            # Save noise results
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            noise_file = self.output_dir / f"noise_sensitivity_{timestamp}.csv"
            pd.DataFrame(noise_results).to_csv(noise_file, index=False)
            
            results["noise_sensitivity"] = str(noise_file)
        
        return results

def simulation_worker(chunk, idx, test_name, measurements_file, num_runs, output_dir, seed):
    """Worker function for parallel simulations."""
    # Create a new simulator instance for this process
    worker_output_dir = f"{output_dir}/process_{idx}"
    local_simulator = UwbSimulationRunner(
        output_dir=worker_output_dir,
        seed=seed + idx if seed is not None else None
    )
    
    # Ensure the measurements file path is absolute
    measurements_path = Path(measurements_file)
    if not measurements_path.is_absolute():
        # Use the original measurements file from the parent directory
        measurements_path = Path(output_dir) / measurements_path.name
    
    # Run the appropriate test
    if test_name == "linear":
        result_file = local_simulator.run_linear_methods_comparison(
            str(measurements_path), num_runs=num_runs, configs=chunk)
    elif test_name == "stopping":
        result_file = local_simulator.run_stopping_criteria_comparison(
            str(measurements_path), num_runs=num_runs, configs=chunk)
    elif test_name == "nonlinear":
        result_file = local_simulator.run_nonlinear_methods_comparison(
            str(measurements_path), num_runs=num_runs, configs=chunk)
    elif test_name == "trajectory":
        result_file = local_simulator.run_trajectory_methods_comparison(
            str(measurements_path), num_runs=num_runs, configs=chunk)
    else:
        logger.error(f"Unknown test name: {test_name}")
        return None
        
    return result_file

def run_parallel_simulations(simulator, test_name, measurements_file, configs, num_runs, parallel_processes=4):
    """Run simulations in parallel.
    
    Args:
        simulator: UwbSimulationRunner instance
        test_name: Name of the test to run ("linear", "stopping", "nonlinear", "trajectory")
        measurements_file: Path to measurements file
        configs: List of configurations to test
        num_runs: Number of runs per configuration
        parallel_processes: Number of parallel processes to use
        
    Returns:
        List of result file paths
    """
    # Split configs into chunks for parallel processing
    config_chunks = np.array_split(configs, parallel_processes)
    
    # Create pool and run simulations
    with mp.Pool(processes=parallel_processes) as pool:
        results = []
        for i, chunk in enumerate(config_chunks):
            results.append(pool.apply_async(
                simulation_worker, 
                args=(chunk, i, test_name, measurements_file, num_runs, 
                      simulator.output_dir, simulator.seed)
            ))
        
        # Get results
        result_files = [r.get() for r in results]
        
    return result_files

def plot_summary_results(summary_file, plot_type, output_dir=None):
    """Create summary plots for results.
    
    Args:
        summary_file: Path to summary file
        plot_type: Type of plot to create ("linear", "stopping", "nonlinear", "trajectory")
        output_dir: Output directory for plots
    """
    try:
        # Load summary data
        df = pd.read_csv(summary_file)
        
        if output_dir is None:
            output_dir = Path(summary_file).parent
        else:
            output_dir = Path(output_dir)
            
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if plot_type == "linear":
            # Plot position error by method
            plt.figure(figsize=(12, 8))
            methods = df['method'].unique()
            
            # Group by method and outlier removal
            grouped = df.groupby(['method', 'outlier_method'])
            
            positions = np.arange(len(grouped))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(14, 8))
            
            bars = ax.bar(positions, grouped['avg_position_error'].mean(), width,
                         yerr=grouped['std_position_error'].mean(),
                         label='Position Error')
            
            # Add labels and title
            ax.set_ylabel('Average Position Error (m)')
            ax.set_title('Position Error by Method and Outlier Removal')
            ax.set_xticks(positions)
            ax.set_xticklabels([f"{m}\n{o}" for (m, o) in grouped.groups.keys()], 
                              rotation=45, ha='right')
            ax.legend()
            
            plt.tight_layout()
            plt.savefig(output_dir / 'linear_position_error.png')
            
            # Plot effect of bias terms
            plt.figure(figsize=(14, 8))
            bias_grouped = df.groupby(['use_linear_bias', 'use_constant_bias'])
            
            positions = np.arange(len(bias_grouped))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, bias_grouped['avg_position_error'].mean(), width,
                         yerr=bias_grouped['std_position_error'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Position Error (m)')
            ax.set_title('Effect of Bias Terms on Position Error')
            ax.set_xticks(positions)
            ax.set_xticklabels([f"Linear: {l}, Constant: {c}" for (l, c) in bias_grouped.groups.keys()])
            
            plt.tight_layout()
            plt.savefig(output_dir / 'linear_bias_effect.png')
            
        elif plot_type == "stopping":
            # Plot number of measurements by criteria
            plt.figure(figsize=(14, 8))
            criteria_grouped = df.groupby('criteria')
            
            positions = np.arange(len(criteria_grouped))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, criteria_grouped['avg_num_measurements'].mean(), width,
                         yerr=criteria_grouped['std_num_measurements'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Number of Measurements')
            ax.set_title('Number of Measurements by Stopping Criteria')
            ax.set_xticks(positions)
            ax.set_xticklabels(criteria_grouped.groups.keys(), rotation=45, ha='right')
            
            plt.tight_layout()
            plt.savefig(output_dir / 'stopping_num_measurements.png')
            
            # Plot position error by criteria
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, criteria_grouped['avg_position_error'].mean(), width,
                         yerr=criteria_grouped['std_position_error'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Position Error (m)')
            ax.set_title('Position Error by Stopping Criteria')
            ax.set_xticks(positions)
            ax.set_xticklabels(criteria_grouped.groups.keys(), rotation=45, ha='right')
            
            plt.tight_layout()
            plt.savefig(output_dir / 'stopping_position_error.png')
            
            # Plot success rate by criteria
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            success_rates = criteria_grouped['criteria_met_count'].mean() / df['total_runs'].iloc[0] * 100
            
            bars = ax.bar(positions, success_rates, width)
            
            # Add labels and title
            ax.set_ylabel('Success Rate (%)')
            ax.set_title('Success Rate by Stopping Criteria')
            ax.set_xticks(positions)
            ax.set_xticklabels(criteria_grouped.groups.keys(), rotation=45, ha='right')
            
            plt.tight_layout()
            plt.savefig(output_dir / 'stopping_success_rate.png')
            
        elif plot_type == "nonlinear":
            # Plot position error by method
            plt.figure(figsize=(14, 8))
            methods = df['method'].unique()
            
            positions = np.arange(len(methods))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            method_grouped = df.groupby('method')
            
            bars = ax.bar(positions, method_grouped['avg_position_error'].mean(), width,
                         yerr=method_grouped['std_position_error'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Position Error (m)')
            ax.set_title('Position Error by Nonlinear Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'nonlinear_position_error.png')
            
            # Plot improvement over linear method
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, method_grouped['avg_improvement'].mean(), width,
                         yerr=method_grouped['std_improvement'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Improvement (m)')
            ax.set_title('Improvement over Linear Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'nonlinear_improvement.png')
            
            # Plot computation time
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, method_grouped['avg_refinement_time'].mean(), width,
                         yerr=method_grouped['std_refinement_time'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Computation Time (s)')
            ax.set_title('Computation Time by Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'nonlinear_computation_time.png')
            
        elif plot_type == "trajectory":
            # Plot position improvement by method
            plt.figure(figsize=(14, 8))
            
            traj_methods = df['trajectory_method'].unique()
            link_methods = df['link_method'].unique()
            
            grouped = df.groupby('trajectory_method')
            
            positions = np.arange(len(traj_methods))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, grouped['avg_improvement'].mean(), width,
                         yerr=grouped['std_improvement'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Improvement (m)')
            ax.set_title('Position Improvement by Trajectory Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(traj_methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'trajectory_improvement.png')
            
            # Plot trajectory length by method
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, grouped['avg_total_length'].mean(), width,
                         yerr=grouped['std_total_length'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Trajectory Length (m)')
            ax.set_title('Trajectory Length by Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(traj_methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'trajectory_length.png')
            
            # Plot computation time by method
            plt.figure(figsize=(14, 8))
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            bars = ax.bar(positions, grouped['avg_optimization_time'].mean(), width,
                         yerr=grouped['std_optimization_time'].mean())
            
            # Add labels and title
            ax.set_ylabel('Average Computation Time (s)')
            ax.set_title('Optimization Time by Method')
            ax.set_xticks(positions)
            ax.set_xticklabels(traj_methods)
            
            plt.tight_layout()
            plt.savefig(output_dir / 'trajectory_computation_time.png')
        
        logger.info(f"Created summary plots for {plot_type} in {output_dir}")
        
    except Exception as e:
        logger.error(f"Error creating plots: {e}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="UWB Anchor Localization Monte Carlo Simulation")
    
    # General settings
    parser.add_argument("--output-dir", type=str, default="simulation_results",
                      help="Directory to save results")
    parser.add_argument("--seed", type=int, default=42,
                      help="Random seed for reproducibility")
    parser.add_argument("--num-runs", type=int, default=10,
                      help="Number of runs per simulation")
    parser.add_argument("--num-processes", type=int, default=4,
                      help="Number of parallel processes")
    
    # Simulation modes
    parser.add_argument("--mode", type=str, 
                       choices=["comprehensive", "linear", "stopping", "nonlinear", "trajectory", 
                                "multi_anchor", "drone_halle", "noise_sensitivity"],
                       default="comprehensive", help="Simulation mode to run")
    
    # Environment settings
    parser.add_argument("--env-type", type=str, 
                       choices=["random", "drone_halle"],
                       default="random", help="Environment type")
    parser.add_argument("--randomize-env", action="store_true",
                      help="Randomize environment parameters")
    parser.add_argument("--num-anchors", type=int, default=1,
                      help="Number of anchors (for multi-anchor simulations)")
    
    # Data generation settings
    parser.add_argument("--generate-data", action="store_true",
                      help="Generate new simulation data")
    parser.add_argument("--measurements-file", type=str, default="measurements.csv",
                      help="File with measurements to use (if not generating new data)")
    parser.add_argument("--trajectory-type", type=str, 
                      choices=["random", "spiral", "grid", "circular"],
                      default="spiral", help="Type of trajectory to generate")
    parser.add_argument("--num-points", type=int, default=100,
                      help="Number of points in the trajectory")
    
    # Anchor settings
    parser.add_argument("--anchor-x", type=float, default=2.0,
                      help="X-coordinate of the anchor")
    parser.add_argument("--anchor-y", type=float, default=3.0,
                      help="Y-coordinate of the anchor")
    parser.add_argument("--anchor-z", type=float, default=0.0,
                      help="Z-coordinate of the anchor")
    parser.add_argument("--constant-bias", type=float, default=0.1,
                      help="Constant bias of the anchor")
    parser.add_argument("--linear-bias", type=float, default=1.02,
                      help="Linear bias of the anchor")
    parser.add_argument("--noise-variance", type=float, default=0.2,
                      help="Noise variance of the anchor")
    parser.add_argument("--outlier-probability", type=float, default=0.05,
                      help="Outlier probability of the anchor")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize simulator
    simulator = UwbSimulationRunner(output_dir=args.output_dir, seed=args.seed)
    
    # Set anchor parameters
    simulator.anchor_position = np.array([args.anchor_x, args.anchor_y, args.anchor_z])
    simulator.anchor_bias_model = BiasModel(constant_bias=args.constant_bias, linear_bias=args.linear_bias)
    simulator.anchor_noise_model = NoiseModel(variance=args.noise_variance, outlier_probability=args.outlier_probability)
    
    # Set up environment based on specified type
    if args.env_type == "drone_halle":
        simulator.setup_environment_drone_halle()
        if args.generate_data:
            trajectory, _ = simulator.setup_trajectory_drone_halle()
    elif args.randomize_env:
        # Create multiple anchors if requested
        if args.num_anchors > 1 and not hasattr(simulator, 'anchors'):
            simulator.anchors = []
            for i in range(args.num_anchors):
                # Generate random position
                x = np.random.uniform(-5, 5)
                y = np.random.uniform(-5, 5)
                z = np.random.uniform(0, 3)
                
                anchor = Anchor(
                    anchor_id=f"{i+1}",
                    position=np.array([x, y, z]),
                    bias_model=simulator.anchor_bias_model,
                    noise_model=simulator.anchor_noise_model
                )
                simulator.anchors.append(anchor)
                
        simulator.randomize_environment(
            randomize_anchor_params=True,
            randomize_positions=(args.num_anchors > 1)
        )
    
    # Generate data if needed
    measurements_file = args.measurements_file
    if args.generate_data:
        # Generate trajectory and measurements
        if not hasattr(simulator, 'trajectory'):
            trajectory = simulator.generate_trajectory(
                trajectory_type=args.trajectory_type,
                num_points=args.num_points
            )
        
        # Generate measurements
        if args.env_type == "drone_halle" or args.num_anchors > 1:
            # Multi-anchor measurements
            all_measurements = []
            for anchor in simulator.anchors:
                positions, distances = simulator.generate_measurements(
                    trajectory=trajectory,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model
                )
                
                # Save measurements
                anchor_file = f"measurements_{anchor.anchor_id}.csv"
                simulator.save_trajectory_and_measurements(
                    positions=positions,
                    distances=distances,
                    anchor_position=anchor.position,
                    bias_model=anchor.bias_model,
                    noise_model=anchor.noise_model,
                    filename=anchor_file
                )
                all_measurements.append((anchor.anchor_id, anchor_file))
                
            # Use the first anchor's file as the default
            if all_measurements:
                measurements_file = all_measurements[0][1]
        else:
            # Single anchor measurements
            positions, distances = simulator.generate_measurements(
                trajectory=trajectory,
                anchor_position=simulator.anchor_position,
                bias_model=simulator.anchor_bias_model,
                noise_model=simulator.anchor_noise_model
            )
            
            # Save measurements
            measurements_file = simulator.save_trajectory_and_measurements(
                positions=positions,
                distances=distances,
                anchor_position=simulator.anchor_position,
                bias_model=simulator.anchor_bias_model,
                noise_model=simulator.anchor_noise_model,
                filename=args.measurements_file
            )
    else:
        # Use existing measurements file
        if not Path(measurements_file).is_absolute():
            measurements_file = str(output_dir / measurements_file)
    
    # Run simulations based on mode
    if args.mode == "comprehensive":
        results = simulator.run_simulation_batch(
            batch_name="comprehensive",
            num_runs=args.num_runs
        )
        
        # Create summary of all results
        summary = {
            "simulation_parameters": vars(args),
            "results": results
        }
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        summary_file = output_dir / f"comprehensive_summary_{timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
            
        logger.info(f"Saved comprehensive simulation summary to {summary_file}")
        
    elif args.mode == "multi_anchor":
        result_file = simulator.run_multi_anchor_simulation(
            num_runs=args.num_runs,
            randomize_env=args.randomize_env,
            env_type=args.env_type
        )
        
        logger.info(f"Saved multi-anchor simulation results to {result_file}")
        
    elif args.mode == "drone_halle":
        results = simulator.run_simulation_batch(
            batch_name="drone_halle",
            num_runs=args.num_runs
        )
        
        logger.info(f"Saved drone halle simulation results to {results['drone_halle']}")
        
    elif args.mode == "noise_sensitivity":
        results = simulator.run_simulation_batch(
            batch_name="noise_sensitivity",
            num_runs=1  # Just 1 run needed as we're systematically testing noise parameters
        )
        
        logger.info(f"Saved noise sensitivity results to {results['noise_sensitivity']}")
        
    elif args.mode == "linear":
        # Run linear methods comparison
        configs = simulator.create_config_variations("linear_methods")
        
        if args.num_processes > 1:
            result_files = run_parallel_simulations(
                simulator=simulator,
                test_name="linear",
                measurements_file=measurements_file,
                configs=configs,
                num_runs=args.num_runs,
                parallel_processes=args.num_processes
            )
            
            # Merge results if multiple processes were used
            if result_files and len(result_files) > 1:
                # Find summary files
                summary_files = []
                for result_file in result_files:
                    if result_file:
                        result_path = Path(result_file)
                        summary_path = result_path.parent / result_file.replace("results", "summary")
                        if summary_path.exists():
                            summary_files.append(summary_path)
                
                # Merge summary files
                if summary_files:
                    merged_summary = pd.concat([pd.read_csv(f) for f in summary_files])
                    merged_summary_path = output_dir / f"linear_methods_summary_merged.csv"
                    merged_summary.to_csv(merged_summary_path, index=False)
                    
                    # Create plots from merged summary
                    plot_summary_results(
                        summary_file=str(merged_summary_path),
                        plot_type="linear",
                        output_dir=output_dir / "plots" / "linear"
                    )
        else:
            # Run in a single process
            result_file = simulator.run_linear_methods_comparison(
                measurements_file=measurements_file,
                num_runs=args.num_runs,
                configs=configs
            )
            
            # Find summary file
            if result_file:
                result_path = Path(result_file)
                summary_path = result_path.parent / result_file.replace("results", "summary")
                if summary_path.exists():
                    # Create plots from summary
                    plot_summary_results(
                        summary_file=str(summary_path),
                        plot_type="linear",
                        output_dir=output_dir / "plots" / "linear"
                    )
    
    elif args.mode == "stopping":
        # Run stopping criteria comparison
        configs = simulator.create_config_variations("stopping_criteria")
        
        if args.num_processes > 1:
            result_files = run_parallel_simulations(
                simulator=simulator,
                test_name="stopping",
                measurements_file=measurements_file,
                configs=configs,
                num_runs=args.num_runs,
                parallel_processes=args.num_processes
            )
            
            # Similar merging logic as for linear mode
            if result_files and len(result_files) > 1:
                summary_files = []
                for result_file in result_files:
                    if result_file:
                        result_path = Path(result_file)
                        summary_path = result_path.parent / result_file.replace("results", "summary")
                        if summary_path.exists():
                            summary_files.append(summary_path)
                
                if summary_files:
                    merged_summary = pd.concat([pd.read_csv(f) for f in summary_files])
                    merged_summary_path = output_dir / f"stopping_criteria_summary_merged.csv"
                    merged_summary.to_csv(merged_summary_path, index=False)
                    
                    plot_summary_results(
                        summary_file=str(merged_summary_path),
                        plot_type="stopping",
                        output_dir=output_dir / "plots" / "stopping"
                    )
        else:
            result_file = simulator.run_stopping_criteria_comparison(
                measurements_file=measurements_file,
                num_runs=args.num_runs,
                configs=configs
            )
            
            if result_file:
                result_path = Path(result_file)
                summary_path = result_path.parent / result_file.replace("results", "summary")
                if summary_path.exists():
                    plot_summary_results(
                        summary_file=str(summary_path),
                        plot_type="stopping",
                        output_dir=output_dir / "plots" / "stopping"
                    )
    
    elif args.mode == "nonlinear":
        # Run nonlinear methods comparison
        configs = simulator.create_config_variations("nonlinear_methods")
        
        if args.num_processes > 1:
            result_files = run_parallel_simulations(
                simulator=simulator,
                test_name="nonlinear",
                measurements_file=measurements_file,
                configs=configs,
                num_runs=args.num_runs,
                parallel_processes=args.num_processes
            )
            
            # Similar merging logic
            if result_files and len(result_files) > 1:
                summary_files = [Path(f).parent / f.replace("results", "summary") 
                               for f in result_files if f]
                summary_files = [f for f in summary_files if f.exists()]
                
                if summary_files:
                    merged_summary = pd.concat([pd.read_csv(f) for f in summary_files])
                    merged_summary_path = output_dir / f"nonlinear_methods_summary_merged.csv"
                    merged_summary.to_csv(merged_summary_path, index=False)
                    
                    plot_summary_results(
                        summary_file=str(merged_summary_path),
                        plot_type="nonlinear",
                        output_dir=output_dir / "plots" / "nonlinear"
                    )
        else:
            result_file = simulator.run_nonlinear_methods_comparison(
                measurements_file=measurements_file,
                num_runs=args.num_runs,
                configs=configs
            )
            
            if result_file:
                result_path = Path(result_file)
                summary_path = result_path.parent / result_file.replace("results", "summary")
                if summary_path.exists():
                    plot_summary_results(
                        summary_file=str(summary_path),
                        plot_type="nonlinear",
                        output_dir=output_dir / "plots" / "nonlinear"
                    )
    
    elif args.mode == "trajectory":
        # Run trajectory methods comparison
        configs = simulator.create_config_variations("trajectory_methods")
        
        if args.num_processes > 1:
            result_files = run_parallel_simulations(
                simulator=simulator,
                test_name="trajectory",
                measurements_file=measurements_file,
                configs=configs,
                num_runs=args.num_runs,
                parallel_processes=args.num_processes
            )
            
            # Similar merging logic
            if result_files and len(result_files) > 1:
                summary_files = [Path(f).parent / f.replace("results", "summary") 
                               for f in result_files if f]
                summary_files = [f for f in summary_files if f.exists()]
                
                if summary_files:
                    merged_summary = pd.concat([pd.read_csv(f) for f in summary_files])
                    merged_summary_path = output_dir / f"trajectory_methods_summary_merged.csv"
                    merged_summary.to_csv(merged_summary_path, index=False)
                    
                    plot_summary_results(
                        summary_file=str(merged_summary_path),
                        plot_type="trajectory",
                        output_dir=output_dir / "plots" / "trajectory"
                    )
        else:
            result_file = simulator.run_trajectory_methods_comparison(
                measurements_file=measurements_file,
                num_runs=args.num_runs,
                configs=configs
            )
            
            if result_file:
                result_path = Path(result_file)
                summary_path = result_path.parent / result_file.replace("results", "summary")
                if summary_path.exists():
                    plot_summary_results(
                        summary_file=str(summary_path),
                        plot_type="trajectory",
                        output_dir=output_dir / "plots" / "trajectory"
                    )
    
    logger.info("All simulations completed")

if __name__ == "__main__":
    main()