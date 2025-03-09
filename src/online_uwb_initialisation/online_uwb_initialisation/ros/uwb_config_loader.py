# In your ROS node: uwb_online_initialisation_node.py

import yaml
import os
from ament_index_python.packages import get_package_share_directory
from online_uwb_initialisation.core.config_params import UwbInitializationConfig


def load_config_from_yaml(node, package_name="simulator_bringup", config_file="uwb_config.yaml"):
    """Load UWB initialization configuration from a YAML file.
    
    Args:
        node: ROS Node instance for logging and parameter access
        package_name: Name of the ROS package containing the config file
        config_file: Name of the YAML configuration file
        
    Returns:
        UwbInitializationConfig object initialized with parameters from the YAML file
    """
    # First check if a config path is specified as a parameter
    config_path = node.declare_parameter('config_path', '').get_parameter_value().string_value
    
    # If no parameter is specified, use the default path
    if not config_path:
        try:
            package_dir = get_package_share_directory(package_name)
            config_path = os.path.join(package_dir, 'config', config_file)
        except Exception as e:
            node.get_logger().error(f"Error finding package directory: {e}")
            # Return default config if we can't find the file
            return UwbInitializationConfig()
    
    # Load configuration from YAML file
    try:
        with open(config_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            node.get_logger().info(f"Loaded configuration from {config_path}")
            
            # Convert YAML data to a flat dictionary for UwbInitializationConfig
            flat_config = flatten_yaml_config(yaml_data)
            
            # Create config from dictionary
            config = UwbInitializationConfig.from_dict(flat_config)
            
            # Log some key configuration values
            node.get_logger().info(f"Configured for {len(config.stopping_criteria.stopping_criteria)} stopping criteria: {config.stopping_criteria.stopping_criteria}")
            node.get_logger().info(f"Using {config.trajectory.trajectory_optimisation_method.name} trajectory optimization method")
            
            return config
    except Exception as e:
        node.get_logger().error(f"Error loading configuration: {e}")
        # Return default config if we can't load the file
        return UwbInitializationConfig()


def flatten_yaml_config(yaml_data, parent_key='', flattened_dict=None):
    """Convert a nested YAML configuration to a flat dictionary.
    
    Args:
        yaml_data: Nested dictionary from YAML parsing
        parent_key: Current parent key (used in recursion)
        flattened_dict: Accumulating flattened dictionary (used in recursion)
        
    Returns:
        Flattened dictionary with dot-separated keys
    """
    if flattened_dict is None:
        flattened_dict = {}
        
    # Handle non-dict case (leaf value)
    if not isinstance(yaml_data, dict):
        flattened_dict[parent_key] = yaml_data
        return flattened_dict
    
    # Process each key in the current level
    for key, value in yaml_data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        
        if isinstance(value, dict):
            # If we have a nested structure, convert to new_key.subkey format
            flatten_yaml_config(value, new_key, flattened_dict)
        else:
            # Otherwise add the value directly
            flattened_dict[new_key] = value
            
    return flattened_dict


# Example YAML configuration structure:
"""
measurement:
  distance_to_anchor_ratio_threshold: 0.03
  number_of_redundant_measurements: 1
  distance_rejection_threshold: 20.0

least_squares:
  use_linear_bias: false
  use_constant_bias: true
  normalised: false
  regularise: true
  rough_estimate_method: "linear_reweighted"
  outlier_removing: "None"
  reweighting_iterations: 5
  use_trimmed_reweighted: true
  weighting_function: "mad"
  huber_delta: 0.01
  tukey_c: 4.685
  welsch_c: 2.0
  non_linear_optimisation_type: "EM"

stopping_criteria:
  criteria:
    - "nb_measurements"
    - "GDOP"
  thresholds:
    number_of_measurements_thresh: 30
    GDOP_thresh: 3.0
    condition_number_thresh: 5e5
  ratios:
    GDOP_ratio_thresh: 0.2
    condition_number_ratio_thresh: 0.1
  convergence_counter_threshold: 3

outlier:
  z_score_threshold: 2.0
  outlier_count_threshold: 3

trajectory:
  trajectory_optimisation_method: "GDOP"
  link_method: "strict_return"
"""