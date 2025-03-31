from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    # Get the path to the parameters file
    config_file = os.path.join(
        get_package_share_directory('simulator_bringup'),
        'config',
        'drone_sim_params.yaml'
    )

    sim_node = Node(
            package='drone_uwb_simulator',
            executable='drone_simulator',
            name='sim',
            output='screen',
            parameters=[config_file]
        )
    
    error_calculator_node = Node(
            package='online_uwb_initialisation',
            executable='uwb_online_initialisation',
            name='estimator',
            output='screen',
            parameters=[config_file]
        )
    
    ld.add_action(sim_node)
    ld.add_action(error_calculator_node)

    return ld