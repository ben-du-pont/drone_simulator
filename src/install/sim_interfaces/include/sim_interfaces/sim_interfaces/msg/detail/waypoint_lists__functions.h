// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__FUNCTIONS_H_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sim_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "sim_interfaces/msg/detail/waypoint_lists__struct.h"

/// Initialize msg/WaypointLists message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sim_interfaces__msg__WaypointLists
 * )) before or use
 * sim_interfaces__msg__WaypointLists__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__init(sim_interfaces__msg__WaypointLists * msg);

/// Finalize msg/WaypointLists message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__WaypointLists__fini(sim_interfaces__msg__WaypointLists * msg);

/// Create msg/WaypointLists message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sim_interfaces__msg__WaypointLists__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__WaypointLists *
sim_interfaces__msg__WaypointLists__create();

/// Destroy msg/WaypointLists message.
/**
 * It calls
 * sim_interfaces__msg__WaypointLists__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__WaypointLists__destroy(sim_interfaces__msg__WaypointLists * msg);

/// Check for msg/WaypointLists message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__are_equal(const sim_interfaces__msg__WaypointLists * lhs, const sim_interfaces__msg__WaypointLists * rhs);

/// Copy a msg/WaypointLists message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__copy(
  const sim_interfaces__msg__WaypointLists * input,
  sim_interfaces__msg__WaypointLists * output);

/// Initialize array of msg/WaypointLists messages.
/**
 * It allocates the memory for the number of elements and calls
 * sim_interfaces__msg__WaypointLists__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__Sequence__init(sim_interfaces__msg__WaypointLists__Sequence * array, size_t size);

/// Finalize array of msg/WaypointLists messages.
/**
 * It calls
 * sim_interfaces__msg__WaypointLists__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__WaypointLists__Sequence__fini(sim_interfaces__msg__WaypointLists__Sequence * array);

/// Create array of msg/WaypointLists messages.
/**
 * It allocates the memory for the array and calls
 * sim_interfaces__msg__WaypointLists__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__WaypointLists__Sequence *
sim_interfaces__msg__WaypointLists__Sequence__create(size_t size);

/// Destroy array of msg/WaypointLists messages.
/**
 * It calls
 * sim_interfaces__msg__WaypointLists__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__WaypointLists__Sequence__destroy(sim_interfaces__msg__WaypointLists__Sequence * array);

/// Check for msg/WaypointLists message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__Sequence__are_equal(const sim_interfaces__msg__WaypointLists__Sequence * lhs, const sim_interfaces__msg__WaypointLists__Sequence * rhs);

/// Copy an array of msg/WaypointLists messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__WaypointLists__Sequence__copy(
  const sim_interfaces__msg__WaypointLists__Sequence * input,
  sim_interfaces__msg__WaypointLists__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__FUNCTIONS_H_
