"""
Drone Simulation ROS Node

This module provides a ROS2 node that runs the drone simulation and publishes
relevant information for visualization and analysis. It also subscribes to
UWB anchor initialization estimates and calculates estimation errors.

The node publishes:
- Drone position updates
- Trajectory visualization
- Drone trail visualization
- Waypoints status
- Anchor error metrics

It subscribes to:
- UWB anchor initialization estimates
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped, Quaternion, PoseStamped
from nav_msgs.msg import Path
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA, Float64MultiArray
from builtin_interfaces.msg import Time

import tf2_ros
import threading
import numpy as np
from typing import Dict, List, Tuple, Optional, Any, Union
import time
from enum import Enum, auto
import json

# Import from the improved simulation modules
from drone_uwb_simulator.drone_simulator import (
    DroneSimulation, SimulationConfig, WaypointMode, 
    AnchorPlacementStrategy, SimulationResult, Trajectory, Waypoint
)
from drone_uwb_simulator.UWB_protocol import AnchorID, Position3D

# Custom messages
from sim_interfaces.msg import (
    DronePosition, AnchorEstimate, AnchorError, 
    AnchorErrors, WaypointList, OptimizedTrajectory, AnchorInfo, WaypointLists
)


class EstimationType(Enum):
    """Enumeration of UWB anchor estimation types."""
    LINEAR = auto()
    NON_LINEAR = auto()
    FINAL = auto()


class DroneSimulationNode(Node):
    """
    ROS2 Node for drone simulation with UWB-based localization.
    
    This node manages:
    - Drone position updates and trajectory visualization
    - UWB anchor information and visualization
    - Subscription to anchor initialization estimates
    - Calculation and publishing of estimation errors
    """
    
    def __init__(self):
        """Initialize the drone simulation node with publishers and subscribers."""
        super().__init__('drone_simulation')
        
        # Declare node parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('namespace', 'drone_sim'),
                ('dt', 0.1),
                ('drone_speed', 3.0),
                ('num_waypoints', 7),
                ('wait_time', 2.0),
                ('bounds', [10.0, 10.0, 10.0]),
                ('random_seed', 42),
                ('mesh_resource', 'package://drone_uwb_simulator/drone_mesh.glb'),
                ('frame_id', 'world'),
                ('waypoint_mode', 'OPPOSITE_EDGES'),
                ('anchor_strategy', 'FIXED'),
                ('interpolation_method', 'spline'),
                ('position_history_limit', 1000),
                ('publish_transforms', True)
            ]
        )
        
        # Get parameters
        self.ns = self.get_parameter('namespace').value
        self.frame_id = self.get_parameter('frame_id').value
        self.dt = self.get_parameter('dt').value
        self.drone_speed = self.get_parameter('drone_speed').value
        self.wait_time = self.get_parameter('wait_time').value
        self.num_waypoints = self.get_parameter('num_waypoints').value
        self.bounds = self.get_parameter('bounds').value
        self.random_seed = self.get_parameter('random_seed').value

        self.mesh_resource = self.get_parameter('mesh_resource').value
        self.position_history_limit = self.get_parameter('position_history_limit').value
        self.publish_transforms = self.get_parameter('publish_transforms').value
        
        # Set up simulation parameters
        waypoint_mode_str = self.get_parameter('waypoint_mode').value
        self.waypoint_mode = getattr(WaypointMode, waypoint_mode_str)
        
        anchor_strategy_str = self.get_parameter('anchor_strategy').value
        self.anchor_strategy = getattr(AnchorPlacementStrategy, anchor_strategy_str)
        
        self.interpolation_method = self.get_parameter('interpolation_method').value
        
        # Simulation state flags
        self.simulation_reset = False
        self.simulation_paused = False
        
        # Initialize publishers
        self._init_publishers()
        
        # Initialize subscribers
        self._init_subscribers()
        
        # Create the drone simulation
        self._init_simulation()
        
        # Storage for anchor estimation errors
        self.anchor_estimates = {}
        
        # Log initialization
        self.get_logger().info('Drone simulation node initialized')
    
    def _init_publishers(self):
        """Initialize all publishers."""
        # Main publishers
        self.drone_position_pub = self.create_publisher(
            DronePosition, f'{self.ns}/drone_position', 10
        )
        
        self.trajectory_pub = self.create_publisher(
            Path, f'{self.ns}/drone_trajectory', 10
        )
        
        self.trail_pub = self.create_publisher(
            Path, f'{self.ns}/drone_trail', 10
        )
        
        self.drone_marker_pub = self.create_publisher(
            Marker, f'{self.ns}/drone_marker', 10
        )
        
        self.waypoints_pub = self.create_publisher(
            MarkerArray, f'{self.ns}/waypoints', 10
        )
        
        # Waypoint tracking publishers
        # New publisher for waypoint lists
        self.waypoint_lists_pub = self.create_publisher(
            WaypointLists, f'{self.ns}/waypoint_lists', 10
        )
        
        # Error publishers for each anchor estimation type
        self.linear_error_pub = self.create_publisher(
            AnchorError, f'{self.ns}/linear_estimate_error', 10
        )
        
        self.nonlinear_error_pub = self.create_publisher(
            AnchorError, f'{self.ns}/nonlinear_estimate_error', 10
        )
        
        self.final_error_pub = self.create_publisher(
            AnchorError, f'{self.ns}/final_estimate_error', 10
        )
        
        # Combined error publishers
        self.anchor_errors_pub = self.create_publisher(
            AnchorErrors, f'{self.ns}/anchor_errors', 10
        )
        
        # Add publisher for anchor information
        self.anchor_info_pub = self.create_publisher(
            AnchorInfo, f'{self.ns}/anchor_info', 10
        )

        # TF broadcaster (optional)
        if self.publish_transforms:
            self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        
        # For tracking drone history
        self.position_history = []

        
    
    def _init_subscribers(self):
        """Initialize all subscribers."""
        # Subscribe to UWB anchor initialization estimates
        self.linear_estimate_sub = self.create_subscription(
            AnchorEstimate,
            f'{self.ns}/linear_anchor_estimate',
            lambda msg: self._anchor_estimate_callback(msg, EstimationType.LINEAR),
            10
        )
        
        self.nonlinear_estimate_sub = self.create_subscription(
            AnchorEstimate,
            f'{self.ns}/nonlinear_anchor_estimate',
            lambda msg: self._anchor_estimate_callback(msg, EstimationType.NON_LINEAR),
            10
        )
        
        self.final_estimate_sub = self.create_subscription(
            AnchorEstimate,
            f'{self.ns}/final_anchor_estimate',
            lambda msg: self._anchor_estimate_callback(msg, EstimationType.FINAL),
            10
        )
        
        # Subscribe to optimized trajectory
        self.optimized_trajectory_sub = self.create_subscription(
            OptimizedTrajectory,
            f'{self.ns}/optimized_trajectory',
            self._optimized_trajectory_callback,
            10
        )
    
    def _init_simulation(self):
        """Initialize the drone simulation object."""
        # Create simulation configuration
        sim_config = SimulationConfig(
            dt=self.dt,
            drone_speed=self.drone_speed,
            num_waypoints=self.num_waypoints,
            bounds=self.bounds,
            random_seed=self.random_seed,
            wait_time=self.wait_time
        )
        
        # Create simulation instance
        self.drone_sim = DroneSimulation(sim_config)
        self.drone_sim.initialize_environment(
            waypoint_mode=self.waypoint_mode,
            anchor_strategy=self.anchor_strategy,
            interpolation_method=self.interpolation_method
        )
        
        # Store initial trajectory for reference
        self.initial_trajectory = (
            self.drone_sim.drone_trajectory.points_x.copy(),
            self.drone_sim.drone_trajectory.points_y.copy(),
            self.drone_sim.drone_trajectory.points_z.copy()
        )
        
        # Initialize ground truth anchor data
        self._init_anchor_data()
    
    def _init_anchor_data(self):
        """Initialize ground truth anchor data for error calculation."""
        self.ground_truth_anchors = {}
        
        # Process base (known) anchors
        for anchor in self.drone_sim.base_anchors:
            self.ground_truth_anchors[anchor.anchor_id] = {
                'position': anchor.position.copy(),
                'constant_bias': anchor.bias_model.constant_bias,
                'linear_bias': anchor.bias_model.linear_bias
            }
        
        # Process unknown anchors
        for anchor in self.drone_sim.unknown_anchors:
            self.ground_truth_anchors[anchor.anchor_id] = {
                'position': anchor.position.copy(),
                'constant_bias': anchor.bias_model.constant_bias,
                'linear_bias': anchor.bias_model.linear_bias
            }
    
    def _anchor_estimate_callback(self, msg: AnchorEstimate, estimate_type: EstimationType):
        """
        Process incoming anchor estimation message.
        
        Parameters:
        -----------
        msg : AnchorEstimate
            The anchor estimate message containing position and bias estimates.
        estimate_type : EstimationType
            The type of estimation (LINEAR, NON_LINEAR, FINAL).
        """
        anchor_id = msg.anchor_id
        
        # Extract position and bias from message
        position = np.array([msg.position_x, msg.position_y, msg.position_z])
        constant_bias = msg.constant_bias
        linear_bias = msg.linear_bias
        
        # Store the estimate for the specific anchor and estimation type
        if anchor_id not in self.anchor_estimates:
            self.anchor_estimates[anchor_id] = {}
        
        self.anchor_estimates[anchor_id][estimate_type] = {
            'position': position,
            'constant_bias': constant_bias,
            'linear_bias': linear_bias,
            'timestamp': self.get_clock().now()
        }
        
        # Calculate and publish error
        self._calculate_and_publish_error(anchor_id, estimate_type)
        
        self.get_logger().debug(f'Received {estimate_type.name} estimate for anchor {anchor_id}')
    
    def _calculate_and_publish_error(self, anchor_id: str, estimate_type: EstimationType):
        """
        Calculate and publish estimation error.
        
        Parameters:
        -----------
        anchor_id : str
            The ID of the anchor.
        estimate_type : EstimationType
            The type of estimation.
        """
        # Get ground truth and estimation
        if anchor_id not in self.ground_truth_anchors:
            self.get_logger().warn(f'No ground truth for anchor {anchor_id}')
            return
            
        if anchor_id not in self.anchor_estimates or estimate_type not in self.anchor_estimates[anchor_id]:
            return
            
        truth = self.ground_truth_anchors[anchor_id]
        estimate = self.anchor_estimates[anchor_id][estimate_type]
        
        # Calculate errors
        position_error = np.linalg.norm(truth['position'] - estimate['position'])
        constant_bias_error = abs(truth['constant_bias'] - estimate['constant_bias'])
        linear_bias_error = abs(truth['linear_bias'] - estimate['linear_bias'])
        
        # Create and publish error message
        error_msg = AnchorError()
        error_msg.header.stamp = self.get_clock().now().to_msg()
        error_msg.anchor_id = anchor_id
        error_msg.position_error = float(position_error)
        error_msg.constant_bias_error = float(constant_bias_error)
        error_msg.linear_bias_error = float(linear_bias_error)
        
        # Publish to the appropriate topic
        if estimate_type == EstimationType.LINEAR:
            self.linear_error_pub.publish(error_msg)
        elif estimate_type == EstimationType.NON_LINEAR:
            self.nonlinear_error_pub.publish(error_msg)
        elif estimate_type == EstimationType.FINAL:
            self.final_error_pub.publish(error_msg)
        
        # Check if we have all three error types and publish combined error message
        if (anchor_id in self.anchor_estimates and
            EstimationType.LINEAR in self.anchor_estimates[anchor_id] and
            EstimationType.NON_LINEAR in self.anchor_estimates[anchor_id] and
            EstimationType.FINAL in self.anchor_estimates[anchor_id]):
            
            # Create combined error message
            combined_error = AnchorErrors()
            combined_error.header.stamp = self.get_clock().now().to_msg()
            combined_error.anchor_id = anchor_id
            
            # Create individual error messages
            linear_error = AnchorError()
            linear_error.header.stamp = self.get_clock().now().to_msg()
            linear_error.anchor_id = anchor_id
            linear_error.position_error = float(np.linalg.norm(
                truth['position'] - self.anchor_estimates[anchor_id][EstimationType.LINEAR]['position']
            ))
            linear_error.constant_bias_error = abs(
                truth['constant_bias'] - self.anchor_estimates[anchor_id][EstimationType.LINEAR]['constant_bias']
            )
            linear_error.linear_bias_error = abs(
                truth['linear_bias'] - self.anchor_estimates[anchor_id][EstimationType.LINEAR]['linear_bias']
            )
            
            nonlinear_error = AnchorError()
            nonlinear_error.header.stamp = self.get_clock().now().to_msg()
            nonlinear_error.anchor_id = anchor_id
            nonlinear_error.position_error = float(np.linalg.norm(
                truth['position'] - self.anchor_estimates[anchor_id][EstimationType.NON_LINEAR]['position']
            ))
            nonlinear_error.constant_bias_error = abs(
                truth['constant_bias'] - self.anchor_estimates[anchor_id][EstimationType.NON_LINEAR]['constant_bias']
            )
            nonlinear_error.linear_bias_error = abs(
                truth['linear_bias'] - self.anchor_estimates[anchor_id][EstimationType.NON_LINEAR]['linear_bias']
            )
            
            final_error = AnchorError()
            final_error.header.stamp = self.get_clock().now().to_msg()
            final_error.anchor_id = anchor_id
            final_error.position_error = float(np.linalg.norm(
                truth['position'] - self.anchor_estimates[anchor_id][EstimationType.FINAL]['position']
            ))
            final_error.constant_bias_error = abs(
                truth['constant_bias'] - self.anchor_estimates[anchor_id][EstimationType.FINAL]['constant_bias']
            )
            final_error.linear_bias_error = abs(
                truth['linear_bias'] - self.anchor_estimates[anchor_id][EstimationType.FINAL]['linear_bias']
            )
            
            # Add errors to combined message
            combined_error.linear_error = linear_error
            combined_error.nonlinear_error = nonlinear_error
            combined_error.final_error = final_error
            
            # Publish combined error message
            self.anchor_errors_pub.publish(combined_error)

            
    def _optimized_trajectory_callback(self, msg: OptimizedTrajectory):
        """
        Process incoming optimized trajectory message.
        
        Parameters:
        -----------
        msg : OptimizedTrajectory
            Message containing the optimized trajectory waypoints.
        """
        self.get_logger().info(f"Received optimized trajectory with {len(msg.waypoint_x)} waypoints")
        # Extract waypoints from message
        new_waypoints = []
        for i in range(len(msg.waypoint_x)):
            new_waypoints.append(Waypoint(
                msg.waypoint_x[i],
                msg.waypoint_y[i],
                msg.waypoint_z[i]
            ))
        
        if not new_waypoints:
            self.get_logger().warn("Received empty optimized trajectory")
            return
            
        # Record the current trajectory as the initial trajectory if not already set
        if not hasattr(self, 'original_trajectory'):
            self.original_trajectory = self.initial_trajectory
        
        # Create a new trajectory using the same parameters
        new_trajectory = Trajectory(
            speed=self.drone_sim.config.drone_speed,
            dt=self.drone_sim.config.dt
        )
        
        # Add current position to beginning of waypoints
        new_waypoints.insert(0, Waypoint(
            self.drone_sim.drone_position[0],
            self.drone_sim.drone_position[1],
            self.drone_sim.drone_position[2]
        ))
        
        # Construct the new trajectory
        success = new_trajectory.construct_trajectory(new_waypoints, self.interpolation_method)
        
        if not success:
            self.get_logger().error("Failed to construct optimized trajectory")
            return
            
        # Update the drone simulation
        self.drone_sim.waypoints = new_waypoints
        self.drone_sim.drone_trajectory = new_trajectory
        
        # Store the optimized trajectory points
        self.optimized_trajectory = (
            new_trajectory.points_x.copy(),
            new_trajectory.points_y.copy(),
            new_trajectory.points_z.copy()
        )
        
        # Reset progress to continue from closest point
        current_position = self.drone_sim.drone_position
        closest_idx = new_trajectory.find_closest_point_index(current_position)
        self.drone_sim.drone_progress = max(0, closest_idx)
        
        # Clear position history for the new trajectory
        self.position_history = []
        
        self.get_logger().info(f"New waypoints: {new_waypoints}")
        self.get_logger().info(f'Applied optimized trajectory with {len(new_waypoints)} waypoints')
        
        # Trigger immediate publishing of the new trajectory
        self.publish_trajectory(*self.optimized_trajectory)

    def run_simulation(self):
        """Main simulation loop."""
        rate = self.create_rate(1.0 / self.dt)
        
        while rclpy.ok():
            if self.simulation_paused:
                rate.sleep()
                continue

            if self.simulation_reset:
                self.position_history = []
                self.simulation_reset = False

            # Determine which trajectory to publish
            if hasattr(self, 'original_trajectory'):
                # If we have an original trajectory, publish it
                self.publish_trajectory(*self.original_trajectory)
            else:
                # Otherwise publish the initial/current trajectory
                self.publish_trajectory(*self.initial_trajectory)
                
            # Publish other static visualization data
            self.publish_anchors()
            self.publish_waypoints()

            
            self.publish_anchor_info()

            # Update drone position
            new_position = self.drone_sim.update_drone_position()
            
            # Add to position history (with limit)
            self.position_history.append(new_position)
            if len(self.position_history) > self.position_history_limit:
                self.position_history = self.position_history[-self.position_history_limit:]
            
            # Get completion progress
            passed_waypoints, _ = self.drone_sim.get_remaining_waypoints()
            waypoints_achieved = len(passed_waypoints)
            
            # Check if simulation reset is needed
            if waypoints_achieved == len(self.drone_sim.waypoints):
                self.simulation_reset = True

            # Publish drone position and state
            self.publish_drone_position(new_position, waypoints_achieved)
            
            if self.publish_transforms:
                self.publish_drone_tf(new_position)
                
            self.publish_drone_marker()
            self.publish_drone_trail()
            
            # Publish waypoint lists
            self.publish_waypoint_lists()
            
            # Sleep to maintain the correct update rate
            rate.sleep()
    
    def publish_drone_position(self, position: np.ndarray, waypoints_achieved: int):
        """
        Publish current drone position.
        
        Parameters:
        -----------
        position : np.ndarray
            Current position of the drone.
        waypoints_achieved : int
            Number of waypoints achieved so far.
        """
        msg = DronePosition()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        msg.position_x = float(position[0])
        msg.position_y = float(position[1])
        msg.position_z = float(position[2])
        msg.waypoints_achieved = waypoints_achieved
        msg.total_waypoints = len(self.drone_sim.waypoints)
        
        self.drone_position_pub.publish(msg)
    
    def publish_drone_tf(self, position: np.ndarray):
        """
        Publish transform for the drone position.
        
        Parameters:
        -----------
        position : np.ndarray
            Current position of the drone.
        """
        if not self.publish_transforms:
            return
            
        tf_msg = TransformStamped()
        tf_msg.header.stamp = self.get_clock().now().to_msg()
        tf_msg.header.frame_id = self.frame_id
        tf_msg.child_frame_id = f'{self.ns}/drone'
        tf_msg.transform.translation.x = float(position[0])
        tf_msg.transform.translation.y = float(position[1])
        tf_msg.transform.translation.z = float(position[2])
        tf_msg.transform.rotation = Quaternion(w=1.0, x=0.0, y=0.0, z=0.0)
        
        self.tf_broadcaster.sendTransform(tf_msg)
    
    def publish_anchors(self):
        """Publish transforms for UWB anchors."""
        if not self.publish_transforms:
            return
            
        now = self.get_clock().now().to_msg()
        
        # Publish known anchors
        for anchor in self.drone_sim.base_anchors:
            tf_msg = TransformStamped()
            tf_msg.header.stamp = now
            tf_msg.header.frame_id = self.frame_id
            tf_msg.child_frame_id = f'{self.ns}/anchor_{anchor.anchor_id}'
            tf_msg.transform.translation.x = float(anchor.position[0])
            tf_msg.transform.translation.y = float(anchor.position[1])
            tf_msg.transform.translation.z = float(anchor.position[2])
            tf_msg.transform.rotation = Quaternion(w=1.0, x=0.0, y=0.0, z=0.0)
            
            self.tf_broadcaster.sendTransform(tf_msg)
        
        # Publish unknown anchors
        for anchor in self.drone_sim.unknown_anchors:
            tf_msg = TransformStamped()
            tf_msg.header.stamp = now
            tf_msg.header.frame_id = self.frame_id
            tf_msg.child_frame_id = f'{self.ns}/unknown_anchor_{anchor.anchor_id}'
            tf_msg.transform.translation.x = float(anchor.position[0])
            tf_msg.transform.translation.y = float(anchor.position[1])
            tf_msg.transform.translation.z = float(anchor.position[2])
            tf_msg.transform.rotation = Quaternion(w=1.0, x=0.0, y=0.0, z=0.0)
            
            self.tf_broadcaster.sendTransform(tf_msg)
    
    def publish_anchor_info(self):
        """Publish information about known and unknown anchors."""
        msg = AnchorInfo()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        
        # Populate message with all anchors
        all_anchors = self.drone_sim.base_anchors + self.drone_sim.unknown_anchors
        msg.count = len(all_anchors)
        
        for i, anchor in enumerate(all_anchors):
            msg.ids.append(anchor.anchor_id)
            msg.x.append(float(anchor.position[0]))
            msg.y.append(float(anchor.position[1]))
            msg.z.append(float(anchor.position[2]))
            msg.constant_bias.append(float(anchor.bias_model.constant_bias))
            msg.linear_bias.append(float(anchor.bias_model.linear_bias))
            
            # Set type - 0 for known (base), 1 for unknown
            is_unknown = anchor in self.drone_sim.unknown_anchors
            msg.types.append(1 if is_unknown else 0)
        
        self.anchor_info_pub.publish(msg)

    def publish_trajectory(
        self, 
        points_x: np.ndarray, 
        points_y: np.ndarray, 
        points_z: np.ndarray
    ):
        """
        Publish planned trajectory path.
        
        Parameters:
        -----------
        points_x : np.ndarray
            X-coordinates of trajectory points.
        points_y : np.ndarray
            Y-coordinates of trajectory points.
        points_z : np.ndarray
            Z-coordinates of trajectory points.
        """
        path_msg = Path()
        path_msg.header.frame_id = self.frame_id
        path_msg.header.stamp = self.get_clock().now().to_msg()
        
        # Create poses for each point in the trajectory
        for i in range(len(points_x)):
            pose_msg = PoseStamped()
            pose_msg.header.frame_id = self.frame_id
            pose_msg.header.stamp = self.get_clock().now().to_msg()
            pose_msg.pose.position.x = float(points_x[i])
            pose_msg.pose.position.y = float(points_y[i])
            pose_msg.pose.position.z = float(points_z[i])
            pose_msg.pose.orientation.w = 1.0
            
            path_msg.poses.append(pose_msg)
        
        self.trajectory_pub.publish(path_msg)
    
    def publish_drone_trail(self):
        """Publish the drone's position history as a path."""
        if not self.position_history:
            return
            
        path_msg = Path()
        path_msg.header.frame_id = self.frame_id
        path_msg.header.stamp = self.get_clock().now().to_msg()
        
        # Create poses for each point in the history
        for position in self.position_history:
            pose_msg = PoseStamped()
            pose_msg.header.frame_id = self.frame_id
            pose_msg.header.stamp = self.get_clock().now().to_msg()
            pose_msg.pose.position.x = float(position[0])
            pose_msg.pose.position.y = float(position[1])
            pose_msg.pose.position.z = float(position[2])
            pose_msg.pose.orientation.w = 1.0
            
            path_msg.poses.append(pose_msg)
        
        self.trail_pub.publish(path_msg)
    
    def publish_drone_marker(self):
        """Publish drone mesh marker."""
        marker_msg = Marker()
        marker_msg.header.frame_id = f'{self.ns}/drone' if self.publish_transforms else self.frame_id
        marker_msg.header.stamp = self.get_clock().now().to_msg()
        marker_msg.ns = f'{self.ns}'
        marker_msg.id = 0
        marker_msg.type = Marker.MESH_RESOURCE
        marker_msg.action = Marker.ADD
        
        # Position and orientation
        if not self.publish_transforms:
            # If not publishing transforms, include position in the marker
            current_pos = self.drone_sim.drone_position
            marker_msg.pose.position.x = float(current_pos[0])
            marker_msg.pose.position.y = float(current_pos[1])
            marker_msg.pose.position.z = float(current_pos[2])
        else:
            # If publishing transforms, position is relative to the drone frame
            marker_msg.pose.position.x = 0.0
            marker_msg.pose.position.y = 0.0
            marker_msg.pose.position.z = 0.0
            
        marker_msg.pose.orientation.w = 1.0
        
        # Scale and appearance
        marker_msg.scale.x = 1.0
        marker_msg.scale.y = 1.0
        marker_msg.scale.z = 1.0
        marker_msg.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
        marker_msg.mesh_resource = self.mesh_resource
        marker_msg.mesh_use_embedded_materials = True
        
        self.drone_marker_pub.publish(marker_msg)
    
    def publish_waypoints(self):
        """Publish waypoints as marker array."""
        marker_array = MarkerArray()
        now = self.get_clock().now().to_msg()
        
        # Add a marker for each waypoint
        for i, point in enumerate(self.drone_sim.waypoints):
            marker = Marker()
            marker.header.frame_id = self.frame_id
            marker.header.stamp = now
            marker.ns = f'{self.ns}/waypoints'
            marker.id = i
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            
            # Position
            marker.pose.position.x = float(point.x)
            marker.pose.position.y = float(point.y)
            marker.pose.position.z = float(point.z)
            marker.pose.orientation.w = 1.0
            
            # Size and appearance
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            
            # Color based on progress (visited waypoints are green, remaining are red)
            _, remaining = self.drone_sim.get_remaining_waypoints()
            if point in remaining:
                marker.color = ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0)  # Red
            else:
                marker.color = ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0)  # Green
            
            marker_array.markers.append(marker)
        
        self.waypoints_pub.publish(marker_array)
    
    def publish_waypoint_lists(self):
        """Publish lists of reached and remaining waypoints in a single message."""
        if not self.drone_sim.waypoints:
            return
            
        # Get remaining waypoints
        reached_waypoints, remaining_waypoints = self.drone_sim.get_remaining_waypoints()
        
        # Create combined waypoint lists message
        combined_msg = WaypointLists()  # Assuming new message type
        combined_msg.header.stamp = self.get_clock().now().to_msg()
        combined_msg.header.frame_id = self.frame_id
        
        # Fill reached waypoints
        combined_msg.reached.count = len(reached_waypoints)
        for wp in reached_waypoints:
            combined_msg.reached.x.append(float(wp.x))
            combined_msg.reached.y.append(float(wp.y))
            combined_msg.reached.z.append(float(wp.z))
        
        # Fill remaining waypoints
        combined_msg.remaining.count = len(remaining_waypoints)
        for wp in remaining_waypoints:
            combined_msg.remaining.x.append(float(wp.x))
            combined_msg.remaining.y.append(float(wp.y))
            combined_msg.remaining.z.append(float(wp.z))
        
        self.waypoint_lists_pub.publish(combined_msg)
    

    def reset_simulation(
        self, 
        waypoint_mode: Optional[WaypointMode] = None,
        anchor_strategy: Optional[AnchorPlacementStrategy] = None,
        interpolation_method: Optional[str] = None
    ):
        """
        Reset the simulation with optionally new parameters.
        
        Parameters:
        -----------
        waypoint_mode : Optional[WaypointMode]
            If provided, use this mode to generate new waypoints.
        anchor_strategy : Optional[AnchorPlacementStrategy]
            If provided, use this strategy for anchor placement.
        interpolation_method : Optional[str]
            If provided, use this method for trajectory interpolation.
        """
        if waypoint_mode is not None:
            self.waypoint_mode = waypoint_mode
        
        if anchor_strategy is not None:
            self.anchor_strategy = anchor_strategy
            
        if interpolation_method is not None:
            self.interpolation_method = interpolation_method
        
        self.drone_sim.reset_simulation(
            self.waypoint_mode,
            self.anchor_strategy,
            self.interpolation_method
        )
        
        self.position_history = []
        
        # Update initial trajectory reference
        self.initial_trajectory = (
            self.drone_sim.drone_trajectory.points_x.copy(),
            self.drone_sim.drone_trajectory.points_y.copy(),
            self.drone_sim.drone_trajectory.points_z.copy()
        )
        
        # Reset anchor data
        self._init_anchor_data()
        self.anchor_estimates = {}
        
        self.get_logger().info('Simulation reset')
    
    def pause_simulation(self):
        """Pause the simulation."""
        self.simulation_paused = True
        self.get_logger().info('Simulation paused')
    
    def resume_simulation(self):
        """Resume the simulation."""
        self.simulation_paused = False
        self.get_logger().info('Simulation resumed')


def main(args=None):
    """Entry point for the node."""
    rclpy.init(args=args)
    sim_node = DroneSimulationNode()
    
    # Create a separate thread for handling callbacks
    spin_thread = threading.Thread(target=rclpy.spin, args=(sim_node,), daemon=True)
    spin_thread.start()
    
    try:
        # Run the simulation loop
        sim_node.run_simulation()
    except KeyboardInterrupt:
        sim_node.get_logger().info('Node stopped cleanly')
    except Exception as e:
        sim_node.get_logger().error(f'Error in simulation: {str(e)}')
    finally:
        rclpy.shutdown()
        spin_thread.join(timeout=1.0)


if __name__ == '__main__':
    main()