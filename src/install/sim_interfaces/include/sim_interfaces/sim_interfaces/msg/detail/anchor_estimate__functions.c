// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_estimate__functions.h"

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

bool
sim_interfaces__msg__AnchorEstimate__init(sim_interfaces__msg__AnchorEstimate * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__AnchorEstimate__fini(msg);
    return false;
  }
  // anchor_id
  if (!rosidl_runtime_c__String__init(&msg->anchor_id)) {
    sim_interfaces__msg__AnchorEstimate__fini(msg);
    return false;
  }
  // position_x
  // position_y
  // position_z
  // constant_bias
  // linear_bias
  return true;
}

void
sim_interfaces__msg__AnchorEstimate__fini(sim_interfaces__msg__AnchorEstimate * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // anchor_id
  rosidl_runtime_c__String__fini(&msg->anchor_id);
  // position_x
  // position_y
  // position_z
  // constant_bias
  // linear_bias
}

bool
sim_interfaces__msg__AnchorEstimate__are_equal(const sim_interfaces__msg__AnchorEstimate * lhs, const sim_interfaces__msg__AnchorEstimate * rhs)
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
  // position_x
  if (lhs->position_x != rhs->position_x) {
    return false;
  }
  // position_y
  if (lhs->position_y != rhs->position_y) {
    return false;
  }
  // position_z
  if (lhs->position_z != rhs->position_z) {
    return false;
  }
  // constant_bias
  if (lhs->constant_bias != rhs->constant_bias) {
    return false;
  }
  // linear_bias
  if (lhs->linear_bias != rhs->linear_bias) {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__AnchorEstimate__copy(
  const sim_interfaces__msg__AnchorEstimate * input,
  sim_interfaces__msg__AnchorEstimate * output)
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
  // position_x
  output->position_x = input->position_x;
  // position_y
  output->position_y = input->position_y;
  // position_z
  output->position_z = input->position_z;
  // constant_bias
  output->constant_bias = input->constant_bias;
  // linear_bias
  output->linear_bias = input->linear_bias;
  return true;
}

sim_interfaces__msg__AnchorEstimate *
sim_interfaces__msg__AnchorEstimate__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimate * msg = (sim_interfaces__msg__AnchorEstimate *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorEstimate), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__AnchorEstimate));
  bool success = sim_interfaces__msg__AnchorEstimate__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__AnchorEstimate__destroy(sim_interfaces__msg__AnchorEstimate * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__AnchorEstimate__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__AnchorEstimate__Sequence__init(sim_interfaces__msg__AnchorEstimate__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimate * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__AnchorEstimate *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__AnchorEstimate), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__AnchorEstimate__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__AnchorEstimate__fini(&data[i - 1]);
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
sim_interfaces__msg__AnchorEstimate__Sequence__fini(sim_interfaces__msg__AnchorEstimate__Sequence * array)
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
      sim_interfaces__msg__AnchorEstimate__fini(&array->data[i]);
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

sim_interfaces__msg__AnchorEstimate__Sequence *
sim_interfaces__msg__AnchorEstimate__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorEstimate__Sequence * array = (sim_interfaces__msg__AnchorEstimate__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorEstimate__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__AnchorEstimate__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__AnchorEstimate__Sequence__destroy(sim_interfaces__msg__AnchorEstimate__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__AnchorEstimate__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__AnchorEstimate__Sequence__are_equal(const sim_interfaces__msg__AnchorEstimate__Sequence * lhs, const sim_interfaces__msg__AnchorEstimate__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__AnchorEstimate__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__AnchorEstimate__Sequence__copy(
  const sim_interfaces__msg__AnchorEstimate__Sequence * input,
  sim_interfaces__msg__AnchorEstimate__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__AnchorEstimate);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__AnchorEstimate * data =
      (sim_interfaces__msg__AnchorEstimate *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__AnchorEstimate__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__AnchorEstimate__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__AnchorEstimate__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
