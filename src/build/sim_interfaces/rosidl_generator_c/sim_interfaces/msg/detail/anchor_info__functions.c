// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_interfaces:msg/AnchorInfo.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `ids`
#include "rosidl_runtime_c/string_functions.h"
// Member `x`
// Member `y`
// Member `z`
// Member `constant_bias`
// Member `linear_bias`
// Member `types`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
sim_interfaces__msg__AnchorInfo__init(sim_interfaces__msg__AnchorInfo * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // count
  // ids
  if (!rosidl_runtime_c__String__Sequence__init(&msg->ids, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__init(&msg->x, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__init(&msg->y, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // z
  if (!rosidl_runtime_c__double__Sequence__init(&msg->z, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // constant_bias
  if (!rosidl_runtime_c__double__Sequence__init(&msg->constant_bias, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // linear_bias
  if (!rosidl_runtime_c__double__Sequence__init(&msg->linear_bias, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  // types
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->types, 0)) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
    return false;
  }
  return true;
}

void
sim_interfaces__msg__AnchorInfo__fini(sim_interfaces__msg__AnchorInfo * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // count
  // ids
  rosidl_runtime_c__String__Sequence__fini(&msg->ids);
  // x
  rosidl_runtime_c__double__Sequence__fini(&msg->x);
  // y
  rosidl_runtime_c__double__Sequence__fini(&msg->y);
  // z
  rosidl_runtime_c__double__Sequence__fini(&msg->z);
  // constant_bias
  rosidl_runtime_c__double__Sequence__fini(&msg->constant_bias);
  // linear_bias
  rosidl_runtime_c__double__Sequence__fini(&msg->linear_bias);
  // types
  rosidl_runtime_c__int32__Sequence__fini(&msg->types);
}

bool
sim_interfaces__msg__AnchorInfo__are_equal(const sim_interfaces__msg__AnchorInfo * lhs, const sim_interfaces__msg__AnchorInfo * rhs)
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
  // count
  if (lhs->count != rhs->count) {
    return false;
  }
  // ids
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->ids), &(rhs->ids)))
  {
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->x), &(rhs->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->y), &(rhs->y)))
  {
    return false;
  }
  // z
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->z), &(rhs->z)))
  {
    return false;
  }
  // constant_bias
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->constant_bias), &(rhs->constant_bias)))
  {
    return false;
  }
  // linear_bias
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->linear_bias), &(rhs->linear_bias)))
  {
    return false;
  }
  // types
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->types), &(rhs->types)))
  {
    return false;
  }
  return true;
}

bool
sim_interfaces__msg__AnchorInfo__copy(
  const sim_interfaces__msg__AnchorInfo * input,
  sim_interfaces__msg__AnchorInfo * output)
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
  // count
  output->count = input->count;
  // ids
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->ids), &(output->ids)))
  {
    return false;
  }
  // x
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->x), &(output->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->y), &(output->y)))
  {
    return false;
  }
  // z
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->z), &(output->z)))
  {
    return false;
  }
  // constant_bias
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->constant_bias), &(output->constant_bias)))
  {
    return false;
  }
  // linear_bias
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->linear_bias), &(output->linear_bias)))
  {
    return false;
  }
  // types
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->types), &(output->types)))
  {
    return false;
  }
  return true;
}

sim_interfaces__msg__AnchorInfo *
sim_interfaces__msg__AnchorInfo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorInfo * msg = (sim_interfaces__msg__AnchorInfo *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_interfaces__msg__AnchorInfo));
  bool success = sim_interfaces__msg__AnchorInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_interfaces__msg__AnchorInfo__destroy(sim_interfaces__msg__AnchorInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_interfaces__msg__AnchorInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_interfaces__msg__AnchorInfo__Sequence__init(sim_interfaces__msg__AnchorInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorInfo * data = NULL;

  if (size) {
    data = (sim_interfaces__msg__AnchorInfo *)allocator.zero_allocate(size, sizeof(sim_interfaces__msg__AnchorInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_interfaces__msg__AnchorInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_interfaces__msg__AnchorInfo__fini(&data[i - 1]);
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
sim_interfaces__msg__AnchorInfo__Sequence__fini(sim_interfaces__msg__AnchorInfo__Sequence * array)
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
      sim_interfaces__msg__AnchorInfo__fini(&array->data[i]);
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

sim_interfaces__msg__AnchorInfo__Sequence *
sim_interfaces__msg__AnchorInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_interfaces__msg__AnchorInfo__Sequence * array = (sim_interfaces__msg__AnchorInfo__Sequence *)allocator.allocate(sizeof(sim_interfaces__msg__AnchorInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_interfaces__msg__AnchorInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_interfaces__msg__AnchorInfo__Sequence__destroy(sim_interfaces__msg__AnchorInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_interfaces__msg__AnchorInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_interfaces__msg__AnchorInfo__Sequence__are_equal(const sim_interfaces__msg__AnchorInfo__Sequence * lhs, const sim_interfaces__msg__AnchorInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_interfaces__msg__AnchorInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_interfaces__msg__AnchorInfo__Sequence__copy(
  const sim_interfaces__msg__AnchorInfo__Sequence * input,
  sim_interfaces__msg__AnchorInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_interfaces__msg__AnchorInfo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_interfaces__msg__AnchorInfo * data =
      (sim_interfaces__msg__AnchorInfo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_interfaces__msg__AnchorInfo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_interfaces__msg__AnchorInfo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_interfaces__msg__AnchorInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
