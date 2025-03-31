// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/srv/detail/trajectory_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
sim_interfaces__srv__TrajectoryInfo_Request__init(sim_interfaces__srv__TrajectoryInfo_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
sim_interfaces__srv__TrajectoryInfo_Request__fini(sim_interfaces__srv__TrajectoryInfo_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
sim_interfaces__srv__TrajectoryInfo_Request__are_equal(const sim_interfaces__srv__TrajectoryInfo_Request * lhs, const sim_interfaces__srv__TrajectoryInfo_Request * rhs)
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
sim_interfaces__srv__TrajectoryInfo_Request__copy(
  const sim_interfaces__srv__TrajectoryInfo_Request * input,
  sim_interfaces__srv__TrajectoryInfo_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

sim_interfaces__srv__TrajectoryInfo_Request *
sim_interfaces__srv__TrajectoryInfo_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Request * msg = (sim_interfaces__srv__TrajectoryInfo_Request *)allocator.allocate(sizeof(sim_interfaces__srv__TrajectoryInfo_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__srv__TrajectoryInfo_Request));
  bool success = sim_interfaces__srv__TrajectoryInfo_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__srv__TrajectoryInfo_Request__destroy(sim_interfaces__srv__TrajectoryInfo_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__srv__TrajectoryInfo_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__init(sim_interfaces__srv__TrajectoryInfo_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Request * data = NULL;

  if (size) {
    data = (sim_interfaces__srv__TrajectoryInfo_Request *)allocator.zero_allocate(size, sizeof(sim_interfaces__srv__TrajectoryInfo_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__srv__TrajectoryInfo_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__srv__TrajectoryInfo_Request__fini(&data[i - 1]);
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
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__fini(sim_interfaces__srv__TrajectoryInfo_Request__Sequence * array)
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
      sim_interfaces__srv__TrajectoryInfo_Request__fini(&array->data[i]);
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

sim_interfaces__srv__TrajectoryInfo_Request__Sequence *
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Request__Sequence * array = (sim_interfaces__srv__TrajectoryInfo_Request__Sequence *)allocator.allocate(sizeof(sim_interfaces__srv__TrajectoryInfo_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__srv__TrajectoryInfo_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__destroy(sim_interfaces__srv__TrajectoryInfo_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__srv__TrajectoryInfo_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__are_equal(const sim_interfaces__srv__TrajectoryInfo_Request__Sequence * lhs, const sim_interfaces__srv__TrajectoryInfo_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__srv__TrajectoryInfo_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__srv__TrajectoryInfo_Request__Sequence__copy(
  const sim_interfaces__srv__TrajectoryInfo_Request__Sequence * input,
  sim_interfaces__srv__TrajectoryInfo_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__srv__TrajectoryInfo_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__srv__TrajectoryInfo_Request * data =
      (sim_interfaces__srv__TrajectoryInfo_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__srv__TrajectoryInfo_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__srv__TrajectoryInfo_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__srv__TrajectoryInfo_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `waypoints_x`
// Member `waypoints_y`
// Member `waypoints_z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
sim_interfaces__srv__TrajectoryInfo_Response__init(sim_interfaces__srv__TrajectoryInfo_Response * msg)
{
  if (!msg) {
    return false;
  }
  // waypoints_x
  if (!rosidl_runtime_c__double__Sequence__init(&msg->waypoints_x, 0)) {
    sim_interfaces__srv__TrajectoryInfo_Response__fini(msg);
    return false;
  }
  // waypoints_y
  if (!rosidl_runtime_c__double__Sequence__init(&msg->waypoints_y, 0)) {
    sim_interfaces__srv__TrajectoryInfo_Response__fini(msg);
    return false;
  }
  // waypoints_z
  if (!rosidl_runtime_c__double__Sequence__init(&msg->waypoints_z, 0)) {
    sim_interfaces__srv__TrajectoryInfo_Response__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__srv__TrajectoryInfo_Response__fini(sim_interfaces__srv__TrajectoryInfo_Response * msg)
{
  if (!msg) {
    return;
  }
  // waypoints_x
  rosidl_runtime_c__double__Sequence__fini(&msg->waypoints_x);
  // waypoints_y
  rosidl_runtime_c__double__Sequence__fini(&msg->waypoints_y);
  // waypoints_z
  rosidl_runtime_c__double__Sequence__fini(&msg->waypoints_z);
}

bool
sim_interfaces__srv__TrajectoryInfo_Response__are_equal(const sim_interfaces__srv__TrajectoryInfo_Response * lhs, const sim_interfaces__srv__TrajectoryInfo_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // waypoints_x
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->waypoints_x), &(rhs->waypoints_x)))
  {
    return false;
  }
  // waypoints_y
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->waypoints_y), &(rhs->waypoints_y)))
  {
    return false;
  }
  // waypoints_z
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->waypoints_z), &(rhs->waypoints_z)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__srv__TrajectoryInfo_Response__copy(
  const sim_interfaces__srv__TrajectoryInfo_Response * input,
  sim_interfaces__srv__TrajectoryInfo_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // waypoints_x
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->waypoints_x), &(output->waypoints_x)))
  {
    return false;
  }
  // waypoints_y
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->waypoints_y), &(output->waypoints_y)))
  {
    return false;
  }
  // waypoints_z
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->waypoints_z), &(output->waypoints_z)))
  {
    return false;
  }
  return true;
}

sim_interfaces__srv__TrajectoryInfo_Response *
sim_interfaces__srv__TrajectoryInfo_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Response * msg = (sim_interfaces__srv__TrajectoryInfo_Response *)allocator.allocate(sizeof(sim_interfaces__srv__TrajectoryInfo_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__srv__TrajectoryInfo_Response));
  bool success = sim_interfaces__srv__TrajectoryInfo_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__srv__TrajectoryInfo_Response__destroy(sim_interfaces__srv__TrajectoryInfo_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__srv__TrajectoryInfo_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__init(sim_interfaces__srv__TrajectoryInfo_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Response * data = NULL;

  if (size) {
    data = (sim_interfaces__srv__TrajectoryInfo_Response *)allocator.zero_allocate(size, sizeof(sim_interfaces__srv__TrajectoryInfo_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__srv__TrajectoryInfo_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__srv__TrajectoryInfo_Response__fini(&data[i - 1]);
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
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__fini(sim_interfaces__srv__TrajectoryInfo_Response__Sequence * array)
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
      sim_interfaces__srv__TrajectoryInfo_Response__fini(&array->data[i]);
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

sim_interfaces__srv__TrajectoryInfo_Response__Sequence *
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__srv__TrajectoryInfo_Response__Sequence * array = (sim_interfaces__srv__TrajectoryInfo_Response__Sequence *)allocator.allocate(sizeof(sim_interfaces__srv__TrajectoryInfo_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__srv__TrajectoryInfo_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__destroy(sim_interfaces__srv__TrajectoryInfo_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__srv__TrajectoryInfo_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__are_equal(const sim_interfaces__srv__TrajectoryInfo_Response__Sequence * lhs, const sim_interfaces__srv__TrajectoryInfo_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__srv__TrajectoryInfo_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__srv__TrajectoryInfo_Response__Sequence__copy(
  const sim_interfaces__srv__TrajectoryInfo_Response__Sequence * input,
  sim_interfaces__srv__TrajectoryInfo_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__srv__TrajectoryInfo_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__srv__TrajectoryInfo_Response * data =
      (sim_interfaces__srv__TrajectoryInfo_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__srv__TrajectoryInfo_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__srv__TrajectoryInfo_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__srv__TrajectoryInfo_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
