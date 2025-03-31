// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__STRUCT_H_

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

/// Struct defined in msg/AnchorEstimate in the package sim_interfaces.
typedef struct sim_interfaces__msg__AnchorEstimate
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String anchor_id;
  double position_x;
  double position_y;
  double position_z;
  double constant_bias;
  double linear_bias;
} sim_interfaces__msg__AnchorEstimate;

// Struct for a sequence of sim_interfaces__msg__AnchorEstimate.
typedef struct sim_interfaces__msg__AnchorEstimate__Sequence
{
  sim_interfaces__msg__AnchorEstimate * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__AnchorEstimate__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__STRUCT_H_
