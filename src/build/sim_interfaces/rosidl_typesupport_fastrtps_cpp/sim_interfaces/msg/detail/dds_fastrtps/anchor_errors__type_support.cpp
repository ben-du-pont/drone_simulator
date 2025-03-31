// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_errors__rosidl_typesupport_fastrtps_cpp.hpp"
#include "sim_interfaces/msg/detail/anchor_errors__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::Header &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::Header &);
size_t get_serialized_size(
  const std_msgs::msg::Header &,
  size_t current_alignment);
size_t
max_serialized_size_Header(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace sim_interfaces
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const sim_interfaces::msg::AnchorError &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  sim_interfaces::msg::AnchorError &);
size_t get_serialized_size(
  const sim_interfaces::msg::AnchorError &,
  size_t current_alignment);
size_t
max_serialized_size_AnchorError(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace sim_interfaces

// functions for sim_interfaces::msg::AnchorError already declared above

// functions for sim_interfaces::msg::AnchorError already declared above


namespace sim_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sim_interfaces
cdr_serialize(
  const sim_interfaces::msg::AnchorErrors & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: anchor_id
  cdr << ros_message.anchor_id;
  // Member: linear_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.linear_error,
    cdr);
  // Member: nonlinear_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.nonlinear_error,
    cdr);
  // Member: final_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.final_error,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sim_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sim_interfaces::msg::AnchorErrors & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: anchor_id
  cdr >> ros_message.anchor_id;

  // Member: linear_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.linear_error);

  // Member: nonlinear_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.nonlinear_error);

  // Member: final_error
  sim_interfaces::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.final_error);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sim_interfaces
get_serialized_size(
  const sim_interfaces::msg::AnchorErrors & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: header

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.header, current_alignment);
  // Member: anchor_id
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.anchor_id.size() + 1);
  // Member: linear_error

  current_alignment +=
    sim_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.linear_error, current_alignment);
  // Member: nonlinear_error

  current_alignment +=
    sim_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.nonlinear_error, current_alignment);
  // Member: final_error

  current_alignment +=
    sim_interfaces::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.final_error, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sim_interfaces
max_serialized_size_AnchorErrors(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: header
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_Header(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: anchor_id
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: linear_error
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        sim_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_AnchorError(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: nonlinear_error
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        sim_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_AnchorError(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: final_error
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        sim_interfaces::msg::typesupport_fastrtps_cpp::max_serialized_size_AnchorError(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = sim_interfaces::msg::AnchorErrors;
    is_plain =
      (
      offsetof(DataType, final_error) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _AnchorErrors__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const sim_interfaces::msg::AnchorErrors *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _AnchorErrors__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<sim_interfaces::msg::AnchorErrors *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _AnchorErrors__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const sim_interfaces::msg::AnchorErrors *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _AnchorErrors__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_AnchorErrors(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _AnchorErrors__callbacks = {
  "sim_interfaces::msg",
  "AnchorErrors",
  _AnchorErrors__cdr_serialize,
  _AnchorErrors__cdr_deserialize,
  _AnchorErrors__get_serialized_size,
  _AnchorErrors__max_serialized_size
};

static rosidl_message_type_support_t _AnchorErrors__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_AnchorErrors__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sim_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<sim_interfaces::msg::AnchorErrors>()
{
  return &sim_interfaces::msg::typesupport_fastrtps_cpp::_AnchorErrors__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sim_interfaces, msg, AnchorErrors)() {
  return &sim_interfaces::msg::typesupport_fastrtps_cpp::_AnchorErrors__handle;
}

#ifdef __cplusplus
}
#endif
