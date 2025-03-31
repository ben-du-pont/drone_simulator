// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__FUNCTIONS_H_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sim_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "sim_interfaces/msg/detail/anchor_estimate__struct.h"

/// Initialize msg/AnchorEstimate message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sim_interfaces__msg__AnchorEstimate
 * )) before or use
 * sim_interfaces__msg__AnchorEstimate__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__AnchorEstimate__init(sim_interfaces__msg__AnchorEstimate * msg);

/// Finalize msg/AnchorEstimate message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__AnchorEstimate__fini(sim_interfaces__msg__AnchorEstimate * msg);

/// Create msg/AnchorEstimate message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sim_interfaces__msg__AnchorEstimate__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__AnchorEstimate *
sim_interfaces__msg__AnchorEstimate__create();

/// Destroy msg/AnchorEstimate message.
/**
 * It calls
 * sim_interfaces__msg__AnchorEstimate__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__AnchorEstimate__destroy(sim_interfaces__msg__AnchorEstimate * msg);

/// Check for msg/AnchorEstimate message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__AnchorEstimate__are_equal(const sim_interfaces__msg__AnchorEstimate * lhs, const sim_interfaces__msg__AnchorEstimate * rhs);

/// Copy a msg/AnchorEstimate message.
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
sim_interfaces__msg__AnchorEstimate__copy(
  const sim_interfaces__msg__AnchorEstimate * input,
  sim_interfaces__msg__AnchorEstimate * output);

/// Initialize array of msg/AnchorEstimate messages.
/**
 * It allocates the memory for the number of elements and calls
 * sim_interfaces__msg__AnchorEstimate__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__AnchorEstimate__Sequence__init(sim_interfaces__msg__AnchorEstimate__Sequence * array, size_t size);

/// Finalize array of msg/AnchorEstimate messages.
/**
 * It calls
 * sim_interfaces__msg__AnchorEstimate__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__AnchorEstimate__Sequence__fini(sim_interfaces__msg__AnchorEstimate__Sequence * array);

/// Create array of msg/AnchorEstimate messages.
/**
 * It allocates the memory for the array and calls
 * sim_interfaces__msg__AnchorEstimate__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__AnchorEstimate__Sequence *
sim_interfaces__msg__AnchorEstimate__Sequence__create(size_t size);

/// Destroy array of msg/AnchorEstimate messages.
/**
 * It calls
 * sim_interfaces__msg__AnchorEstimate__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__AnchorEstimate__Sequence__destroy(sim_interfaces__msg__AnchorEstimate__Sequence * array);

/// Check for msg/AnchorEstimate message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__AnchorEstimate__Sequence__are_equal(const sim_interfaces__msg__AnchorEstimate__Sequence * lhs, const sim_interfaces__msg__AnchorEstimate__Sequence * rhs);

/// Copy an array of msg/AnchorEstimate messages.
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
sim_interfaces__msg__AnchorEstimate__Sequence__copy(
  const sim_interfaces__msg__AnchorEstimate__Sequence * input,
  sim_interfaces__msg__AnchorEstimate__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__FUNCTIONS_H_
