// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/waypoint_lists__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `reached`
// Member `remaining`
#include "sim_interfaces/msg/detail/waypoint_list__functions.h"

bool
sim_interfaces__msg__WaypointLists__init(sim_interfaces__msg__WaypointLists * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__WaypointLists__fini(msg);
    return false;
  }
  // reached
  if (!sim_interfaces__msg__WaypointList__init(&msg->reached)) {
    sim_interfaces__msg__WaypointLists__fini(msg);
    return false;
  }
  // remaining
  if (!sim_interfaces__msg__WaypointList__init(&msg->remaining)) {
    sim_interfaces__msg__WaypointLists__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__msg__WaypointLists__fini(sim_interfaces__msg__WaypointLists * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // reached
  sim_interfaces__msg__WaypointList__fini(&msg->reached);
  // remaining
  sim_interfaces__msg__WaypointList__fini(&msg->remaining);
}

bool
sim_interfaces__msg__WaypointLists__are_equal(const sim_interfaces__msg__WaypointLists * lhs, const sim_interfaces__msg__WaypointLists * rhs)
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
  // reached
  if (!sim_interfaces__msg__WaypointList__are_equal(
      &(lhs->reached), &(rhs->reached)))
  {
    return false;
  }
  // remaining
  if (!sim_interfaces__msg__WaypointList__are_equal(
      &(lhs->remaining), &(rhs->remaining)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__WaypointLists__copy(
  const sim_interfaces__msg__WaypointLists * input,
  sim_interfaces__msg__WaypointLists * output)
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
  // reached
  if (!sim_interfaces__msg__WaypointList__copy(
      &(input->reached), &(output->reached)))
  {
    return false;
  }
  // remaining
  if (!sim_interfaces__msg__WaypointList__copy(
      &(input->remaining), &(output->remaining)))
  {
    return false;
  }
  return true;
}

sim_interfaces__msg__WaypointLists *
sim_interfaces__msg__WaypointLists__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__WaypointLists * msg = (sim_interfaces__msg__WaypointLists *)allocator.allocate(sizeof(sim_interfaces__msg__WaypointLists), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__WaypointLists));
  bool success = sim_interfaces__msg__WaypointLists__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__WaypointLists__destroy(sim_interfaces__msg__WaypointLists * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__WaypointLists__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__WaypointLists__Sequence__init(sim_interfaces__msg__WaypointLists__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__WaypointLists * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__WaypointLists *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__WaypointLists), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__WaypointLists__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__WaypointLists__fini(&data[i - 1]);
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
sim_interfaces__msg__WaypointLists__Sequence__fini(sim_interfaces__msg__WaypointLists__Sequence * array)
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
      sim_interfaces__msg__WaypointLists__fini(&array->data[i]);
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

sim_interfaces__msg__WaypointLists__Sequence *
sim_interfaces__msg__WaypointLists__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__WaypointLists__Sequence * array = (sim_interfaces__msg__WaypointLists__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__WaypointLists__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__WaypointLists__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__WaypointLists__Sequence__destroy(sim_interfaces__msg__WaypointLists__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__WaypointLists__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__WaypointLists__Sequence__are_equal(const sim_interfaces__msg__WaypointLists__Sequence * lhs, const sim_interfaces__msg__WaypointLists__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__WaypointLists__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__WaypointLists__Sequence__copy(
  const sim_interfaces__msg__WaypointLists__Sequence * input,
  sim_interfaces__msg__WaypointLists__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__WaypointLists);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__WaypointLists * data =
      (sim_interfaces__msg__WaypointLists *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__WaypointLists__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__WaypointLists__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__WaypointLists__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
