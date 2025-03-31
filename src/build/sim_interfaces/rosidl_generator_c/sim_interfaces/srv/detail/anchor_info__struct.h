// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_H_
#define SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/AnchorInfo in the package sim_interfaces.
typedef struct sim_interfaces__srv__AnchorInfo_Request
{
  uint8_t structure_needs_at_least_one_member;
} sim_interfaces__srv__AnchorInfo_Request;

// Struct for a sequence of sim_interfaces__srv__AnchorInfo_Request.
typedef struct sim_interfaces__srv__AnchorInfo_Request__Sequence
{
  sim_interfaces__srv__AnchorInfo_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__srv__AnchorInfo_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'known_anchor_ids'
// Member 'unknown_anchor_ids'
#include "rosidl_runtime_c/string.h"
// Member 'known_anchor_x_positions'
// Member 'known_anchor_y_positions'
// Member 'known_anchor_z_positions'
// Member 'known_anchor_biases'
// Member 'known_anchor_linear_biases'
// Member 'known_anchor_noise_variances'
// Member 'unknown_anchor_x_positions'
// Member 'unknown_anchor_y_positions'
// Member 'unknown_anchor_z_positions'
// Member 'unknown_anchor_biases'
// Member 'unknown_anchor_linear_biases'
// Member 'unknown_anchor_noise_variances'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/AnchorInfo in the package sim_interfaces.
typedef struct sim_interfaces__srv__AnchorInfo_Response
{
  rosidl_runtime_c__String__Sequence known_anchor_ids;
  rosidl_runtime_c__double__Sequence known_anchor_x_positions;
  rosidl_runtime_c__double__Sequence known_anchor_y_positions;
  rosidl_runtime_c__double__Sequence known_anchor_z_positions;
  rosidl_runtime_c__double__Sequence known_anchor_biases;
  rosidl_runtime_c__double__Sequence known_anchor_linear_biases;
  rosidl_runtime_c__double__Sequence known_anchor_noise_variances;
  rosidl_runtime_c__String__Sequence unknown_anchor_ids;
  rosidl_runtime_c__double__Sequence unknown_anchor_x_positions;
  rosidl_runtime_c__double__Sequence unknown_anchor_y_positions;
  rosidl_runtime_c__double__Sequence unknown_anchor_z_positions;
  rosidl_runtime_c__double__Sequence unknown_anchor_biases;
  rosidl_runtime_c__double__Sequence unknown_anchor_linear_biases;
  rosidl_runtime_c__double__Sequence unknown_anchor_noise_variances;
} sim_interfaces__srv__AnchorInfo_Response;

// Struct for a sequence of sim_interfaces__srv__AnchorInfo_Response.
typedef struct sim_interfaces__srv__AnchorInfo_Response__Sequence
{
  sim_interfaces__srv__AnchorInfo_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__srv__AnchorInfo_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_H_
