// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sim_interfaces/srv/detail/anchor_info__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sim_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void AnchorInfo_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sim_interfaces::srv::AnchorInfo_Request(_init);
}

void AnchorInfo_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sim_interfaces::srv::AnchorInfo_Request *>(message_memory);
  typed_message->~AnchorInfo_Request();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember AnchorInfo_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers AnchorInfo_Request_message_members = {
  "sim_interfaces::srv",  // message namespace
  "AnchorInfo_Request",  // message name
  1,  // number of fields
  sizeof(sim_interfaces::srv::AnchorInfo_Request),
  AnchorInfo_Request_message_member_array,  // message members
  AnchorInfo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  AnchorInfo_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t AnchorInfo_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AnchorInfo_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace sim_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sim_interfaces::srv::AnchorInfo_Request>()
{
  return &::sim_interfaces::srv::rosidl_typesupport_introspection_cpp::AnchorInfo_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sim_interfaces, srv, AnchorInfo_Request)() {
  return &::sim_interfaces::srv::rosidl_typesupport_introspection_cpp::AnchorInfo_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sim_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void AnchorInfo_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sim_interfaces::srv::AnchorInfo_Response(_init);
}

void AnchorInfo_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sim_interfaces::srv::AnchorInfo_Response *>(message_memory);
  typed_message->~AnchorInfo_Response();
}

size_t size_function__AnchorInfo_Response__known_anchor_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__AnchorInfo_Response__known_anchor_ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__AnchorInfo_Response__known_anchor_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_x_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_x_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_x_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_x_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_x_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_x_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_x_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_x_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_y_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_y_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_y_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_y_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_y_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_y_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_y_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_y_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_z_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_z_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_z_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_z_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_z_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_z_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_z_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_z_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_biases(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_biases(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_biases(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_biases(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_biases(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_biases(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_linear_biases(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_linear_biases(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_linear_biases(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_linear_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_linear_biases(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_linear_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_linear_biases(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_linear_biases(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__known_anchor_noise_variances(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__known_anchor_noise_variances(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__known_anchor_noise_variances(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__known_anchor_noise_variances(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__known_anchor_noise_variances(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__known_anchor_noise_variances(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__known_anchor_noise_variances(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__known_anchor_noise_variances(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__AnchorInfo_Response__unknown_anchor_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_x_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_x_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_x_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_x_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_x_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_x_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_x_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_x_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_y_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_y_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_y_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_y_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_y_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_y_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_y_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_y_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_z_positions(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_z_positions(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_z_positions(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_z_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_z_positions(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_z_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_z_positions(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_z_positions(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_biases(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_biases(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_biases(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_biases(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_biases(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_biases(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_linear_biases(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_linear_biases(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_linear_biases(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_linear_biases(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AnchorInfo_Response__unknown_anchor_noise_variances(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__AnchorInfo_Response__unknown_anchor_noise_variances(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__AnchorInfo_Response__unknown_anchor_noise_variances(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__AnchorInfo_Response__unknown_anchor_noise_variances(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember AnchorInfo_Response_message_member_array[14] = {
  {
    "known_anchor_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_ids,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_ids,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_ids,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_ids,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_ids,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_ids  // resize(index) function pointer
  },
  {
    "known_anchor_x_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_x_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_x_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_x_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_x_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_x_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_x_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_x_positions  // resize(index) function pointer
  },
  {
    "known_anchor_y_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_y_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_y_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_y_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_y_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_y_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_y_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_y_positions  // resize(index) function pointer
  },
  {
    "known_anchor_z_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_z_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_z_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_z_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_z_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_z_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_z_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_z_positions  // resize(index) function pointer
  },
  {
    "known_anchor_biases",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_biases),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_biases,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_biases,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_biases,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_biases,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_biases,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_biases  // resize(index) function pointer
  },
  {
    "known_anchor_linear_biases",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_linear_biases),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_linear_biases,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_linear_biases,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_linear_biases,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_linear_biases,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_linear_biases,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_linear_biases  // resize(index) function pointer
  },
  {
    "known_anchor_noise_variances",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, known_anchor_noise_variances),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__known_anchor_noise_variances,  // size() function pointer
    get_const_function__AnchorInfo_Response__known_anchor_noise_variances,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__known_anchor_noise_variances,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__known_anchor_noise_variances,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__known_anchor_noise_variances,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__known_anchor_noise_variances  // resize(index) function pointer
  },
  {
    "unknown_anchor_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_ids,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_ids,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_ids,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_ids,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_ids,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_ids  // resize(index) function pointer
  },
  {
    "unknown_anchor_x_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_x_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_x_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_x_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_x_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_x_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_x_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_x_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_y_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_y_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_y_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_y_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_y_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_y_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_y_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_y_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_z_positions",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_z_positions),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_z_positions,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_z_positions,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_z_positions,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_z_positions,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_z_positions,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_z_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_biases",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_biases),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_biases,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_biases,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_biases,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_biases,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_biases,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_biases  // resize(index) function pointer
  },
  {
    "unknown_anchor_linear_biases",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_linear_biases),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_linear_biases  // resize(index) function pointer
  },
  {
    "unknown_anchor_noise_variances",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces::srv::AnchorInfo_Response, unknown_anchor_noise_variances),  // bytes offset in struct
    nullptr,  // default value
    size_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // size() function pointer
    get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // get_const(index) function pointer
    get_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // get(index) function pointer
    fetch_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // fetch(index, &value) function pointer
    assign_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // assign(index, value) function pointer
    resize_function__AnchorInfo_Response__unknown_anchor_noise_variances  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers AnchorInfo_Response_message_members = {
  "sim_interfaces::srv",  // message namespace
  "AnchorInfo_Response",  // message name
  14,  // number of fields
  sizeof(sim_interfaces::srv::AnchorInfo_Response),
  AnchorInfo_Response_message_member_array,  // message members
  AnchorInfo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  AnchorInfo_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t AnchorInfo_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AnchorInfo_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace sim_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sim_interfaces::srv::AnchorInfo_Response>()
{
  return &::sim_interfaces::srv::rosidl_typesupport_introspection_cpp::AnchorInfo_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sim_interfaces, srv, AnchorInfo_Response)() {
  return &::sim_interfaces::srv::rosidl_typesupport_introspection_cpp::AnchorInfo_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace sim_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers AnchorInfo_service_members = {
  "sim_interfaces::srv",  // service namespace
  "AnchorInfo",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<sim_interfaces::srv::AnchorInfo>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t AnchorInfo_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AnchorInfo_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace sim_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<sim_interfaces::srv::AnchorInfo>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::sim_interfaces::srv::rosidl_typesupport_introspection_cpp::AnchorInfo_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::sim_interfaces::srv::AnchorInfo_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::sim_interfaces::srv::AnchorInfo_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sim_interfaces, srv, AnchorInfo)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<sim_interfaces::srv::AnchorInfo>();
}

#ifdef __cplusplus
}
#endif
