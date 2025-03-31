// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/AnchorError.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__STRUCT_H_

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

/// Struct defined in msg/AnchorError in the package sim_interfaces.
typedef struct sim_interfaces__msg__AnchorError
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String anchor_id;
  double position_error;
  double constant_bias_error;
  double linear_bias_error;
} sim_interfaces__msg__AnchorError;

// Struct for a sequence of sim_interfaces__msg__AnchorError.
typedef struct sim_interfaces__msg__AnchorError__Sequence
{
  sim_interfaces__msg__AnchorError * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__AnchorError__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__STRUCT_H_
