# Minimum CMake version and project name
cmake_minimum_required(VERSION 3.8)
project(sim_interfaces)

# Add compiler warnings if using GCC or Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find required ROS2 packages
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate interfaces from .msg and .srv files
rosidl_generate_interfaces(${PROJECT_NAME}
  # Service definitions
  "srv/AnchorInfo.srv"
  "srv/TrajectoryInfo.srv"
  
  # Message definitions
  "msg/StampedFloat.msg"
  "msg/DronePosition.msg"
  "msg/AnchorEstimate.msg"
  "msg/AnchorEstimates.msg"
  "msg/AnchorError.msg"
  "msg/AnchorErrors.msg"
  "msg/WaypointList.msg"
  "msg/WaypointLists.msg"
  "msg/OptimizedTrajectory.msg"
  "msg/AnchorInfo.msg"
  DEPENDENCIES std_msgs
)

# Export runtime dependencies
ament_export_dependencies(rosidl_default_runtime)

# Required for ROS2 packages
ament_package()
