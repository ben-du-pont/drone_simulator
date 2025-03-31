// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sim_interfaces:msg/StampedFloat.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sim_interfaces/msg/detail/stamped_float__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sim_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void StampedFloat_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sim_interfaces::msg::StampedFloat(_init);
}

void StampedFloat_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sim_interfaces::msg::StampedFloat *>(message_memory);
  typed_message->~StampedFloat();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember StampedFloat_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::StampedFloat, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "data",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::StampedFloat, data),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers StampedFloat_message_members = {
  "sim_interfaces::msg",  // message namespace
  "StampedFloat",  // message name
  2,  // number of fields
  sizeof(sim_interfaces::msg::StampedFloat),
  StampedFloat_message_member_array,  // message members
  StampedFloat_init_function,  // function to initialize message memory (memory has to be allocated)
  StampedFloat_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t StampedFloat_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &StampedFloat_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace sim_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sim_interfaces::msg::StampedFloat>()
{
  return &::sim_interfaces::msg::rosidl_typesupport_introspection_cpp::StampedFloat_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sim_interfaces, msg, StampedFloat)() {
  return &::sim_interfaces::msg::rosidl_typesupport_introspection_cpp::StampedFloat_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
