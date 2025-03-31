// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_interfaces:msg/WaypointList.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_interfaces/msg/detail/waypoint_list__rosidl_typesupport_introspection_c.h"
#include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_interfaces/msg/detail/waypoint_list__functions.h"
#include "sim_interfaces/msg/detail/waypoint_list__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `x`
// Member `y`
// Member `z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__msg__WaypointList__init(message_memory);
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_fini_function(void * message_memory)
{
  sim_interfaces__msg__WaypointList__fini(message_memory);
}

size_t sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__x(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__x(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__x(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__y(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__y(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__y(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__z(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__z(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__z(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__z(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__z(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__z(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_member_array[5] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__WaypointList, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "count",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__WaypointList, count),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__WaypointList, x),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__x,  // size() function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__x,  // get_const(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__x,  // get(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__x,  // fetch(index, &value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__x,  // assign(index, value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__x  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__WaypointList, y),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__y,  // size() function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__y,  // get_const(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__y,  // get(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__y,  // fetch(index, &value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__y,  // assign(index, value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__y  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__WaypointList, z),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__size_function__WaypointList__z,  // size() function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_const_function__WaypointList__z,  // get_const(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__get_function__WaypointList__z,  // get(index) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__fetch_function__WaypointList__z,  // fetch(index, &value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__assign_function__WaypointList__z,  // assign(index, value) function pointer
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__resize_function__WaypointList__z  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_members = {
  "sim_interfaces__msg",  // message namespace
  "WaypointList",  // message name
  5,  // number of fields
  sizeof(sim_interfaces__msg__WaypointList),
  sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_member_array,  // message members
  sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_type_support_handle = {
  0,
  &sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, WaypointList)() {
  sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__msg__WaypointList__rosidl_typesupport_introspection_c__WaypointList_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
