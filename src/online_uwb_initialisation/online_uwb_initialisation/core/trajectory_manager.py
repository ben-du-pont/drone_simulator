import numpy as np
from typing import List, Dict, Tuple, Optional, Union, Any, Set
import logging
from copy import deepcopy
from enum import Enum

from online_uwb_initialisation.core.trajectory_optimisation import TrajectoryOptimizer, ReturnTrajectoryMethod
from online_uwb_initialisation.core.config_params import TrajectoryOptimizationMethod, LinkMethod
from online_uwb_initialisation.core.anchor_data import AnchorData, AnchorStatus

# Set up logging
logger = logging.getLogger(__name__)


class TrajectoryState(Enum):
    """Enumeration of trajectory states for the drone."""
    OPEN_TO_MEASUREMENTS = "open_to_measurements"
    ON_OPTIMAL_TRAJECTORY = "on_optimal_trajectory"


class TrajectoryManager:
    """Manages trajectory optimization and waypoint planning for UWB anchor initialization.
    
    This class handles the planning of optimal trajectories for UWB anchor initialization,
    managing the transition between normal mission waypoints and optimized trajectories,
    and selecting which anchor to optimize next based on current drone position.
    """
    
    def __init__(self, 
                trajectory_optimizer: Optional[TrajectoryOptimizer] = None,
                optimization_method: Union[str, TrajectoryOptimizationMethod] = "GDOP",
                link_method: Union[str, LinkMethod] = "strict_return"):
        """Initialize the TrajectoryManager.
        
        Args:
            trajectory_optimizer: Optional trajectory optimizer instance
            optimization_method: Method to use for trajectory optimization
            link_method: Method to use for linking trajectory segments
        """
        # Convert string to enum if needed
        if isinstance(optimization_method, str):
            try:
                optimization_method = TrajectoryOptimizationMethod.from_string(optimization_method)
            except (ValueError, AttributeError):
                logger.warning(f"Invalid optimization method: {optimization_method}, using GDOP")
                optimization_method = TrajectoryOptimizationMethod.GDOP
                
        if isinstance(link_method, str):
            try:
                link_method = LinkMethod.from_string(link_method)
            except (ValueError, AttributeError):
                logger.warning(f"Invalid link method: {link_method}, using STRICT_RETURN")
                link_method = LinkMethod.STRICT_RETURN
            
        self.trajectory_optimizer = trajectory_optimizer or TrajectoryOptimizer(metric_type=optimization_method.name)
        self.optimization_method = optimization_method
        self.link_method = link_method
        
        # Waypoint tracking
        self.passed_waypoints: List[np.ndarray] = []
        self.remaining_waypoints: List[np.ndarray] = []
        
        # Current trajectory segments
        self.current_optimal_waypoints: List[np.ndarray] = []
        self.current_link_waypoints: List[np.ndarray] = []
        
        # Optimization queue for anchors
        self.anchor_to_optimise_queue: Dict[str, np.ndarray] = {}
        
        # Trajectory state
        self.state = TrajectoryState.OPEN_TO_MEASUREMENTS
    
    def set_initial_mission(self, waypoints: List[Union[Tuple[float, float, float], np.ndarray]]) -> None:
        """Set the initial mission waypoints.
        
        Args:
            waypoints: List of mission waypoints [x, y, z]
        """
        self.remaining_waypoints = [np.array(wp, dtype=float) for wp in waypoints]
        
        if self.remaining_waypoints:
            # Set the first waypoint as the first passed waypoint
            self.passed_waypoints = [self.remaining_waypoints[0]]
            # Remove it from remaining waypoints to avoid duplication
            self.remaining_waypoints = self.remaining_waypoints[1:]
            
        logger.info(f"Set initial mission with {len(waypoints)} waypoints")
    
    def update_passed_waypoint(self, current_position: np.ndarray) -> None:
        """Update the list of passed waypoints with the current position.
        
        Args:
            current_position: Current position of the drone [x, y, z]
        """
        self.passed_waypoints.append(np.array(current_position, dtype=float))
    
    def update_optimizer_method(self, method: Union[str, TrajectoryOptimizationMethod]) -> None:
        """Update the trajectory optimization method.
        
        Args:
            method: Trajectory optimization method
        """
        if isinstance(method, str):
            try:
                method = TrajectoryOptimizationMethod.from_string(method)
            except (ValueError, AttributeError):
                logger.warning(f"Invalid optimization method: {method}, using {self.optimization_method.name}")
                return
        
        self.optimization_method = method
        self.trajectory_optimizer.method = method.name
        logger.info(f"Updated optimization method to {method.name}")
    
    def update_link_method(self, method: Union[str, LinkMethod]) -> None:
        """Update the trajectory link method.
        
        Args:
            method: Trajectory link method
        """
        if isinstance(method, str):
            try:
                method = LinkMethod.from_string(method)
            except (ValueError, AttributeError):
                logger.warning(f"Invalid link method: {method}, using {self.link_method.name}")
                return
        
        self.link_method = method
        logger.info(f"Updated link method to {method.name}")
    
    def add_anchor_to_optimization_queue(self, anchor_id: str, anchor_position: np.ndarray) -> None:
        """Add an anchor to the optimization queue.
        
        Args:
            anchor_id: ID of the anchor
            anchor_position: Estimated position of the anchor [x, y, z]
        """
        self.anchor_to_optimise_queue[anchor_id] = np.array(anchor_position, dtype=float)
        logger.info(f"Added anchor {anchor_id} to optimization queue at position {anchor_position}")
    
    def remove_anchor_from_optimization_queue(self, anchor_id: str) -> bool:
        """Remove an anchor from the optimization queue.
        
        Args:
            anchor_id: ID of the anchor
            
        Returns:
            True if the anchor was removed, False if it wasn't in the queue
        """
        if anchor_id in self.anchor_to_optimise_queue:
            del self.anchor_to_optimise_queue[anchor_id]
            logger.info(f"Removed anchor {anchor_id} from optimization queue")
            return True
        return False
    
    def find_closest_anchor_in_queue(self, current_position: np.ndarray) -> Optional[str]:
        """Find the closest anchor in the optimization queue to the current position.
        
        Args:
            current_position: Current position of the drone [x, y, z]
            
        Returns:
            ID of the closest anchor, or None if the queue is empty or it's closer to return to link waypoint
        """
        if not self.anchor_to_optimise_queue:
            logger.debug("No anchors in optimization queue")
            return None
        
        closest_anchor_id = None
        min_distance = float('inf')
        
        # Find closest anchor
        for anchor_id, anchor_position in self.anchor_to_optimise_queue.items():
            distance = np.linalg.norm(current_position - anchor_position)
            if distance < min_distance:
                min_distance = distance
                closest_anchor_id = anchor_id
        
        # Check if it's closer to return to the link waypoint
        if self.current_link_waypoints and len(self.current_link_waypoints) > 0:
            link_distance = np.linalg.norm(current_position - self.current_link_waypoints[-1])
            if link_distance < min_distance:
                logger.info(f"Closer to return to link waypoint ({link_distance:.2f}m) than optimize anchor ({min_distance:.2f}m)")
                return None
        
        logger.info(f"Closest anchor in queue is {closest_anchor_id} at distance {min_distance:.2f}m")
        return closest_anchor_id
    
    def optimize_trajectory(self, 
                          anchor_position: np.ndarray,
                          current_position: np.ndarray,
                          previous_measurements: List[np.ndarray]) -> List[np.ndarray]:
        """Optimize a trajectory for an anchor.
        
        Args:
            anchor_position: Estimated position of the anchor [x, y, z]
            current_position: Current position of the drone [x, y, z]
            previous_measurements: Previous measurement positions
            
        Returns:
            List of optimized waypoints
        """
        # Set the optimizer's method
        self.trajectory_optimizer.method = self.optimization_method.name
        
        # Determine starting point for optimization
        optimal_trajectory_starting_point = current_position
        if self.current_link_waypoints and len(self.current_link_waypoints) > 0:
            # Check if link waypoint is a better starting point than current position
            current_distance = np.linalg.norm(current_position - anchor_position)
            link_distance = np.linalg.norm(self.current_link_waypoints[-1] - anchor_position)
            
            if link_distance < current_distance:
                logger.info(f"Using link waypoint as starting point for optimization")
                optimal_trajectory_starting_point = self.current_link_waypoints[-1]
            else:
                logger.info(f"Using current position as starting point for optimization")
        
        # Convert data to numpy arrays
        starting_point = np.array(optimal_trajectory_starting_point)
        anchor_pos = np.array(anchor_position)
        measurement_pos = np.array(previous_measurements)
        
        # Get optimization result
        optimization_result = self.trajectory_optimizer.optimize_trajectory(
            starting_point, 
            anchor_pos, 
            measurement_pos
        )
        
        optimal_waypoints = optimization_result.optimal_waypoints
        
        if len(optimal_waypoints) == 0:
            logger.warning("Optimization produced no waypoints")
            return []
        
        logger.info(f"Generated {len(optimal_waypoints)} optimal waypoints")
        return optimal_waypoints
    
    def compute_full_trajectory(self, 
                               optimal_waypoints: List[np.ndarray],
                               return_waypoints: Optional[List[np.ndarray]] = None) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """Compute the full trajectory by combining optimal and return segments.
        
        Args:
            optimal_waypoints: Optimized waypoints for anchor
            return_waypoints: Optional return waypoints
            
        Returns:
            Tuple of (full trajectory waypoints, link waypoints)
        """
        if not optimal_waypoints:
            logger.warning("No optimal waypoints provided")
            return self.remaining_waypoints.copy(), []
        
        if not self.passed_waypoints:
            logger.warning("No passed waypoints available")
            last_passed = np.zeros(3)
        else:
            last_passed = self.passed_waypoints[-1]
        
        # Convert ReturnTrajectoryMethod enum to string
        link_method_str = self.link_method.name.lower()
        if link_method_str == "strict_return":
            link_method_str = "strict_return"
        elif link_method_str == "return_to_initial":
            link_method_str = "return_to_initial"
        elif link_method_str == "straight_to_waypoint":
            link_method_str = "straight_to_wapoint"  # Match original spelling
        elif link_method_str == "return_to_closest":
            link_method_str = "return_to_closest"
        elif link_method_str == "hybrid_return":
            link_method_str = "hybrid_return"
        elif link_method_str == "optimal":
            link_method_str = "optimal"
        
        # Compute new mission waypoints
        full_waypoints, final_optimal_waypoints, link_waypoints, remaining = self.trajectory_optimizer.compute_new_mission_waypoints(
            last_passed,
            self.remaining_waypoints,
            optimal_waypoints,
            link_method_str,
            return_waypoints
        )
        
        # Update internal state
        self.current_optimal_waypoints = list(final_optimal_waypoints)
        self.current_link_waypoints = list(link_waypoints)
        
        logger.info(f"Computed full trajectory with {len(full_waypoints)} waypoints")
        logger.info(f"Trajectory includes {len(final_optimal_waypoints)} optimal waypoints and {len(link_waypoints)} link waypoints")
        
        return full_waypoints, link_waypoints
    
    def generate_optimal_trajectory(self, 
                                  anchor_id: str,
                                  anchor_position: np.ndarray,
                                  current_position: np.ndarray,
                                  previous_measurements: List[np.ndarray]) -> List[np.ndarray]:
        """Generate an optimal trajectory for an anchor.
        
        Args:
            anchor_id: ID of the anchor
            anchor_position: Estimated position of the anchor [x, y, z]
            current_position: Current position of the drone [x, y, z]
            previous_measurements: Previous measurement positions
            
        Returns:
            Complete list of waypoints for the trajectory
        """
        # Optimize trajectory
        optimal_waypoints = self.optimize_trajectory(
            anchor_position,
            current_position,
            previous_measurements
        )
        
        if not optimal_waypoints:
            logger.warning(f"Failed to generate optimal trajectory for anchor {anchor_id}")
            return self.remaining_waypoints.copy()
        
        # Generate return waypoints if using optimal link method
        return_waypoints = None
        if self.link_method == LinkMethod.OPTIMAL and self.remaining_waypoints:
            logger.info("Generating optimal return waypoints")
            try:
                # Try to optimize return path (this matches original code behavior)
                optimal_waypoints, return_waypoints = self.trajectory_optimizer.optimize_return_waypoints_incrementally_spherical(
                    optimal_waypoints[-1], 
                    np.concatenate([anchor_position, [0, 1]]),  # Add dummy bias values to match expected format
                    np.eye(3),  # Dummy covariance
                    previous_measurements,
                    self.remaining_waypoints[0],
                    radius_of_search=0.2,
                    max_waypoints=20,
                    marginal_gain_threshold=0.01,
                    lambda_penalty=1
                )
            except Exception as e:
                logger.error(f"Error generating return waypoints: {e}")
                return_waypoints = None
        
        # Compute full trajectory
        full_waypoints, _ = self.compute_full_trajectory(optimal_waypoints, return_waypoints)
        
        # Update state
        self.state = TrajectoryState.ON_OPTIMAL_TRAJECTORY
        
        # Remove anchor from queue
        self.remove_anchor_from_optimization_queue(anchor_id)
        
        return full_waypoints
    
    def check_trajectory_completion(self, current_position: np.ndarray) -> bool:
        """Check if the current optimal trajectory is complete.
        
        Args:
            current_position: Current position of the drone [x, y, z]
            
        Returns:
            True if the trajectory is complete, False otherwise
        """
        if not self.current_optimal_waypoints:
            return True
            
        # Check if we're close to the last optimal waypoint and there are no more
        if (len(self.current_optimal_waypoints) < 2 and 
            np.linalg.norm(np.array(self.passed_waypoints[-1]) - np.array(self.current_optimal_waypoints[-1])) < 0.01):
            
            logger.info("Optimal trajectory completed")
            self.state = TrajectoryState.OPEN_TO_MEASUREMENTS
            self.current_optimal_waypoints = []
            return True
            
        # We're still on the optimal trajectory
        return False
    
    def clear_trajectory(self) -> None:
        """Clear the current trajectory."""
        self.current_optimal_waypoints = []
        self.current_link_waypoints = []
        self.state = TrajectoryState.OPEN_TO_MEASUREMENTS
        logger.info("Cleared trajectory")