// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_interfaces/msg/detail/anchor_errors__rosidl_typesupport_introspection_c.h"
#include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_interfaces/msg/detail/anchor_errors__functions.h"
#include "sim_interfaces/msg/detail/anchor_errors__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `anchor_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `linear_error`
// Member `nonlinear_error`
// Member `final_error`
#include "sim_interfaces/msg/anchor_error.h"
// Member `linear_error`
// Member `nonlinear_error`
// Member `final_error`
#include "sim_interfaces/msg/detail/anchor_error__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__msg__AnchorErrors__init(message_memory);
}

void sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_fini_function(void * message_memory)
{
  sim_interfaces__msg__AnchorErrors__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array[5] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__AnchorErrors, header),  // bytes offset in struct
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
    offsetof(sim_interfaces__msg__AnchorErrors, anchor_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "linear_error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__AnchorErrors, linear_error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "nonlinear_error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__AnchorErrors, nonlinear_error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "final_error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__msg__AnchorErrors, final_error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_members = {
  "sim_interfaces__msg",  // message namespace
  "AnchorErrors",  // message name
  5,  // number of fields
  sizeof(sim_interfaces__msg__AnchorErrors),
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array,  // message members
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_type_support_handle = {
  0,
  &sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, AnchorErrors)() {
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, AnchorError)();
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, AnchorError)();
  sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, msg, AnchorError)();
  if (!sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__msg__AnchorErrors__rosidl_typesupport_introspection_c__AnchorErrors_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
