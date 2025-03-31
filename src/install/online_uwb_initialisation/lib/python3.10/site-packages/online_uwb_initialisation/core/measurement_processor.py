import numpy as np
from typing import List, Dict, Tuple, Optional, Union, Any, Protocol
import logging
from dataclasses import dataclass, field

from online_uwb_initialisation.core.anchor_data import AnchorData, AnchorStatus

# Set up logging
logger = logging.getLogger(__name__)


@dataclass
class MeasurementProcessorConfig:
    """Configuration for the MeasurementProcessor class."""
    distance_to_anchor_ratio_threshold: float = 0.03
    """Tangent ratio between consecutive measurements; smaller means more measurements."""
    
    number_of_redundant_measurements: int = 1
    """Number of measurements to take at the same place, ignoring the angle condition."""
    
    distance_rejection_threshold: float = 20.0
    """Maximum distance to the anchor to accept the measurement."""
    
    outlier_z_score_threshold: float = 2.0
    """Z-score threshold for outlier detection."""
    
    outlier_count_threshold: int = 3
    """Number of consecutive outliers to remove a measurement when using the counter method."""
    
    outlier_removal_method: str = "None"
    """Method to use for outlier removal: "None", "counter", or "immediate"."""


class MeasurementProcessor:
    """Handles measurement collection, filtering, and outlier detection for UWB anchors.
    
    This class encapsulates the logic for processing measurements, deciding whether to keep
    or reject them, and handling outlier detection and removal.
    """
    
    def __init__(self, config: Optional[MeasurementProcessorConfig] = None):
        """Initialize the MeasurementProcessor with configuration parameters.
        
        Args:
            config: Configuration parameters. If None, default values will be used.
        """
        self.config = config or MeasurementProcessorConfig()
        logger.debug(f"Initialized MeasurementProcessor with config: {self.config}")
    
    def process_measurement(self, anchor_data: AnchorData, drone_position: Tuple[float, float, float], 
                           distance: float) -> bool:
        """Process a new measurement and decide whether to add it to the anchor data.
        
        This method applies filtering rules to determine if a measurement should be 
        accepted for the anchor initialization process.
        
        Args:
            anchor_data: The data for the anchor being measured
            drone_position: The drone position when taking the measurement [x, y, z]
            distance: The measured distance to the anchor
            
        Returns:
            True if the measurement was added, False if it was rejected
        """
        # Reject measurements that are too far away
        if distance > self.config.distance_rejection_threshold:
            logger.debug(f"Rejected measurement for anchor {anchor_data.anchor_id}: distance {distance} exceeds threshold")
            return False
        
        # If we have no measurements yet, or if we're collecting redundant measurements
        # at the same position, add the measurement
        if (anchor_data.num_measurements_pre_estimation % self.config.number_of_redundant_measurements != 0 or 
            anchor_data.num_measurements_pre_estimation == 0):
            anchor_data.add_pre_estimate_measurement(drone_position, distance)
            logger.debug(f"Added measurement for anchor {anchor_data.anchor_id}: redundant or first measurement")
            return True
        
        # Check if the drone has moved significantly relative to the anchor distance
        last_position = np.array(anchor_data.positions_pre_rough_estimate[-1])
        current_position = np.array(drone_position)
        
        # Calculate movement as a ratio relative to distance to anchor
        movement_ratio = np.linalg.norm(current_position - last_position) / distance
        
        if movement_ratio > self.config.distance_to_anchor_ratio_threshold:
            anchor_data.add_pre_estimate_measurement(drone_position, distance)
            logger.debug(f"Added measurement for anchor {anchor_data.anchor_id}: sufficient movement ratio {movement_ratio:.4f}")
            return True
        else:
            logger.debug(f"Rejected measurement for anchor {anchor_data.anchor_id}: insufficient movement ratio {movement_ratio:.4f}")
            return False
    
    def process_measurement_optimal_trajectory(self, anchor_data: AnchorData, 
                                              drone_position: Tuple[float, float, float],
                                              distance: float) -> bool:
        """Process a measurement during the optimal trajectory phase.
        
        The rules are similar to regular measurement processing but stores in
        the post-estimate measurement collections.
        
        Args:
            anchor_data: The data for the anchor being measured
            drone_position: The drone position when taking the measurement [x, y, z]
            distance: The measured distance to the anchor
            
        Returns:
            True if the measurement was added, False if it was rejected
        """
        # Reject measurements that are too far away
        if distance > self.config.distance_rejection_threshold:
            logger.debug(f"Rejected optimal trajectory measurement for anchor {anchor_data.anchor_id}: distance {distance} exceeds threshold")
            return False
        
        # If collecting redundant measurements at the same position, add the measurement
        if anchor_data.num_measurements_post_estimation % self.config.number_of_redundant_measurements != 0:
            anchor_data.add_post_estimate_measurement(drone_position, distance)
            logger.debug(f"Added optimal trajectory measurement for anchor {anchor_data.anchor_id}: redundant measurement")
            return True
        
        # For first post-estimate measurement, compare with last pre-estimate position
        if anchor_data.num_measurements_post_estimation == 0:
            if anchor_data.num_measurements_pre_estimation > 0:
                last_position = np.array(anchor_data.positions_pre_rough_estimate[-1])
                current_position = np.array(drone_position)
                movement_ratio = np.linalg.norm(current_position - last_position) / distance
                
                if movement_ratio > self.config.distance_to_anchor_ratio_threshold:
                    anchor_data.add_post_estimate_measurement(drone_position, distance)
                    logger.debug(f"Added first optimal trajectory measurement for anchor {anchor_data.anchor_id}")
                    return True
                else:
                    logger.debug(f"Rejected first optimal trajectory measurement for anchor {anchor_data.anchor_id}: insufficient movement")
                    return False
            else:
                # No pre-estimate measurements, accept this one
                anchor_data.add_post_estimate_measurement(drone_position, distance)
                logger.debug(f"Added first optimal trajectory measurement for anchor {anchor_data.anchor_id}: no pre-estimate measurements")
                return True
        
        # Check if the drone has moved significantly compared to the last post-estimate measurement
        last_position = np.array(anchor_data.positions_post_rough_estimate[-1])
        current_position = np.array(drone_position)
        movement_ratio = np.linalg.norm(current_position - last_position) / distance
        
        if movement_ratio > self.config.distance_to_anchor_ratio_threshold:
            anchor_data.add_post_estimate_measurement(drone_position, distance)
            logger.debug(f"Added optimal trajectory measurement for anchor {anchor_data.anchor_id}: sufficient movement")
            return True
        else:
            logger.debug(f"Rejected optimal trajectory measurement for anchor {anchor_data.anchor_id}: insufficient movement")
            return False
    
    def compute_z_score(self, residuals: np.ndarray) -> np.ndarray:
        """Compute the z-score of the residuals.
        
        Args:
            residuals: Array of residuals from the estimation
            
        Returns:
            Array of z-scores for each residual
        """
        mean_residuals = np.mean(residuals)
        std_residuals = np.std(residuals)
        
        # Avoid division by zero
        if std_residuals == 0:
            return np.zeros_like(residuals)
            
        return (residuals - mean_residuals) / std_residuals
    
    def compute_mad(self, residuals: np.ndarray) -> float:
        """Compute the Median Absolute Deviation (MAD) of the residuals.
        
        Args:
            residuals: Array of residuals from the estimation
            
        Returns:
            The MAD value
        """
        median = np.median(residuals)
        return np.median(np.abs(residuals - median))
    
    def identify_outliers(self, residuals: np.ndarray) -> np.ndarray:
        """Identify outliers in the residuals using the z-score method.
        
        Args:
            residuals: Array of residuals from the estimation
            
        Returns:
            Array of indices of outliers in the residuals
        """
        z_scores = self.compute_z_score(residuals)
        outliers = np.where(np.abs(z_scores) > self.config.outlier_z_score_threshold)[0]
        
        if len(outliers) > 0:
            logger.debug(f"Identified {len(outliers)} outliers with z-scores > {self.config.outlier_z_score_threshold}")
            
        return outliers
    
    def filter_outliers(self, anchor_data: AnchorData, residuals: np.ndarray) -> bool:
        """Filter outliers from the measurements using the configured method.
        
        Args:
            anchor_data: The data for the anchor being processed
            residuals: Array of residuals from the estimation
            
        Returns:
            True if outliers were found and removed, False otherwise
        """
        # If no outlier removal is configured, return False
        if self.config.outlier_removal_method == "NONE":
            return False
            
        outliers = self.identify_outliers(residuals)
        
        if self.config.outlier_removal_method == "IMMEDIATE":
            # Immediately remove outliers from the measurements
            if len(outliers) > 0:
                # Convert lists to numpy arrays for easier removal
                distances = np.array(anchor_data.distances_pre_rough_estimate)
                positions = np.array(anchor_data.positions_pre_rough_estimate, dtype=object)
                
                # Remove outliers
                distances = np.delete(distances, outliers)
                positions = np.delete(positions, outliers, axis=0)
                
                # Update anchor_data
                anchor_data.distances_pre_rough_estimate = distances.tolist()
                anchor_data.positions_pre_rough_estimate = positions.tolist()
                
                # Also update weights if they exist
                if len(anchor_data.linear_ls_weights) > 0 and len(anchor_data.linear_ls_weights[-1]) > 0:
                    weights = np.array(anchor_data.linear_ls_weights[-1])
                    weights = np.delete(weights, outliers)
                    anchor_data.linear_ls_weights[-1] = weights.tolist()
                
                logger.info(f"Removed {len(outliers)} outliers from anchor {anchor_data.anchor_id} using immediate method")
                return True
            
            return False
            
        elif self.config.outlier_removal_method == "COUNTER":
            # Track outliers and remove after consecutive detections
            number_of_measurements = anchor_data.num_measurements_pre_estimation
            outlier_counter_length = len(anchor_data.linear_ls_outlier_counter)
            
            # Extend outlier counter if needed
            if outlier_counter_length < number_of_measurements:
                anchor_data.linear_ls_outlier_counter.extend([0] * (number_of_measurements - outlier_counter_length))
            
            # Create mask for outliers
            mask = np.zeros(number_of_measurements)
            mask[outliers] = 1
            
            # Increment counters for all measurements
            outlier_counter = np.array(anchor_data.linear_ls_outlier_counter)
            outlier_counter = outlier_counter * mask + mask  # Reset non-outliers to 0 and increment outliers
            
            # Update counter in anchor_data
            anchor_data.linear_ls_outlier_counter = outlier_counter.tolist()
            
            # Check if any counters exceed threshold
            to_remove = np.where(outlier_counter >= self.config.outlier_count_threshold)[0]
            
            if len(to_remove) > 0:
                # Remove from highest index to lowest to avoid index shifting
                to_remove = sorted(to_remove, reverse=True)
                
                for idx in to_remove:
                    del anchor_data.distances_pre_rough_estimate[idx]
                    del anchor_data.positions_pre_rough_estimate[idx]
                    
                    if (len(anchor_data.linear_ls_weights) > 0 and 
                        len(anchor_data.linear_ls_weights[-1]) > idx):
                        del anchor_data.linear_ls_weights[-1][idx]
                
                logger.info(f"Removed {len(to_remove)} outliers from anchor {anchor_data.anchor_id} using counter method")
                return True
            
            return False
            
        else:
            logger.warning(f"Unknown outlier removal method: {self.config.outlier_removal_method}")
            return False