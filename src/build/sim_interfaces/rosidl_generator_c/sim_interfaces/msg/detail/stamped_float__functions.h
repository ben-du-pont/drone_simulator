// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sim_interfaces:msg/StampedFloat.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__FUNCTIONS_H_
#define SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sim_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "sim_interfaces/msg/detail/stamped_float__struct.h"

/// Initialize msg/StampedFloat message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sim_interfaces__msg__StampedFloat
 * )) before or use
 * sim_interfaces__msg__StampedFloat__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__StampedFloat__init(sim_interfaces__msg__StampedFloat * msg);

/// Finalize msg/StampedFloat message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__StampedFloat__fini(sim_interfaces__msg__StampedFloat * msg);

/// Create msg/StampedFloat message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sim_interfaces__msg__StampedFloat__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__StampedFloat *
sim_interfaces__msg__StampedFloat__create();

/// Destroy msg/StampedFloat message.
/**
 * It calls
 * sim_interfaces__msg__StampedFloat__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__StampedFloat__destroy(sim_interfaces__msg__StampedFloat * msg);

/// Check for msg/StampedFloat message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__StampedFloat__are_equal(const sim_interfaces__msg__StampedFloat * lhs, const sim_interfaces__msg__StampedFloat * rhs);

/// Copy a msg/StampedFloat message.
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
sim_interfaces__msg__StampedFloat__copy(
  const sim_interfaces__msg__StampedFloat * input,
  sim_interfaces__msg__StampedFloat * output);

/// Initialize array of msg/StampedFloat messages.
/**
 * It allocates the memory for the number of elements and calls
 * sim_interfaces__msg__StampedFloat__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__StampedFloat__Sequence__init(sim_interfaces__msg__StampedFloat__Sequence * array, size_t size);

/// Finalize array of msg/StampedFloat messages.
/**
 * It calls
 * sim_interfaces__msg__StampedFloat__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__StampedFloat__Sequence__fini(sim_interfaces__msg__StampedFloat__Sequence * array);

/// Create array of msg/StampedFloat messages.
/**
 * It allocates the memory for the array and calls
 * sim_interfaces__msg__StampedFloat__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
sim_interfaces__msg__StampedFloat__Sequence *
sim_interfaces__msg__StampedFloat__Sequence__create(size_t size);

/// Destroy array of msg/StampedFloat messages.
/**
 * It calls
 * sim_interfaces__msg__StampedFloat__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
void
sim_interfaces__msg__StampedFloat__Sequence__destroy(sim_interfaces__msg__StampedFloat__Sequence * array);

/// Check for msg/StampedFloat message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_interfaces
bool
sim_interfaces__msg__StampedFloat__Sequence__are_equal(const sim_interfaces__msg__StampedFloat__Sequence * lhs, const sim_interfaces__msg__StampedFloat__Sequence * rhs);

/// Copy an array of msg/StampedFloat messages.
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
sim_interfaces__msg__StampedFloat__Sequence__copy(
  const sim_interfaces__msg__StampedFloat__Sequence * input,
  sim_interfaces__msg__StampedFloat__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__FUNCTIONS_H_
