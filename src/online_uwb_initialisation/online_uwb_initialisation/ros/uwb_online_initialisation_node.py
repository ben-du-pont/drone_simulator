#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
import tf2_ros

from geometry_msgs.msg import PoseStamped, TransformStamped, Quaternion
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Path

from drone_uwb_simulator.UWB_protocol import Anchor, BiasModel, NoiseModel

# Import the new pipeline and related classes
from online_uwb_initialisation.core.uwb_online_initialisation_pipeline import UwbInitializationPipeline
from online_uwb_initialisation.core.anchor_data import AnchorData, AnchorStatus
from online_uwb_initialisation.core.config_params import UwbInitializationConfig, TrajectoryOptimizationMethod, LinkMethod
from online_uwb_initialisation.core.trajectory_manager import TrajectoryManager, TrajectoryState

from online_uwb_initialisation.ros.uwb_config_loader import load_config_from_yaml

# Import custom messages for the simulation
from sim_interfaces.msg import (
    DronePosition, AnchorEstimate, OptimizedTrajectory, WaypointLists, AnchorInfo
)


class UwbOnlineInitialisationNode(Node):
    """ROS2 node for online initialization of UWB anchors."""

    def __init__(self):
        """Initialize the UWB Online Initialization Node."""
        super().__init__('uwb_online_initialisation_node')
        
        # Core components
        # Load configuration from YAML
        config = load_config_from_yaml(self)
        
        # Core components
        self.uwb_initializer = UwbInitializationPipeline(config)
        self.base_anchors = {}
        self.unknown_anchors = {}
        self.anchor_status_dictionary = {}
        
        # Initialize dictionaries for publishers
        self.pub_dict = {}
        self.visualization_pub_dict = {}
        
        # Keep track of published optimized trajectories
        self.published_optimized_trajectories = set()
        
        # Declare node parameters
        self._declare_parameters()
        
        # Setup publishers and subscribers
        self._setup_subscribers()
        self._setup_publishers()
        
        # Initial state
        self.initialized = False
        self.waypoints = []
        
        # Timer for initialization attempt
        self.create_timer(1.0, self._initialization_timer_callback)
        
        self.get_logger().info('UWB Online Initialization Node initialized successfully')

    def _declare_parameters(self):
        """Declare node parameters with defaults."""
        self.declare_parameter('waypoint_threshold', 0.01)  # meters
        self.declare_parameter('namespace', 'uwb_initialisation')
        self.declare_parameter('frame_id', 'world')

    def _initialization_timer_callback(self):
        """Timer callback to check if we have received initial waypoints."""
        if not self.initialized and len(self.waypoints) > 0:
            self.get_logger().info('Received initial waypoints, initializing anchor tracking')
            
            # Setup initial waypoints using new API
            self.uwb_initializer.set_initial_mission(self.waypoints)
            
            self.initialized = True
            
            # Stop the timer once initialized
            return True
        return False

    def _setup_subscribers(self):
        """Set up ROS topic subscribers."""
        # Subscribe to drone position
        self.drone_position_subscription = self.create_subscription(
            DronePosition, 
            '/drone_sim/drone_position', 
            self._drone_position_callback, 
            10
        )
        
        # Replace separate waypoint subscriptions with single subscription
        self.waypoint_lists_sub = self.create_subscription(
            WaypointLists,
            '/drone_sim/waypoint_lists',
            self._waypoint_lists_callback,
            10
        )

        # Subscribe to anchor information
        self.anchor_info_sub = self.create_subscription(
            AnchorInfo,
            '/drone_sim/anchor_info',
            self._anchor_info_callback,
            10
        )   

    
    def _setup_publishers(self):
        """Set up ROS topic publishers."""
        namespace = self.get_parameter('namespace').get_parameter_value().string_value
        
        # Anchor estimate publishers
        self.pub_dict = {
            'linear_estimate': self.create_publisher(
                AnchorEstimate,
                f'/drone_sim/linear_anchor_estimate',
                10
            ),
            'nonlinear_estimate': self.create_publisher(
                AnchorEstimate,
                f'/drone_sim/nonlinear_anchor_estimate',
                10
            ),
            'final_estimate': self.create_publisher(
                AnchorEstimate,
                f'/drone_sim/final_anchor_estimate',
                10
            ),
            'optimized_trajectory': self.create_publisher(
                OptimizedTrajectory,
                f'/drone_sim/optimized_trajectory',
                10
            )
        }
        
        # Visualization publishers
        self.visualization_pub_dict = {
            'optimised_waypoints': self.create_publisher(
                MarkerArray, 
                f'/{namespace}/optimised_waypoints', 
                10
            ),
            'anchor_markers': self.create_publisher(
                MarkerArray,
                f'/{namespace}/anchor_positions',
                10
            )
        }
        
        # TF broadcaster
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # Reset the publishers
        self.reset_publishers()

    def reset_publishers(self):
        """Reset all publishers and clear existing visualizations."""
        # Reset anchor estimate publishers
        for publisher in self.pub_dict.values():
            if publisher == self.pub_dict['optimized_trajectory']:
                publisher.publish(OptimizedTrajectory())
            else:
                publisher.publish(AnchorEstimate())
        
        # Clear visualization markers by sending DELETE action
        delete_markers = MarkerArray()
        
        # Create a deletion marker for anchor positions
        delete_marker = Marker()
        delete_marker.header.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        delete_marker.header.stamp = self.get_clock().now().to_msg()
        delete_marker.action = Marker.DELETEALL
        delete_markers.markers.append(delete_marker)
        
        # Send deletion markers to all visualization publishers
        for publisher in self.visualization_pub_dict.values():
            publisher.publish(delete_markers)
        
        # Reset tracking sets/variables
        self.published_optimized_trajectories.clear()

    def _waypoint_lists_callback(self, msg):
        """Process waypoint lists message containing both reached and remaining waypoints.
        
        Args:
            msg: WaypointLists message containing both reached and remaining waypoints
        """
        if not self.initialized:
            # Extract all waypoints for initialization
            waypoints = []
            # Add reached waypoints
            for i in range(msg.reached.count):
                waypoints.append([msg.reached.x[i], msg.reached.y[i], msg.reached.z[i]])
            # Add remaining waypoints
            for i in range(msg.remaining.count):
                waypoints.append([msg.remaining.x[i], msg.remaining.y[i], msg.remaining.z[i]])
            self.waypoints = waypoints
            return

        # Extract reached waypoints
        reached_waypoints = []
        for i in range(msg.reached.count):
            reached_waypoints.append([msg.reached.x[i], msg.reached.y[i], msg.reached.z[i]])
        
        # Extract remaining waypoints
        remaining_waypoints = []
        for i in range(msg.remaining.count):
            remaining_waypoints.append([msg.remaining.x[i], msg.remaining.y[i], msg.remaining.z[i]])

        # Update waypoints in the trajectory manager
        self.uwb_initializer.trajectory_manager.passed_waypoints = reached_waypoints
        self.uwb_initializer.trajectory_manager.remaining_waypoints = remaining_waypoints

        # Check if the last passed waypoint matches the next optimal waypoint
        if (self.uwb_initializer.trajectory_manager.current_optimal_waypoints and 
            len(self.uwb_initializer.trajectory_manager.passed_waypoints) > 0):
            if np.linalg.norm(np.array(self.uwb_initializer.trajectory_manager.passed_waypoints[-1]) - 
                            np.array(self.uwb_initializer.trajectory_manager.current_optimal_waypoints[0])) < 0.01:
                self.uwb_initializer.trajectory_manager.current_optimal_waypoints = self.uwb_initializer.trajectory_manager.current_optimal_waypoints[1:]

    def _get_anchor_range_measurement(self, drone_position, anchor_id):
        """Get range measurement from an anchor to the drone.
        
        Args:
            drone_position: 3D position of the drone as [x, y, z]
            anchor_id: ID of the anchor to measure distance from
            
        Returns:
            float: Measured distance between drone and anchor, or None if anchor unknown
        """
        if anchor_id in self.unknown_anchors:
            return self.unknown_anchors[anchor_id].measure_distance(drone_position).measured_distance
        return None

    def _drone_position_callback(self, msg):
        """Process new drone position data.
        
        Args:
            msg: DronePosition message containing current drone position
        """
        if not self.initialized:
            return
            
        drone_position = [msg.position_x, msg.position_y, msg.position_z]
        
        # Update drone position in estimation module
        self.uwb_initializer.drone_position = drone_position
        
        # Collect measurements from all unknown anchors
        for anchor_id in self.unknown_anchors:
            distance = self._get_anchor_range_measurement(drone_position, anchor_id)
            if distance is not None:
                self.uwb_initializer.measurement_callback(drone_position, distance, anchor_id)
        
        # Check for anchor status changes and publish estimates
        for anchor_id in self.unknown_anchors:
            if anchor_id in self.uwb_initializer.anchor_data:
                anchor_data = self.uwb_initializer.anchor_data[anchor_id]
                current_status = anchor_data.status.name.lower()
                
                # Check for status change
                if current_status != self.anchor_status_dictionary.get(anchor_id, "unseen"):
                    self._anchor_status_change_callback(anchor_id, current_status)
                
                # Publish anchor estimates
                self._publish_anchor_estimates(anchor_id, anchor_data)
                
                # Check if we have a new optimized trajectory and need to publish it
                is_on_optimal_trajectory = self.uwb_initializer.trajectory_manager.state == TrajectoryState.ON_OPTIMAL_TRAJECTORY
                if (is_on_optimal_trajectory and 
                    anchor_id not in self.published_optimized_trajectories and
                    len(self.uwb_initializer.trajectory_manager.current_optimal_waypoints) > 0):
                    self.get_logger().info(f"Publishing optimized trajectory for anchor {anchor_id}")
                    self._publish_optimized_trajectory(anchor_id)
                    self.published_optimized_trajectories.add(anchor_id)
        
        # Update visualizations
        self._publish_anchor_positions()
        self._publish_optimised_waypoint_markers()

    def _anchor_info_callback(self, msg):
        """Process anchor information message.
        
        Args:
            msg: AnchorInfo message containing anchor details
        """
        # Clear existing anchor dictionaries
        self.base_anchors = {}
        self.unknown_anchors = {}
        
        # Process all anchors
        for i in range(msg.count):
            anchor_id = msg.ids[i]
            position = [msg.x[i], msg.y[i], msg.z[i]]
            constant_bias = msg.constant_bias[i]
            linear_bias = msg.linear_bias[i]
            is_unknown = msg.types[i] == 1
            
            # Create bias and noise models
            bias_model = BiasModel(constant_bias, linear_bias)
            noise_model = NoiseModel(0.2)  # Default noise variance
            
            # Create anchor object
            anchor = Anchor(
                anchor_id,
                position,
                bias_model,
                noise_model
            )
            
            # Add to appropriate dictionary
            if is_unknown:
                self.unknown_anchors[anchor_id] = anchor
                # Initialize anchor status if it's a new anchor
                if anchor_id not in self.anchor_status_dictionary:
                    self.anchor_status_dictionary[anchor_id] = "unseen"
                    self.get_logger().info(f"Added unknown anchor {anchor_id} at position {position}")
            else:
                self.base_anchors[anchor_id] = anchor

    def _publish_anchor_estimates(self, anchor_id, anchor_data):
        """Publish various types of anchor estimates.
        
        Args:
            anchor_id: ID of the anchor
            anchor_data: AnchorData object with measurement and estimation data
        """
        # Publish linear estimate if available
        if len(anchor_data.estimator_rough_linear) >= 5 and any(abs(x) > 0.0 for x in anchor_data.estimator_rough_linear):
            estimate = anchor_data.estimator_rough_linear
            position = estimate[:3]
            constant_bias = estimate[3]
            linear_bias = estimate[4] if len(estimate) > 4 else 1.0
            
            self._publish_estimate(
                anchor_id, position, constant_bias, linear_bias, 
                estimate_type='linear_estimate'
            )
        
        # Publish non-linear estimate if available
        if (len(anchor_data.estimator_rough_non_linear) >= 5 and 
            (anchor_data.status == AnchorStatus.OPTIMISED_TRAJECTORY or 
             anchor_data.status == AnchorStatus.STOPPING_CRITERION_TRIGGERED)):
            estimate = anchor_data.estimator_rough_non_linear
            position = estimate[:3]
            constant_bias = estimate[3]
            linear_bias = estimate[4] if len(estimate) > 4 else 1.0
            
            self._publish_estimate(
                anchor_id, position, constant_bias, linear_bias, 
                estimate_type='nonlinear_estimate'
            )
        
        # Publish final estimate if available
        if len(anchor_data.estimator) >= 5 and anchor_data.status == AnchorStatus.INITIALISED:
            estimate = anchor_data.estimator
            position = estimate[:3]
            constant_bias = estimate[3]
            linear_bias = estimate[4] if len(estimate) > 4 else 1.0
            
            self._publish_estimate(
                anchor_id, position, constant_bias, linear_bias, 
                estimate_type='final_estimate'
            )

    def _publish_estimate(self, anchor_id, position, constant_bias, linear_bias, estimate_type):
        """Publish an anchor estimate.
        
        Args:
            anchor_id: ID of the anchor
            position: Position estimate [x, y, z]
            constant_bias: Constant bias estimate
            linear_bias: Linear bias estimate
            estimate_type: Type of estimate (key in self.pub_dict)
        """
        if estimate_type not in self.pub_dict:
            return
            
        msg = AnchorEstimate()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        msg.anchor_id = anchor_id
        msg.position_x = float(position[0])
        msg.position_y = float(position[1])
        msg.position_z = float(position[2])
        msg.constant_bias = float(constant_bias)
        msg.linear_bias = float(linear_bias)
        
        self.pub_dict[estimate_type].publish(msg)

    def _publish_optimized_trajectory(self, anchor_id):
        """Publish optimized trajectory for a specific anchor.
        
        Args:
            anchor_id: ID of the anchor that triggered the trajectory optimization
        """
        remaining_waypoints = self.uwb_initializer.trajectory_manager.remaining_waypoints
        if len(remaining_waypoints) == 0:
            return
            
        msg = OptimizedTrajectory()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        msg.anchor_id = anchor_id
        msg.waypoint_count = len(remaining_waypoints)
        
        # Extract waypoint coordinates
        for waypoint in remaining_waypoints:
            msg.waypoint_x.append(float(waypoint[0]))
            msg.waypoint_y.append(float(waypoint[1]))
            msg.waypoint_z.append(float(waypoint[2]))
        
        # Publish the optimized trajectory
        self.pub_dict['optimized_trajectory'].publish(msg)
        self.get_logger().info(f'Published optimized trajectory for anchor {anchor_id} with {msg.waypoint_count} waypoints')

    def _anchor_status_change_callback(self, anchor_id, status):
        """Handle change in anchor status.
        
        Args:
            anchor_id: ID of the anchor whose status changed
            status: New status of the anchor
        """
        old_status = self.anchor_status_dictionary.get(anchor_id, "unseen")
        self.anchor_status_dictionary[anchor_id] = status
        self.get_logger().info(f"Anchor {anchor_id} status changed from {old_status} to {status}")

    def _publish_tf_transform(self, position, frame_id):
        """Publish a TF transform for a position.
        
        Args:
            position: Position [x, y, z]
            frame_id: Frame ID for the transform
        """
        tf_msg = TransformStamped()
        tf_msg.header.stamp = self.get_clock().now().to_msg()
        tf_msg.header.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        tf_msg.child_frame_id = frame_id
        tf_msg.transform.translation.x = float(position[0])
        tf_msg.transform.translation.y = float(position[1])
        tf_msg.transform.translation.z = float(position[2])
        tf_msg.transform.rotation = Quaternion(w=1.0, x=0.0, y=0.0, z=0.0)
        self.tf_broadcaster.sendTransform(tf_msg)

    def _publish_anchor_positions(self):
        """Publish visualization markers for all anchor positions."""
        marker_array = MarkerArray()
        marker_id = 0
        frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        
        # Publish known anchors (green)
        for anchor_id, anchor in self.base_anchors.items():
            marker = self._create_anchor_marker(
                anchor.position, 
                marker_id, 
                [0.0, 1.0, 0.0],  # Green for known anchors
                f"known_{anchor_id}",
                frame_id
            )
            marker_array.markers.append(marker)
            marker_id += 1
        
        # Publish unknown anchors with different colors based on estimation status
        for anchor_id, anchor in self.unknown_anchors.items():
            # True position (yellow, slightly transparent)
            marker = self._create_anchor_marker(
                anchor.position, 
                marker_id, 
                [1.0, 1.0, 0.0, 0.4],  # Yellow, transparent
                f"true_{anchor_id}",
                frame_id
            )
            marker_array.markers.append(marker)
            marker_id += 1
            
            if anchor_id not in self.uwb_initializer.anchor_data:
                continue
                
            anchor_data = self.uwb_initializer.anchor_data[anchor_id]
            
            # Linear estimate (blue)
            if len(anchor_data.estimator_rough_linear) >= 3:
                linear_pos = anchor_data.estimator_rough_linear[:3]
                marker = self._create_anchor_marker(
                    linear_pos, 
                    marker_id, 
                    [0.0, 0.0, 1.0],  # Blue
                    f"linear_{anchor_id}",
                    frame_id
                )
                marker_array.markers.append(marker)
                marker_id += 1
                
                # Also publish as TF
                self._publish_tf_transform(linear_pos, f"anchor_{anchor_id}_linear")
            
            # Non-linear refined estimate (purple)
            if (len(anchor_data.estimator_rough_non_linear) >= 3 and 
                (anchor_data.status == AnchorStatus.OPTIMISED_TRAJECTORY or 
                 anchor_data.status == AnchorStatus.INITIALISED or
                 anchor_data.status == AnchorStatus.STOPPING_CRITERION_TRIGGERED)):
                nonlinear_pos = anchor_data.estimator_rough_non_linear[:3]
                marker = self._create_anchor_marker(
                    nonlinear_pos, 
                    marker_id, 
                    [0.8, 0.0, 0.8],  # Purple
                    f"nonlinear_{anchor_id}",
                    frame_id
                )
                marker_array.markers.append(marker)
                marker_id += 1
                
                # Also publish as TF
                self._publish_tf_transform(nonlinear_pos, f"anchor_{anchor_id}_nonlinear")
            
            # Final estimate (red)
            if len(anchor_data.estimator) >= 3 and anchor_data.status == AnchorStatus.INITIALISED:
                final_pos = anchor_data.estimator[:3]
                marker = self._create_anchor_marker(
                    final_pos, 
                    marker_id, 
                    [1.0, 0.0, 0.0],  # Red
                    f"final_{anchor_id}",
                    frame_id
                )
                marker_array.markers.append(marker)
                marker_id += 1
                
                # Also publish as TF
                self._publish_tf_transform(final_pos, f"anchor_{anchor_id}_final")
        
        # Publish all markers
        self.visualization_pub_dict['anchor_markers'].publish(marker_array)

    def _create_anchor_marker(self, position, marker_id, color, ns="anchor", frame_id="world"):
        """Create a marker for an anchor.
        
        Args:
            position: Position [x, y, z]
            marker_id: Unique ID for the marker
            color: RGBA color [r, g, b, a]
            ns: Namespace for the marker
            frame_id: Frame ID for the marker
            
        Returns:
            Marker: Configured marker for the anchor
        """
        marker = Marker()
        marker.header.frame_id = frame_id
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = ns
        marker.id = marker_id
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        
        marker.pose.position.x = float(position[0])
        marker.pose.position.y = float(position[1])
        marker.pose.position.z = float(position[2])
        marker.pose.orientation.w = 1.0
        
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        
        # Set color with appropriate alpha
        marker.color.r = color[0]
        marker.color.g = color[1]
        marker.color.b = color[2]
        marker.color.a = 1.0 if len(color) < 4 else color[3]
        
        # Marker lasts indefinitely until removed
        marker.lifetime.sec = 0
        marker.lifetime.nanosec = 0
        
        return marker

    def _publish_optimised_waypoint_markers(self):
        """Publish optimized waypoints for visualization."""
        current_optimal_waypoints = self.uwb_initializer.trajectory_manager.current_optimal_waypoints
        if not current_optimal_waypoints or len(current_optimal_waypoints) == 0:
            return
            
        marker_array = MarkerArray()
        frame_id = self.get_parameter('frame_id').get_parameter_value().string_value

        for i, point in enumerate(current_optimal_waypoints):
            marker = Marker()
            marker.header.frame_id = frame_id
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = "optimal_waypoints"
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            marker.scale.x = 0.15
            marker.scale.y = 0.15
            marker.scale.z = 0.15
            marker.color.a = 1.0
            marker.color.r = 1.0  # Red color
            marker.color.g = 0.5  # Add some green to make it more visible
            marker.pose.position.x = float(point[0])
            marker.pose.position.y = float(point[1])
            marker.pose.position.z = float(point[2])
            marker.id = i
            marker_array.markers.append(marker)

        self.visualization_pub_dict['optimised_waypoints'].publish(marker_array)


def main(args=None):
    """Main entry point for the node."""
    rclpy.init(args=args)
    node = UwbOnlineInitialisationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()