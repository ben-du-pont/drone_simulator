// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_H_

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
// Member 'linear_estimate'
// Member 'refined_estimate'
// Member 'final_estimate'
#include "sim_interfaces/msg/detail/anchor_estimate__struct.h"

/// Struct defined in msg/AnchorEstimates in the package sim_interfaces.
typedef struct sim_interfaces__msg__AnchorEstimates
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String anchor_id;
  sim_interfaces__msg__AnchorEstimate linear_estimate;
  sim_interfaces__msg__AnchorEstimate refined_estimate;
  sim_interfaces__msg__AnchorEstimate final_estimate;
} sim_interfaces__msg__AnchorEstimates;

// Struct for a sequence of sim_interfaces__msg__AnchorEstimates.
typedef struct sim_interfaces__msg__AnchorEstimates__Sequence
{
  sim_interfaces__msg__AnchorEstimates * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__AnchorEstimates__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_H_
