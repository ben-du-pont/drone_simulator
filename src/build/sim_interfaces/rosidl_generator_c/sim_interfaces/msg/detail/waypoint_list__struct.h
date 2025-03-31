// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/WaypointList.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_H_

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
// Member 'x'
// Member 'y'
// Member 'z'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/WaypointList in the package sim_interfaces.
typedef struct sim_interfaces__msg__WaypointList
{
  std_msgs__msg__Header header;
  int32_t count;
  rosidl_runtime_c__double__Sequence x;
  rosidl_runtime_c__double__Sequence y;
  rosidl_runtime_c__double__Sequence z;
} sim_interfaces__msg__WaypointList;

// Struct for a sequence of sim_interfaces__msg__WaypointList.
typedef struct sim_interfaces__msg__WaypointList__Sequence
{
  sim_interfaces__msg__WaypointList * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__WaypointList__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_H_
