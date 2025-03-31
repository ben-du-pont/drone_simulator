// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_interfaces:msg/OptimizedTrajectory.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_interfaces/msg/detail/optimized_trajectory__rosidl_typesupport_introspection_c.h"
#include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_interfaces/msg/detail/optimized_trajectory__functions.h"
#include "sim_interfaces/msg/detail/optimized_trajectory__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `anchor_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `waypoint_x`
// Member `waypoint_y`
// Member `waypoint_z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__msg__OptimizedTrajectory__init(message_memory);
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_fini_function(void * message_memory)
{
  sim_interfaces__msg__OptimizedTrajectory__fini(message_memory);
}

size_t sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_x(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_x(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_x(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_y(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_y(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_y(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_z(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_z(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_z(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_z(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_z(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_z(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_member_array[6] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "anchor_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, anchor_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "waypoint_count",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, waypoint_count),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "waypoint_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, waypoint_x),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_x,  // size() function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_x,  // get_const(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_x,  // get(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_x,  // fetch(index, &value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_x,  // assign(index, value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_x  // resize(index) function pointer
  },
  {
    "waypoint_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, waypoint_y),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_y,  // size() function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_y,  // get_const(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_y,  // get(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_y,  // fetch(index, &value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_y,  // assign(index, value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_y  // resize(index) function pointer
  },
  {
    "waypoint_z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__OptimizedTrajectory, waypoint_z),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__size_function__OptimizedTrajectory__waypoint_z,  // size() function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_const_function__OptimizedTrajectory__waypoint_z,  // get_const(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__get_function__OptimizedTrajectory__waypoint_z,  // get(index) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__fetch_function__OptimizedTrajectory__waypoint_z,  // fetch(index, &value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__assign_function__OptimizedTrajectory__waypoint_z,  // assign(index, value) function pointer
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__resize_function__OptimizedTrajectory__waypoint_z  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_members = {
  "sim_interfaces__msg",  // message namespace
  "OptimizedTrajectory",  // message name
  6,  // number of fields
  sizeof(sim_interfaces__msg__OptimizedTrajectory),
  sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_member_array,  // message members
  sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_type_support_handle = {
  0,
  &sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, OptimizedTrajectory)() {
  sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__msg__OptimizedTrajectory__rosidl_typesupport_introspection_c__OptimizedTrajectory_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
