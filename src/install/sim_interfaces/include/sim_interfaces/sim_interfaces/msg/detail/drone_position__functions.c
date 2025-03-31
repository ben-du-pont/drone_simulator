// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/DronePosition.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/drone_position__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
sim_interfaces__msg__DronePosition__init(sim_interfaces__msg__DronePosition * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__DronePosition__fini(msg);
    return false;
  }
  // position_x
  // position_y
  // position_z
  // waypoints_achieved
  // total_waypoints
  return true;
}

void
sim_interfaces__msg__DronePosition__fini(sim_interfaces__msg__DronePosition * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // position_x
  // position_y
  // position_z
  // waypoints_achieved
  // total_waypoints
}

bool
sim_interfaces__msg__DronePosition__are_equal(const sim_interfaces__msg__DronePosition * lhs, const sim_interfaces__msg__DronePosition * rhs)
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
  // waypoints_achieved
  if (lhs->waypoints_achieved != rhs->waypoints_achieved) {
    return false;
  }
  // total_waypoints
  if (lhs->total_waypoints != rhs->total_waypoints) {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__DronePosition__copy(
  const sim_interfaces__msg__DronePosition * input,
  sim_interfaces__msg__DronePosition * output)
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
  // position_x
  output->position_x = input->position_x;
  // position_y
  output->position_y = input->position_y;
  // position_z
  output->position_z = input->position_z;
  // waypoints_achieved
  output->waypoints_achieved = input->waypoints_achieved;
  // total_waypoints
  output->total_waypoints = input->total_waypoints;
  return true;
}

sim_interfaces__msg__DronePosition *
sim_interfaces__msg__DronePosition__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__DronePosition * msg = (sim_interfaces__msg__DronePosition *)allocator.allocate(sizeof(sim_interfaces__msg__DronePosition), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__DronePosition));
  bool success = sim_interfaces__msg__DronePosition__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__DronePosition__destroy(sim_interfaces__msg__DronePosition * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__DronePosition__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__DronePosition__Sequence__init(sim_interfaces__msg__DronePosition__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__DronePosition * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__DronePosition *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__DronePosition), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__DronePosition__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__DronePosition__fini(&data[i - 1]);
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
sim_interfaces__msg__DronePosition__Sequence__fini(sim_interfaces__msg__DronePosition__Sequence * array)
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
      sim_interfaces__msg__DronePosition__fini(&array->data[i]);
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

sim_interfaces__msg__DronePosition__Sequence *
sim_interfaces__msg__DronePosition__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__DronePosition__Sequence * array = (sim_interfaces__msg__DronePosition__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__DronePosition__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__DronePosition__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__DronePosition__Sequence__destroy(sim_interfaces__msg__DronePosition__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__DronePosition__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__DronePosition__Sequence__are_equal(const sim_interfaces__msg__DronePosition__Sequence * lhs, const sim_interfaces__msg__DronePosition__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__DronePosition__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__DronePosition__Sequence__copy(
  const sim_interfaces__msg__DronePosition__Sequence * input,
  sim_interfaces__msg__DronePosition__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__DronePosition);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__DronePosition * data =
      (sim_interfaces__msg__DronePosition *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__DronePosition__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__DronePosition__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__DronePosition__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
