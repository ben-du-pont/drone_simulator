// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/StampedFloat.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_H_

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

/// Struct defined in msg/StampedFloat in the package sim_interfaces.
typedef struct sim_interfaces__msg__StampedFloat
{
  std_msgs__msg__Header header;
  double data;
} sim_interfaces__msg__StampedFloat;

// Struct for a sequence of sim_interfaces__msg__StampedFloat.
typedef struct sim_interfaces__msg__StampedFloat__Sequence
{
  sim_interfaces__msg__StampedFloat * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__StampedFloat__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_H_
