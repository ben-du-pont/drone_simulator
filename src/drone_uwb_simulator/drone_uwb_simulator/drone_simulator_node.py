import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped, Quaternion, PoseStamped
from nav_msgs.msg import Path
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from builtin_interfaces.msg import Time

from sim_interfaces.srv import AnchorInfo, TrajectoryInfo
from sim_interfaces.msg import DronePosition

import tf2_ros
import threading
import numpy as np

from drone_uwb_simulator.drone_simulator import DroneSimulation, SimulationConfig, WaypointMode


class DroneSimulationNode(Node):
    """
    ROS2 Node for drone simulation with UWB-based localization.
    
    This node manages:
    - Drone position updates and trajectory visualization
    - UWB anchor information and visualization
    - Service interfaces for external modules
    """
    
    def __init__(self):
        """Initialize the drone simulation node with publishers, subscribers, and services."""
        super().__init__('drone_simulation')
        
        # Declare node parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('namespace', 'drone_sim'),
                ('dt', 0.1),
                ('drone_speed', 3.0),
                ('mesh_resource', 'package://drone_uwb_simulator/drone_mesh.glb'),
                ('frame_id', 'world'),
                ('waypoint_mode', 'OPPOSITE_EDGES')
            ]
        )
        
        # Get parameters
        self.ns = self.get_parameter('namespace').value
        self.frame_id = self.get_parameter('frame_id').value
        self.dt = self.get_parameter('dt').value
        self.drone_speed = self.get_parameter('drone_speed').value
        self.mesh_resource = self.get_parameter('mesh_resource').value
        
        # Set up waypoint mode
        waypoint_mode_str = self.get_parameter('waypoint_mode').value
        self.waypoint_mode = getattr(WaypointMode, waypoint_mode_str)
        
        self.simulation_reset = False

        # Initialize services
        self._init_services()
        
        # Initialize publishers
        self._init_publishers()
        
        # Initialize subscribers
        self._init_subscribers()
        
        # Create the drone simulation
        self._init_simulation()
        
        self.get_logger().info('Drone simulation node initialized')
    
    def _init_services(self):
        """Initialize service servers."""
        self.anchor_info_srv = self.create_service(
            AnchorInfo, 
            f'{self.ns}/get_anchor_info', 
            self.get_anchor_info_callback
        )
        
        self.trajectory_info_srv = self.create_service(
            TrajectoryInfo, 
            f'{self.ns}/get_trajectory_info', 
            self.get_trajectory_info_callback
        )
    
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
        
        # TF broadcaster
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        
        # For tracking drone history
        self.position_history = []
    
    def _init_subscribers(self):
        """Initialize all subscribers."""
        self.optimized_trajectory_sub = self.create_subscription(
            Path,
            f'{self.ns}/optimized_trajectory',
            self.optimized_trajectory_callback,
            10
        )
    
    def _init_simulation(self):
        """Initialize the drone simulation object."""
        # Create simulation configuration
        sim_config = SimulationConfig(
            dt=self.dt,
            drone_speed=self.drone_speed
        )
        
        # Create simulation instance
        self.drone_sim = DroneSimulation(sim_config)
        self.drone_sim.initialize_environment(self.waypoint_mode)
        
        # Initialize anchor information
        self._init_anchor_info()
        
        # Store initial trajectory for reference
        self.initial_trajectory = (
            self.drone_sim.drone_trajectory.points_x.copy(),
            self.drone_sim.drone_trajectory.points_y.copy(),
            self.drone_sim.drone_trajectory.points_z.copy()
        )
    
    def _init_anchor_info(self):
        """Initialize anchor information storage."""
        # Known anchors
        self.known_anchors = {
            'ids': [],
            'positions': {
                'x': [],
                'y': [],
                'z': []
            },
            'biases': [],
            'linear_biases': [],
            'noise_variances': []
        }
        
        # Unknown anchors
        self.unknown_anchors = {
            'ids': [],
            'positions': {
                'x': [],
                'y': [],
                'z': []
            },
            'biases': [],
            'linear_biases': [],
            'noise_variances': []
        }
        
        # Process known anchors
        for anchor in self.drone_sim.base_anchors:
            self.known_anchors['ids'].append(anchor.anchor_id)
            self.known_anchors['positions']['x'].append(float(anchor.position[0]))
            self.known_anchors['positions']['y'].append(float(anchor.position[1]))
            self.known_anchors['positions']['z'].append(float(anchor.position[2]))
            self.known_anchors['biases'].append(float(anchor.bias_model.constant_bias))
            self.known_anchors['linear_biases'].append(float(anchor.bias_model.linear_bias))
            self.known_anchors['noise_variances'].append(float(anchor.noise_model.variance))
        
        # Process unknown anchors
        for anchor in self.drone_sim.unknown_anchors:
            self.unknown_anchors['ids'].append(anchor.anchor_id)
            self.unknown_anchors['positions']['x'].append(float(anchor.position[0]))
            self.unknown_anchors['positions']['y'].append(float(anchor.position[1]))
            self.unknown_anchors['positions']['z'].append(float(anchor.position[2]))
            self.unknown_anchors['biases'].append(float(anchor.bias_model.constant_bias))
            self.unknown_anchors['linear_biases'].append(float(anchor.bias_model.linear_bias))
            self.unknown_anchors['noise_variances'].append(float(anchor.noise_model.variance))
    
    def get_anchor_info_callback(self, request, response):
        """Service callback for providing anchor information."""
        # Fill known anchor data
        response.known_anchor_ids = self.known_anchors['ids']
        response.known_anchor_x_positions = self.known_anchors['positions']['x']
        response.known_anchor_y_positions = self.known_anchors['positions']['y']
        response.known_anchor_z_positions = self.known_anchors['positions']['z']
        response.known_anchor_biases = self.known_anchors['biases']
        response.known_anchor_linear_biases = self.known_anchors['linear_biases']
        response.known_anchor_noise_variances = self.known_anchors['noise_variances']
        
        # Fill unknown anchor data
        response.unknown_anchor_ids = self.unknown_anchors['ids']
        response.unknown_anchor_x_positions = self.unknown_anchors['positions']['x']
        response.unknown_anchor_y_positions = self.unknown_anchors['positions']['y']
        response.unknown_anchor_z_positions = self.unknown_anchors['positions']['z']
        response.unknown_anchor_biases = self.unknown_anchors['biases']
        response.unknown_anchor_linear_biases = self.unknown_anchors['linear_biases']
        response.unknown_anchor_noise_variances = self.unknown_anchors['noise_variances']
        
        self.get_logger().info('Sent anchor information')
        return response
    
    def get_trajectory_info_callback(self, request, response):
        """Service callback for providing trajectory waypoint information."""
        response.waypoints_x = [float(point.x) for point in self.drone_sim.waypoints]
        response.waypoints_y = [float(point.y) for point in self.drone_sim.waypoints]
        response.waypoints_z = [float(point.z) for point in self.drone_sim.waypoints]
        
        self.get_logger().info('Sent trajectory information')
        return response
    
    def optimized_trajectory_callback(self, msg):
        """Callback for receiving an optimized trajectory from external planner."""
        # Extract trajectory points from message
        optimized_x = []
        optimized_y = []
        optimized_z = []
        
        for pose in msg.poses:
            optimized_x.append(pose.pose.position.x)
            optimized_y.append(pose.pose.position.y)
            optimized_z.append(pose.pose.position.z)
        
        # Update simulation trajectory
        self.drone_sim.drone_trajectory.points_x = optimized_x
        self.drone_sim.drone_trajectory.points_y = optimized_y
        self.drone_sim.drone_trajectory.points_z = optimized_z
        
        # Reset drone progress
        self.drone_sim.drone_progress = 0
        
        # Clear history for new trajectory
        self.position_history = []
        
        self.get_logger().info('Applied optimized trajectory')
    
    def run_simulation(self):
        """Main simulation loop."""
        rate = self.create_rate(1.0 / self.drone_sim.config.dt)
        
        while rclpy.ok():

            if self.simulation_reset:
                self.position_history = []
                self.simulation_reset = False


            # Publish static visualization data
            self.publish_trajectory(*self.initial_trajectory)
            self.publish_anchors()
            self.publish_waypoints()
            
            # Update drone position
            new_position = self.drone_sim.update_drone_position()
            self.position_history.append(new_position)
            
            # Get completion progress
            waypoints_achieved = len(self.drone_sim.waypoints) - len(self.drone_sim.get_remaining_waypoints())
            
            # Catch the simulation reset
            if waypoints_achieved == len(self.drone_sim.waypoints):
                self.simulation_reset = True

            # Publish drone position and state
            self.publish_drone_position(new_position, waypoints_achieved)
            self.publish_drone_tf(new_position)
            self.publish_drone_marker()
            self.publish_drone_trail()
            
            rate.sleep()
    
    def publish_drone_position(self, position, waypoints_achieved):
        """Publish current drone position."""
        msg = DronePosition()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        msg.position_x = float(position[0])
        msg.position_y = float(position[1])
        msg.position_z = float(position[2])
        msg.waypoints_achieved = waypoints_achieved
        
        self.drone_position_pub.publish(msg)
    
    def publish_drone_tf(self, position):
        """Publish transform for the drone position."""
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
    
    def publish_trajectory(self, points_x, points_y, points_z):
        """Publish planned trajectory path."""
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
        marker_msg.header.frame_id = f'{self.ns}/drone'
        marker_msg.header.stamp = self.get_clock().now().to_msg()
        marker_msg.ns = f'{self.ns}'
        marker_msg.id = 0
        marker_msg.type = Marker.MESH_RESOURCE
        marker_msg.action = Marker.ADD
        
        # Position and orientation offsets
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
            remaining = self.drone_sim.get_remaining_waypoints()
            if point in remaining:
                marker.color = ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0)  # Red
            else:
                marker.color = ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0)  # Green
            
            marker_array.markers.append(marker)
        
        self.waypoints_pub.publish(marker_array)
    
    def reset_simulation(self, waypoint_mode=None):
        """Reset the simulation with optionally new waypoint generation mode."""
        if waypoint_mode is not None:
            self.waypoint_mode = waypoint_mode
        
        self.drone_sim.reset_simulation(self.waypoint_mode)
        self.position_history = []
        
        # Update initial trajectory reference
        self.initial_trajectory = (
            self.drone_sim.drone_trajectory.points_x.copy(),
            self.drone_sim.drone_trajectory.points_y.copy(),
            self.drone_sim.drone_trajectory.points_z.copy()
        )
        
        self._init_anchor_info()
        self.get_logger().info('Simulation reset')


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