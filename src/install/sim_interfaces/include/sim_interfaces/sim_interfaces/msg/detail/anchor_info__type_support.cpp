// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sim_interfaces:msg/AnchorInfo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sim_interfaces/msg/detail/anchor_info__struct.hpp"
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

void AnchorInfo_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sim_interfaces::msg::AnchorInfo(_init);
}

void AnchorInfo_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sim_interfaces::msg::AnchorInfo *>(message_memory);
  typed_message->~AnchorInfo();
}

size_t size_function__AnchorInfo__ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__AnchorInfo__ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__AnchorInfo__ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__x(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__x(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__x(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo__x(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo__x(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__x(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__y(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__y(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__y(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo__y(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo__y(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__y(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__z(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__z(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__z(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo__z(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo__z(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__z(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__constant_bias(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__constant_bias(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__constant_bias(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__constant_bias(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo__constant_bias(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__constant_bias(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo__constant_bias(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__constant_bias(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__linear_bias(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__linear_bias(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__linear_bias(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__linear_bias(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo__linear_bias(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__linear_bias(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo__linear_bias(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__linear_bias(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo__types(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo__types(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo__types(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo__types(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__AnchorInfo__types(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo__types(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__AnchorInfo__types(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo__types(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember AnchorInfo_message_member_array[9] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "count",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, count),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__ids,  // size() function pointer
    get_const_function__AnchorInfo__ids,  // get_const(index) function pointer
    get_function__AnchorInfo__ids,  // get(index) function pointer
    fetch_function__AnchorInfo__ids,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__ids,  // assign(index, value) function pointer
    resize_function__AnchorInfo__ids  // resize(index) function pointer
  },
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, x),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__x,  // size() function pointer
    get_const_function__AnchorInfo__x,  // get_const(index) function pointer
    get_function__AnchorInfo__x,  // get(index) function pointer
    fetch_function__AnchorInfo__x,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__x,  // assign(index, value) function pointer
    resize_function__AnchorInfo__x  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, y),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__y,  // size() function pointer
    get_const_function__AnchorInfo__y,  // get_const(index) function pointer
    get_function__AnchorInfo__y,  // get(index) function pointer
    fetch_function__AnchorInfo__y,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__y,  // assign(index, value) function pointer
    resize_function__AnchorInfo__y  // resize(index) function pointer
  },
  {
    "z",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, z),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__z,  // size() function pointer
    get_const_function__AnchorInfo__z,  // get_const(index) function pointer
    get_function__AnchorInfo__z,  // get(index) function pointer
    fetch_function__AnchorInfo__z,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__z,  // assign(index, value) function pointer
    resize_function__AnchorInfo__z  // resize(index) function pointer
  },
  {
    "constant_bias",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, constant_bias),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__constant_bias,  // size() function pointer
    get_const_function__AnchorInfo__constant_bias,  // get_const(index) function pointer
    get_function__AnchorInfo__constant_bias,  // get(index) function pointer
    fetch_function__AnchorInfo__constant_bias,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__constant_bias,  // assign(index, value) function pointer
    resize_function__AnchorInfo__constant_bias  // resize(index) function pointer
  },
  {
    "linear_bias",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, linear_bias),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__linear_bias,  // size() function pointer
    get_const_function__AnchorInfo__linear_bias,  // get_const(index) function pointer
    get_function__AnchorInfo__linear_bias,  // get(index) function pointer
    fetch_function__AnchorInfo__linear_bias,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__linear_bias,  // assign(index, value) function pointer
    resize_function__AnchorInfo__linear_bias  // resize(index) function pointer
  },
  {
    "types",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::msg::AnchorInfo, types),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo__types,  // size() function pointer
    get_const_function__AnchorInfo__types,  // get_const(index) function pointer
    get_function__AnchorInfo__types,  // get(index) function pointer
    fetch_function__AnchorInfo__types,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo__types,  // assign(index, value) function pointer
    resize_function__AnchorInfo__types  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers AnchorInfo_message_members = {
  "sim_interfaces::msg",  // message namespace
  "AnchorInfo",  // message name
  9,  // number of fields
  sizeof(sim_interfaces::msg::AnchorInfo),
  AnchorInfo_message_member_array,  // message members
  AnchorInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  AnchorInfo_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t AnchorInfo_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AnchorInfo_message_members,
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
get_message_type_support_handle<sim_interfaces::msg::AnchorInfo>()
{
  return &::sim_interfaces::msg::rosidl_typesupport_introspection_cpp::AnchorInfo_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sim_interfaces, msg, AnchorInfo)() {
  return &::sim_interfaces::msg::rosidl_typesupport_introspection_cpp::AnchorInfo_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
