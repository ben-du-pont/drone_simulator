// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_H_
#define SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/TrajectoryInfo in the package sim_interfaces.
typedef struct sim_interfaces__srv__TrajectoryInfo_Request
{
  uint8_t structure_needs_at_least_one_member;
} sim_interfaces__srv__TrajectoryInfo_Request;

// Struct for a sequence of sim_interfaces__srv__TrajectoryInfo_Request.
typedef struct sim_interfaces__srv__TrajectoryInfo_Request__Sequence
{
  sim_interfaces__srv__TrajectoryInfo_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__srv__TrajectoryInfo_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'waypoints_x'
// Member 'waypoints_y'
// Member 'waypoints_z'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/TrajectoryInfo in the package sim_interfaces.
typedef struct sim_interfaces__srv__TrajectoryInfo_Response
{
  rosidl_runtime_c__double__Sequence waypoints_x;
  rosidl_runtime_c__double__Sequence waypoints_y;
  rosidl_runtime_c__double__Sequence waypoints_z;
} sim_interfaces__srv__TrajectoryInfo_Response;

// Struct for a sequence of sim_interfaces__srv__TrajectoryInfo_Response.
typedef struct sim_interfaces__srv__TrajectoryInfo_Response__Sequence
{
  sim_interfaces__srv__TrajectoryInfo_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__srv__TrajectoryInfo_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_H_
