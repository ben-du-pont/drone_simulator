// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_H_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_H_

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
// Member 'reached'
// Member 'remaining'
#include "sim_interfaces/msg/detail/waypoint_list__struct.h"

/// Struct defined in msg/WaypointLists in the package sim_interfaces.
/**
  * Message containing both reached and remaining waypoint lists
 */
typedef struct sim_interfaces__msg__WaypointLists
{
  std_msgs__msg__Header header;
  /// List of reached waypoints
  sim_interfaces__msg__WaypointList reached;
  /// List of remaining waypoints
  sim_interfaces__msg__WaypointList remaining;
} sim_interfaces__msg__WaypointLists;

// Struct for a sequence of sim_interfaces__msg__WaypointLists.
typedef struct sim_interfaces__msg__WaypointLists__Sequence
{
  sim_interfaces__msg__WaypointLists * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_interfaces__msg__WaypointLists__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_H_
