// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/srv/detail/anchor_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
sim_interfaces__srv__AnchorInfo_Request__init(sim_interfaces__srv__AnchorInfo_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
sim_interfaces__srv__AnchorInfo_Request__fini(sim_interfaces__srv__AnchorInfo_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
sim_interfaces__srv__AnchorInfo_Request__are_equal(const sim_interfaces__srv__AnchorInfo_Request * lhs, const sim_interfaces__srv__AnchorInfo_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
sim_interfaces__srv__AnchorInfo_Request__copy(
  const sim_interfaces__srv__AnchorInfo_Request * input,
  sim_interfaces__srv__AnchorInfo_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

sim_interfaces__srv__AnchorInfo_Request *
sim_interfaces__srv__AnchorInfo_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Request * msg = (sim_interfaces__srv__AnchorInfo_Request *)allocator.allocate(sizeof(sim_interfaces__srv__AnchorInfo_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__srv__AnchorInfo_Request));
  bool success = sim_interfaces__srv__AnchorInfo_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__srv__AnchorInfo_Request__destroy(sim_interfaces__srv__AnchorInfo_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__srv__AnchorInfo_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__srv__AnchorInfo_Request__Sequence__init(sim_interfaces__srv__AnchorInfo_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Request * data = NULL;

  if (size) {
    data = (sim_interfaces__srv__AnchorInfo_Request *)allocator.zero_allocate(size, sizeof(sim_interfaces__srv__AnchorInfo_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__srv__AnchorInfo_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__srv__AnchorInfo_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sim_interfaces__srv__AnchorInfo_Request__Sequence__fini(sim_interfaces__srv__AnchorInfo_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sim_interfaces__srv__AnchorInfo_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sim_interfaces__srv__AnchorInfo_Request__Sequence *
sim_interfaces__srv__AnchorInfo_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Request__Sequence * array = (sim_interfaces__srv__AnchorInfo_Request__Sequence *)allocator.allocate(sizeof(sim_interfaces__srv__AnchorInfo_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__srv__AnchorInfo_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__srv__AnchorInfo_Request__Sequence__destroy(sim_interfaces__srv__AnchorInfo_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__srv__AnchorInfo_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__srv__AnchorInfo_Request__Sequence__are_equal(const sim_interfaces__srv__AnchorInfo_Request__Sequence * lhs, const sim_interfaces__srv__AnchorInfo_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__srv__AnchorInfo_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__srv__AnchorInfo_Request__Sequence__copy(
  const sim_interfaces__srv__AnchorInfo_Request__Sequence * input,
  sim_interfaces__srv__AnchorInfo_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__srv__AnchorInfo_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__srv__AnchorInfo_Request * data =
      (sim_interfaces__srv__AnchorInfo_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__srv__AnchorInfo_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__srv__AnchorInfo_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__srv__AnchorInfo_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `known_anchor_ids`
// Member `unknown_anchor_ids`
#include "rosidl_runtime_c/string_functions.h"
// Member `known_anchor_x_positions`
// Member `known_anchor_y_positions`
// Member `known_anchor_z_positions`
// Member `known_anchor_biases`
// Member `known_anchor_linear_biases`
// Member `known_anchor_noise_variances`
// Member `unknown_anchor_x_positions`
// Member `unknown_anchor_y_positions`
// Member `unknown_anchor_z_positions`
// Member `unknown_anchor_biases`
// Member `unknown_anchor_linear_biases`
// Member `unknown_anchor_noise_variances`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
sim_interfaces__srv__AnchorInfo_Response__init(sim_interfaces__srv__AnchorInfo_Response * msg)
{
  if (!msg) {
    return false;
  }
  // known_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__init(&msg->known_anchor_ids, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_x_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_y_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_z_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_biases, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_linear_biases, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // known_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__init(&msg->known_anchor_noise_variances, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__init(&msg->unknown_anchor_ids, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_x_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_y_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_z_positions, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_biases, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_linear_biases, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  // unknown_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__init(&msg->unknown_anchor_noise_variances, 0)) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__srv__AnchorInfo_Response__fini(sim_interfaces__srv__AnchorInfo_Response * msg)
{
  if (!msg) {
    return;
  }
  // known_anchor_ids
  rosidl_runtime_c__String__Sequence__fini(&msg->known_anchor_ids);
  // known_anchor_x_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_x_positions);
  // known_anchor_y_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_y_positions);
  // known_anchor_z_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_z_positions);
  // known_anchor_biases
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_biases);
  // known_anchor_linear_biases
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_linear_biases);
  // known_anchor_noise_variances
  rosidl_runtime_c__double__Sequence__fini(&msg->known_anchor_noise_variances);
  // unknown_anchor_ids
  rosidl_runtime_c__String__Sequence__fini(&msg->unknown_anchor_ids);
  // unknown_anchor_x_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_x_positions);
  // unknown_anchor_y_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_y_positions);
  // unknown_anchor_z_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_z_positions);
  // unknown_anchor_biases
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_biases);
  // unknown_anchor_linear_biases
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_linear_biases);
  // unknown_anchor_noise_variances
  rosidl_runtime_c__double__Sequence__fini(&msg->unknown_anchor_noise_variances);
}

bool
sim_interfaces__srv__AnchorInfo_Response__are_equal(const sim_interfaces__srv__AnchorInfo_Response * lhs, const sim_interfaces__srv__AnchorInfo_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // known_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->known_anchor_ids), &(rhs->known_anchor_ids)))
  {
    return false;
  }
  // known_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_x_positions), &(rhs->known_anchor_x_positions)))
  {
    return false;
  }
  // known_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_y_positions), &(rhs->known_anchor_y_positions)))
  {
    return false;
  }
  // known_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_z_positions), &(rhs->known_anchor_z_positions)))
  {
    return false;
  }
  // known_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_biases), &(rhs->known_anchor_biases)))
  {
    return false;
  }
  // known_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_linear_biases), &(rhs->known_anchor_linear_biases)))
  {
    return false;
  }
  // known_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->known_anchor_noise_variances), &(rhs->known_anchor_noise_variances)))
  {
    return false;
  }
  // unknown_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->unknown_anchor_ids), &(rhs->unknown_anchor_ids)))
  {
    return false;
  }
  // unknown_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_x_positions), &(rhs->unknown_anchor_x_positions)))
  {
    return false;
  }
  // unknown_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_y_positions), &(rhs->unknown_anchor_y_positions)))
  {
    return false;
  }
  // unknown_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_z_positions), &(rhs->unknown_anchor_z_positions)))
  {
    return false;
  }
  // unknown_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_biases), &(rhs->unknown_anchor_biases)))
  {
    return false;
  }
  // unknown_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_linear_biases), &(rhs->unknown_anchor_linear_biases)))
  {
    return false;
  }
  // unknown_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->unknown_anchor_noise_variances), &(rhs->unknown_anchor_noise_variances)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__srv__AnchorInfo_Response__copy(
  const sim_interfaces__srv__AnchorInfo_Response * input,
  sim_interfaces__srv__AnchorInfo_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // known_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->known_anchor_ids), &(output->known_anchor_ids)))
  {
    return false;
  }
  // known_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_x_positions), &(output->known_anchor_x_positions)))
  {
    return false;
  }
  // known_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_y_positions), &(output->known_anchor_y_positions)))
  {
    return false;
  }
  // known_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_z_positions), &(output->known_anchor_z_positions)))
  {
    return false;
  }
  // known_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_biases), &(output->known_anchor_biases)))
  {
    return false;
  }
  // known_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_linear_biases), &(output->known_anchor_linear_biases)))
  {
    return false;
  }
  // known_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->known_anchor_noise_variances), &(output->known_anchor_noise_variances)))
  {
    return false;
  }
  // unknown_anchor_ids
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->unknown_anchor_ids), &(output->unknown_anchor_ids)))
  {
    return false;
  }
  // unknown_anchor_x_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_x_positions), &(output->unknown_anchor_x_positions)))
  {
    return false;
  }
  // unknown_anchor_y_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_y_positions), &(output->unknown_anchor_y_positions)))
  {
    return false;
  }
  // unknown_anchor_z_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_z_positions), &(output->unknown_anchor_z_positions)))
  {
    return false;
  }
  // unknown_anchor_biases
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_biases), &(output->unknown_anchor_biases)))
  {
    return false;
  }
  // unknown_anchor_linear_biases
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_linear_biases), &(output->unknown_anchor_linear_biases)))
  {
    return false;
  }
  // unknown_anchor_noise_variances
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->unknown_anchor_noise_variances), &(output->unknown_anchor_noise_variances)))
  {
    return false;
  }
  return true;
}

sim_interfaces__srv__AnchorInfo_Response *
sim_interfaces__srv__AnchorInfo_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Response * msg = (sim_interfaces__srv__AnchorInfo_Response *)allocator.allocate(sizeof(sim_interfaces__srv__AnchorInfo_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__srv__AnchorInfo_Response));
  bool success = sim_interfaces__srv__AnchorInfo_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__srv__AnchorInfo_Response__destroy(sim_interfaces__srv__AnchorInfo_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__srv__AnchorInfo_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__srv__AnchorInfo_Response__Sequence__init(sim_interfaces__srv__AnchorInfo_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Response * data = NULL;

  if (size) {
    data = (sim_interfaces__srv__AnchorInfo_Response *)allocator.zero_allocate(size, sizeof(sim_interfaces__srv__AnchorInfo_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__srv__AnchorInfo_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__srv__AnchorInfo_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sim_interfaces__srv__AnchorInfo_Response__Sequence__fini(sim_interfaces__srv__AnchorInfo_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sim_interfaces__srv__AnchorInfo_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sim_interfaces__srv__AnchorInfo_Response__Sequence *
sim_interfaces__srv__AnchorInfo_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__AnchorInfo_Response__Sequence * array = (sim_interfaces__srv__AnchorInfo_Response__Sequence *)allocator.allocate(sizeof(sim_interfaces__srv__AnchorInfo_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__srv__AnchorInfo_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__srv__AnchorInfo_Response__Sequence__destroy(sim_interfaces__srv__AnchorInfo_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__srv__AnchorInfo_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__srv__AnchorInfo_Response__Sequence__are_equal(const sim_interfaces__srv__AnchorInfo_Response__Sequence * lhs, const sim_interfaces__srv__AnchorInfo_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__srv__AnchorInfo_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__srv__AnchorInfo_Response__Sequence__copy(
  const sim_interfaces__srv__AnchorInfo_Response__Sequence * input,
  sim_interfaces__srv__AnchorInfo_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__srv__AnchorInfo_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__srv__AnchorInfo_Response * data =
      (sim_interfaces__srv__AnchorInfo_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__srv__AnchorInfo_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__srv__AnchorInfo_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__srv__AnchorInfo_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
