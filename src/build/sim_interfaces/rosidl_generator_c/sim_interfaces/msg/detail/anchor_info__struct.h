// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__STRUCT_H_

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
// Member 'ids'
#include "rosidl_runtime_c/string.h"
// Member 'x'
// Member 'y'
// Member 'z'
// Member 'constant_bias'
// Member 'linear_bias'
// Member 'types'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/AnchorInfo in the package sim_interfaces.
typedef struct sim_interfaces__msg__AnchorInfo
{
  std_msgs__msg__Header header;
  /// Number of anchors
  int32_t count;
  /// Anchor IDs
  rosidl_runtime_c__String__Sequence ids;
  /// Positions
  rosidl_runtime_c__double__Sequence x;
  rosidl_runtime_c__double__Sequence y;
  rosidl_runtime_c__double__Sequence z;
  /// Bias parameters
  rosidl_runtime_c__double__Sequence constant_bias;
  rosidl_runtime_c__double__Sequence linear_bias;
  /// Anchor types - 0 for known, 1 for unknown
  rosidl_runtime_c__int32__Sequence types;
} sim_interfaces__msg__AnchorInfo;

// Struct for a sequence of sim_interfaces__msg__AnchorInfo.
typedef struct sim_interfaces__msg__AnchorInfo__Sequence
{
  sim_interfaces__msg__AnchorInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__AnchorInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__STRUCT_H_
