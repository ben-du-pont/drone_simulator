// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/OptimizedTrajectory.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'anchor_id'
#include "rosidl_runtime_c/string.h"
// Member 'waypoint_x'
// Member 'waypoint_y'
// Member 'waypoint_z'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/OptimizedTrajectory in the package sim_interfaces.
typedef struct sim_interfaces__msg__OptimizedTrajectory
{
  std_msgs__msg__Header header;
  /// ID of the anchor that triggered the optimization
  rosidl_runtime_c__String anchor_id;
  int32_t waypoint_count;
  rosidl_runtime_c__double__Sequence waypoint_x;
  rosidl_runtime_c__double__Sequence waypoint_y;
  rosidl_runtime_c__double__Sequence waypoint_z;
} sim_interfaces__msg__OptimizedTrajectory;

// Struct for a sequence of sim_interfaces__msg__OptimizedTrajectory.
typedef struct sim_interfaces__msg__OptimizedTrajectory__Sequence
{
  sim_interfaces__msg__OptimizedTrajectory * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__OptimizedTrajectory__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_H_
