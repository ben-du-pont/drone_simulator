// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/msg/detail/anchor_estimates__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "sim_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "sim_interfaces/msg/detail/anchor_estimates__struct.h"
#include "sim_interfaces/msg/detail/anchor_estimates__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // anchor_id
#include "rosidl_runtime_c/string_functions.h"  // anchor_id
#include "sim_interfaces/msg/detail/anchor_estimate__functions.h"  // final_estimate, linear_estimate, refined_estimate
#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
size_t get_serialized_size_sim_interfaces__msg__AnchorEstimate(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_sim_interfaces__msg__AnchorEstimate(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate)();
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_sim_interfaces
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_sim_interfaces
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_sim_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _AnchorEstimates__ros_msg_type = sim_interfaces__msg__AnchorEstimates;

static bool _AnchorEstimates__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AnchorEstimates__ros_msg_type * ros_message = static_cast<const _AnchorEstimates__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: anchor_id
  {
    const rosidl_runtime_c__String * str = &ros_message->anchor_id;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: linear_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->linear_estimate, cdr))
    {
      return false;
    }
  }

  // Field name: refined_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->refined_estimate, cdr))
    {
      return false;
    }
  }

  // Field name: final_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->final_estimate, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _AnchorEstimates__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AnchorEstimates__ros_msg_type * ros_message = static_cast<_AnchorEstimates__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: anchor_id
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->anchor_id.data) {
      rosidl_runtime_c__String__init(&ros_message->anchor_id);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->anchor_id,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'anchor_id'\n");
      return false;
    }
  }

  // Field name: linear_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->linear_estimate))
    {
      return false;
    }
  }

  // Field name: refined_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->refined_estimate))
    {
      return false;
    }
  }

  // Field name: final_estimate
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimate
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->final_estimate))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t get_serialized_size_sim_interfaces__msg__AnchorEstimates(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AnchorEstimates__ros_msg_type * ros_message = static_cast<const _AnchorEstimates__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name anchor_id
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->anchor_id.size + 1);
  // field.name linear_estimate

  current_alignment += get_serialized_size_sim_interfaces__msg__AnchorEstimate(
    &(ros_message->linear_estimate), current_alignment);
  // field.name refined_estimate

  current_alignment += get_serialized_size_sim_interfaces__msg__AnchorEstimate(
    &(ros_message->refined_estimate), current_alignment);
  // field.name final_estimate

  current_alignment += get_serialized_size_sim_interfaces__msg__AnchorEstimate(
    &(ros_message->final_estimate), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _AnchorEstimates__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sim_interfaces__msg__AnchorEstimates(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t max_serialized_size_sim_interfaces__msg__AnchorEstimates(
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

  // member: header
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_std_msgs__msg__Header(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: anchor_id
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
  // member: linear_estimate
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_sim_interfaces__msg__AnchorEstimate(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: refined_estimate
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_sim_interfaces__msg__AnchorEstimate(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: final_estimate
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_sim_interfaces__msg__AnchorEstimate(
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
    using DataType = sim_interfaces__msg__AnchorEstimates;
    is_plain =
      (
      offsetof(DataType, final_estimate) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AnchorEstimates__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_sim_interfaces__msg__AnchorEstimates(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AnchorEstimates = {
  "sim_interfaces::msg",
  "AnchorEstimates",
  _AnchorEstimates__cdr_serialize,
  _AnchorEstimates__cdr_deserialize,
  _AnchorEstimates__get_serialized_size,
  _AnchorEstimates__max_serialized_size
};

static rosidl_message_type_support_t _AnchorEstimates__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AnchorEstimates,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, msg, AnchorEstimates)() {
  return &_AnchorEstimates__type_support;
}

#if defined(__cplusplus)
}
#endif
