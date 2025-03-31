// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_errors__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `anchor_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `linear_error`
// Member `nonlinear_error`
// Member `final_error`
#include "sim_interfaces/msg/detail/anchor_error__functions.h"

bool
sim_interfaces__msg__AnchorErrors__init(sim_interfaces__msg__AnchorErrors * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
    return false;
  }
  // anchor_id
  if (!rosidl_runtime_c__String__init(&msg->anchor_id)) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
    return false;
  }
  // linear_error
  if (!sim_interfaces__msg__AnchorError__init(&msg->linear_error)) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
    return false;
  }
  // nonlinear_error
  if (!sim_interfaces__msg__AnchorError__init(&msg->nonlinear_error)) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
    return false;
  }
  // final_error
  if (!sim_interfaces__msg__AnchorError__init(&msg->final_error)) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__msg__AnchorErrors__fini(sim_interfaces__msg__AnchorErrors * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // anchor_id
  rosidl_runtime_c__String__fini(&msg->anchor_id);
  // linear_error
  sim_interfaces__msg__AnchorError__fini(&msg->linear_error);
  // nonlinear_error
  sim_interfaces__msg__AnchorError__fini(&msg->nonlinear_error);
  // final_error
  sim_interfaces__msg__AnchorError__fini(&msg->final_error);
}

bool
sim_interfaces__msg__AnchorErrors__are_equal(const sim_interfaces__msg__AnchorErrors * lhs, const sim_interfaces__msg__AnchorErrors * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // anchor_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->anchor_id), &(rhs->anchor_id)))
  {
    return false;
  }
  // linear_error
  if (!sim_interfaces__msg__AnchorError__are_equal(
      &(lhs->linear_error), &(rhs->linear_error)))
  {
    return false;
  }
  // nonlinear_error
  if (!sim_interfaces__msg__AnchorError__are_equal(
      &(lhs->nonlinear_error), &(rhs->nonlinear_error)))
  {
    return false;
  }
  // final_error
  if (!sim_interfaces__msg__AnchorError__are_equal(
      &(lhs->final_error), &(rhs->final_error)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__AnchorErrors__copy(
  const sim_interfaces__msg__AnchorErrors * input,
  sim_interfaces__msg__AnchorErrors * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // anchor_id
  if (!rosidl_runtime_c__String__copy(
      &(input->anchor_id), &(output->anchor_id)))
  {
    return false;
  }
  // linear_error
  if (!sim_interfaces__msg__AnchorError__copy(
      &(input->linear_error), &(output->linear_error)))
  {
    return false;
  }
  // nonlinear_error
  if (!sim_interfaces__msg__AnchorError__copy(
      &(input->nonlinear_error), &(output->nonlinear_error)))
  {
    return false;
  }
  // final_error
  if (!sim_interfaces__msg__AnchorError__copy(
      &(input->final_error), &(output->final_error)))
  {
    return false;
  }
  return true;
}

sim_interfaces__msg__AnchorErrors *
sim_interfaces__msg__AnchorErrors__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorErrors * msg = (sim_interfaces__msg__AnchorErrors *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorErrors), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__AnchorErrors));
  bool success = sim_interfaces__msg__AnchorErrors__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__AnchorErrors__destroy(sim_interfaces__msg__AnchorErrors * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__AnchorErrors__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__AnchorErrors__Sequence__init(sim_interfaces__msg__AnchorErrors__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorErrors * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__AnchorErrors *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__AnchorErrors), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__AnchorErrors__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__AnchorErrors__fini(&data[i - 1]);
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
sim_interfaces__msg__AnchorErrors__Sequence__fini(sim_interfaces__msg__AnchorErrors__Sequence * array)
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
      sim_interfaces__msg__AnchorErrors__fini(&array->data[i]);
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

sim_interfaces__msg__AnchorErrors__Sequence *
sim_interfaces__msg__AnchorErrors__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorErrors__Sequence * array = (sim_interfaces__msg__AnchorErrors__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorErrors__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__AnchorErrors__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__AnchorErrors__Sequence__destroy(sim_interfaces__msg__AnchorErrors__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__AnchorErrors__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__AnchorErrors__Sequence__are_equal(const sim_interfaces__msg__AnchorErrors__Sequence * lhs, const sim_interfaces__msg__AnchorErrors__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__AnchorErrors__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__AnchorErrors__Sequence__copy(
  const sim_interfaces__msg__AnchorErrors__Sequence * input,
  sim_interfaces__msg__AnchorErrors__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__AnchorErrors);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__AnchorErrors * data =
      (sim_interfaces__msg__AnchorErrors *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__AnchorErrors__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__AnchorErrors__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__AnchorErrors__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
