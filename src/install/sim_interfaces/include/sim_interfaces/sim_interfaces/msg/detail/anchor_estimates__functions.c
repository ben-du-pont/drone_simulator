// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_estimates__functions.h"

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
// Member `linear_estimate`
// Member `refined_estimate`
// Member `final_estimate`
#include "sim_interfaces/msg/detail/anchor_estimate__functions.h"

bool
sim_interfaces__msg__AnchorEstimates__init(sim_interfaces__msg__AnchorEstimates * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
    return false;
  }
  // anchor_id
  if (!rosidl_runtime_c__String__init(&msg->anchor_id)) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
    return false;
  }
  // linear_estimate
  if (!sim_interfaces__msg__AnchorEstimate__init(&msg->linear_estimate)) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
    return false;
  }
  // refined_estimate
  if (!sim_interfaces__msg__AnchorEstimate__init(&msg->refined_estimate)) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
    return false;
  }
  // final_estimate
  if (!sim_interfaces__msg__AnchorEstimate__init(&msg->final_estimate)) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__msg__AnchorEstimates__fini(sim_interfaces__msg__AnchorEstimates * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // anchor_id
  rosidl_runtime_c__String__fini(&msg->anchor_id);
  // linear_estimate
  sim_interfaces__msg__AnchorEstimate__fini(&msg->linear_estimate);
  // refined_estimate
  sim_interfaces__msg__AnchorEstimate__fini(&msg->refined_estimate);
  // final_estimate
  sim_interfaces__msg__AnchorEstimate__fini(&msg->final_estimate);
}

bool
sim_interfaces__msg__AnchorEstimates__are_equal(const sim_interfaces__msg__AnchorEstimates * lhs, const sim_interfaces__msg__AnchorEstimates * rhs)
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
  // linear_estimate
  if (!sim_interfaces__msg__AnchorEstimate__are_equal(
      &(lhs->linear_estimate), &(rhs->linear_estimate)))
  {
    return false;
  }
  // refined_estimate
  if (!sim_interfaces__msg__AnchorEstimate__are_equal(
      &(lhs->refined_estimate), &(rhs->refined_estimate)))
  {
    return false;
  }
  // final_estimate
  if (!sim_interfaces__msg__AnchorEstimate__are_equal(
      &(lhs->final_estimate), &(rhs->final_estimate)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__AnchorEstimates__copy(
  const sim_interfaces__msg__AnchorEstimates * input,
  sim_interfaces__msg__AnchorEstimates * output)
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
  // linear_estimate
  if (!sim_interfaces__msg__AnchorEstimate__copy(
      &(input->linear_estimate), &(output->linear_estimate)))
  {
    return false;
  }
  // refined_estimate
  if (!sim_interfaces__msg__AnchorEstimate__copy(
      &(input->refined_estimate), &(output->refined_estimate)))
  {
    return false;
  }
  // final_estimate
  if (!sim_interfaces__msg__AnchorEstimate__copy(
      &(input->final_estimate), &(output->final_estimate)))
  {
    return false;
  }
  return true;
}

sim_interfaces__msg__AnchorEstimates *
sim_interfaces__msg__AnchorEstimates__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimates * msg = (sim_interfaces__msg__AnchorEstimates *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorEstimates), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__AnchorEstimates));
  bool success = sim_interfaces__msg__AnchorEstimates__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__AnchorEstimates__destroy(sim_interfaces__msg__AnchorEstimates * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__AnchorEstimates__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__AnchorEstimates__Sequence__init(sim_interfaces__msg__AnchorEstimates__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimates * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__AnchorEstimates *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__AnchorEstimates), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__AnchorEstimates__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__AnchorEstimates__fini(&data[i - 1]);
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
sim_interfaces__msg__AnchorEstimates__Sequence__fini(sim_interfaces__msg__AnchorEstimates__Sequence * array)
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
      sim_interfaces__msg__AnchorEstimates__fini(&array->data[i]);
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

sim_interfaces__msg__AnchorEstimates__Sequence *
sim_interfaces__msg__AnchorEstimates__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimates__Sequence * array = (sim_interfaces__msg__AnchorEstimates__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorEstimates__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__AnchorEstimates__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__AnchorEstimates__Sequence__destroy(sim_interfaces__msg__AnchorEstimates__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__AnchorEstimates__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__AnchorEstimates__Sequence__are_equal(const sim_interfaces__msg__AnchorEstimates__Sequence * lhs, const sim_interfaces__msg__AnchorEstimates__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__AnchorEstimates__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__AnchorEstimates__Sequence__copy(
  const sim_interfaces__msg__AnchorEstimates__Sequence * input,
  sim_interfaces__msg__AnchorEstimates__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__AnchorEstimates);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__AnchorEstimates * data =
      (sim_interfaces__msg__AnchorEstimates *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__AnchorEstimates__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__AnchorEstimates__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__AnchorEstimates__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
