// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/srv/detail/anchor_info__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "sim_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "sim_interfaces/srv/detail/anchor_info__struct.h"
#include "sim_interfaces/srv/detail/anchor_info__functions.h"
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


// forward declare type support functions


using _AnchorInfo_Request__ros_msg_type = sim_interfaces__srv__AnchorInfo_Request;

static bool _AnchorInfo_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AnchorInfo_Request__ros_msg_type * ros_message = static_cast<const _AnchorInfo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr << ros_message->structure_needs_at_least_one_member;
  }

  return true;
}

static bool _AnchorInfo_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AnchorInfo_Request__ros_msg_type * ros_message = static_cast<_AnchorInfo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr >> ros_message->structure_needs_at_least_one_member;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t get_serialized_size_sim_interfaces__srv__AnchorInfo_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AnchorInfo_Request__ros_msg_type * ros_message = static_cast<const _AnchorInfo_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name structure_needs_at_least_one_member
  {
    size_t item_size = sizeof(ros_message->structure_needs_at_least_one_member);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AnchorInfo_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sim_interfaces__srv__AnchorInfo_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t max_serialized_size_sim_interfaces__srv__AnchorInfo_Request(
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

  // member: structure_needs_at_least_one_member
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = sim_interfaces__srv__AnchorInfo_Request;
    is_plain =
      (
      offsetof(DataType, structure_needs_at_least_one_member) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AnchorInfo_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_sim_interfaces__srv__AnchorInfo_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AnchorInfo_Request = {
  "sim_interfaces::srv",
  "AnchorInfo_Request",
  _AnchorInfo_Request__cdr_serialize,
  _AnchorInfo_Request__cdr_deserialize,
  _AnchorInfo_Request__get_serialized_size,
  _AnchorInfo_Request__max_serialized_size
};

static rosidl_message_type_support_t _AnchorInfo_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AnchorInfo_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, AnchorInfo_Request)() {
  return &_AnchorInfo_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__struct.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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

#include "rosidl_runtime_c/primitives_sequence.h"  // known_anchor_biases, known_anchor_linear_biases, known_anchor_noise_variances, known_anchor_x_positions, known_anchor_y_positions, known_anchor_z_positions, unknown_anchor_biases, unknown_anchor_linear_biases, unknown_anchor_noise_variances, unknown_anchor_x_positions, unknown_anchor_y_positions, unknown_anchor_z_positions
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // known_anchor_biases, known_anchor_linear_biases, known_anchor_noise_variances, known_anchor_x_positions, known_anchor_y_positions, known_anchor_z_positions, unknown_anchor_biases, unknown_anchor_linear_biases, unknown_anchor_noise_variances, unknown_anchor_x_positions, unknown_anchor_y_positions, unknown_anchor_z_positions
#include "rosidl_runtime_c/string.h"  // known_anchor_ids, unknown_anchor_ids
#include "rosidl_runtime_c/string_functions.h"  // known_anchor_ids, unknown_anchor_ids

// forward declare type support functions


using _AnchorInfo_Response__ros_msg_type = sim_interfaces__srv__AnchorInfo_Response;

static bool _AnchorInfo_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AnchorInfo_Response__ros_msg_type * ros_message = static_cast<const _AnchorInfo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: known_anchor_ids
  {
    size_t size = ros_message->known_anchor_ids.size;
    auto array_ptr = ros_message->known_anchor_ids.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
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
  }

  // Field name: known_anchor_x_positions
  {
    size_t size = ros_message->known_anchor_x_positions.size;
    auto array_ptr = ros_message->known_anchor_x_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: known_anchor_y_positions
  {
    size_t size = ros_message->known_anchor_y_positions.size;
    auto array_ptr = ros_message->known_anchor_y_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: known_anchor_z_positions
  {
    size_t size = ros_message->known_anchor_z_positions.size;
    auto array_ptr = ros_message->known_anchor_z_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: known_anchor_biases
  {
    size_t size = ros_message->known_anchor_biases.size;
    auto array_ptr = ros_message->known_anchor_biases.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: known_anchor_linear_biases
  {
    size_t size = ros_message->known_anchor_linear_biases.size;
    auto array_ptr = ros_message->known_anchor_linear_biases.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: known_anchor_noise_variances
  {
    size_t size = ros_message->known_anchor_noise_variances.size;
    auto array_ptr = ros_message->known_anchor_noise_variances.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_ids
  {
    size_t size = ros_message->unknown_anchor_ids.size;
    auto array_ptr = ros_message->unknown_anchor_ids.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
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
  }

  // Field name: unknown_anchor_x_positions
  {
    size_t size = ros_message->unknown_anchor_x_positions.size;
    auto array_ptr = ros_message->unknown_anchor_x_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_y_positions
  {
    size_t size = ros_message->unknown_anchor_y_positions.size;
    auto array_ptr = ros_message->unknown_anchor_y_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_z_positions
  {
    size_t size = ros_message->unknown_anchor_z_positions.size;
    auto array_ptr = ros_message->unknown_anchor_z_positions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_biases
  {
    size_t size = ros_message->unknown_anchor_biases.size;
    auto array_ptr = ros_message->unknown_anchor_biases.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_linear_biases
  {
    size_t size = ros_message->unknown_anchor_linear_biases.size;
    auto array_ptr = ros_message->unknown_anchor_linear_biases.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_noise_variances
  {
    size_t size = ros_message->unknown_anchor_noise_variances.size;
    auto array_ptr = ros_message->unknown_anchor_noise_variances.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _AnchorInfo_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AnchorInfo_Response__ros_msg_type * ros_message = static_cast<_AnchorInfo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: known_anchor_ids
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_ids.data) {
      rosidl_runtime_c__String__Sequence__fini(&ros_message->known_anchor_ids);
    }
    if (!rosidl_runtime_c__String__Sequence__init(&ros_message->known_anchor_ids, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_ids'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_ids.data;
    for (size_t i = 0; i < size; ++i) {
      std::string tmp;
      cdr >> tmp;
      auto & ros_i = array_ptr[i];
      if (!ros_i.data) {
        rosidl_runtime_c__String__init(&ros_i);
      }
      bool succeeded = rosidl_runtime_c__String__assign(
        &ros_i,
        tmp.c_str());
      if (!succeeded) {
        fprintf(stderr, "failed to assign string into field 'known_anchor_ids'\n");
        return false;
      }
    }
  }

  // Field name: known_anchor_x_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_x_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_x_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_x_positions, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_x_positions'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_x_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: known_anchor_y_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_y_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_y_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_y_positions, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_y_positions'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_y_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: known_anchor_z_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_z_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_z_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_z_positions, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_z_positions'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_z_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: known_anchor_biases
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_biases.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_biases);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_biases, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_biases'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_biases.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: known_anchor_linear_biases
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_linear_biases.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_linear_biases);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_linear_biases, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_linear_biases'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_linear_biases.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: known_anchor_noise_variances
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->known_anchor_noise_variances.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->known_anchor_noise_variances);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->known_anchor_noise_variances, size)) {
      fprintf(stderr, "failed to create array for field 'known_anchor_noise_variances'");
      return false;
    }
    auto array_ptr = ros_message->known_anchor_noise_variances.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_ids
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_ids.data) {
      rosidl_runtime_c__String__Sequence__fini(&ros_message->unknown_anchor_ids);
    }
    if (!rosidl_runtime_c__String__Sequence__init(&ros_message->unknown_anchor_ids, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_ids'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_ids.data;
    for (size_t i = 0; i < size; ++i) {
      std::string tmp;
      cdr >> tmp;
      auto & ros_i = array_ptr[i];
      if (!ros_i.data) {
        rosidl_runtime_c__String__init(&ros_i);
      }
      bool succeeded = rosidl_runtime_c__String__assign(
        &ros_i,
        tmp.c_str());
      if (!succeeded) {
        fprintf(stderr, "failed to assign string into field 'unknown_anchor_ids'\n");
        return false;
      }
    }
  }

  // Field name: unknown_anchor_x_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_x_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_x_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_x_positions, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_x_positions'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_x_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_y_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_y_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_y_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_y_positions, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_y_positions'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_y_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_z_positions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_z_positions.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_z_positions);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_z_positions, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_z_positions'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_z_positions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_biases
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_biases.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_biases);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_biases, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_biases'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_biases.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_linear_biases
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_linear_biases.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_linear_biases);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_linear_biases, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_linear_biases'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_linear_biases.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: unknown_anchor_noise_variances
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->unknown_anchor_noise_variances.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->unknown_anchor_noise_variances);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->unknown_anchor_noise_variances, size)) {
      fprintf(stderr, "failed to create array for field 'unknown_anchor_noise_variances'");
      return false;
    }
    auto array_ptr = ros_message->unknown_anchor_noise_variances.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t get_serialized_size_sim_interfaces__srv__AnchorInfo_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AnchorInfo_Response__ros_msg_type * ros_message = static_cast<const _AnchorInfo_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name known_anchor_ids
  {
    size_t array_size = ros_message->known_anchor_ids.size;
    auto array_ptr = ros_message->known_anchor_ids.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }
  // field.name known_anchor_x_positions
  {
    size_t array_size = ros_message->known_anchor_x_positions.size;
    auto array_ptr = ros_message->known_anchor_x_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name known_anchor_y_positions
  {
    size_t array_size = ros_message->known_anchor_y_positions.size;
    auto array_ptr = ros_message->known_anchor_y_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name known_anchor_z_positions
  {
    size_t array_size = ros_message->known_anchor_z_positions.size;
    auto array_ptr = ros_message->known_anchor_z_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name known_anchor_biases
  {
    size_t array_size = ros_message->known_anchor_biases.size;
    auto array_ptr = ros_message->known_anchor_biases.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name known_anchor_linear_biases
  {
    size_t array_size = ros_message->known_anchor_linear_biases.size;
    auto array_ptr = ros_message->known_anchor_linear_biases.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name known_anchor_noise_variances
  {
    size_t array_size = ros_message->known_anchor_noise_variances.size;
    auto array_ptr = ros_message->known_anchor_noise_variances.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_ids
  {
    size_t array_size = ros_message->unknown_anchor_ids.size;
    auto array_ptr = ros_message->unknown_anchor_ids.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }
  // field.name unknown_anchor_x_positions
  {
    size_t array_size = ros_message->unknown_anchor_x_positions.size;
    auto array_ptr = ros_message->unknown_anchor_x_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_y_positions
  {
    size_t array_size = ros_message->unknown_anchor_y_positions.size;
    auto array_ptr = ros_message->unknown_anchor_y_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_z_positions
  {
    size_t array_size = ros_message->unknown_anchor_z_positions.size;
    auto array_ptr = ros_message->unknown_anchor_z_positions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_biases
  {
    size_t array_size = ros_message->unknown_anchor_biases.size;
    auto array_ptr = ros_message->unknown_anchor_biases.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_linear_biases
  {
    size_t array_size = ros_message->unknown_anchor_linear_biases.size;
    auto array_ptr = ros_message->unknown_anchor_linear_biases.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name unknown_anchor_noise_variances
  {
    size_t array_size = ros_message->unknown_anchor_noise_variances.size;
    auto array_ptr = ros_message->unknown_anchor_noise_variances.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AnchorInfo_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sim_interfaces__srv__AnchorInfo_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t max_serialized_size_sim_interfaces__srv__AnchorInfo_Response(
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

  // member: known_anchor_ids
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: known_anchor_x_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: known_anchor_y_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: known_anchor_z_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: known_anchor_biases
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: known_anchor_linear_biases
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: known_anchor_noise_variances
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_ids
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: unknown_anchor_x_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_y_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_z_positions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_biases
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_linear_biases
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: unknown_anchor_noise_variances
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = sim_interfaces__srv__AnchorInfo_Response;
    is_plain =
      (
      offsetof(DataType, unknown_anchor_noise_variances) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _AnchorInfo_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_sim_interfaces__srv__AnchorInfo_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_AnchorInfo_Response = {
  "sim_interfaces::srv",
  "AnchorInfo_Response",
  _AnchorInfo_Response__cdr_serialize,
  _AnchorInfo_Response__cdr_deserialize,
  _AnchorInfo_Response__get_serialized_size,
  _AnchorInfo_Response__max_serialized_size
};

static rosidl_message_type_support_t _AnchorInfo_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AnchorInfo_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, AnchorInfo_Response)() {
  return &_AnchorInfo_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "sim_interfaces/srv/anchor_info.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t AnchorInfo__callbacks = {
  "sim_interfaces::srv",
  "AnchorInfo",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, AnchorInfo_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, AnchorInfo_Response)(),
};

static rosidl_service_type_support_t AnchorInfo__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &AnchorInfo__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, AnchorInfo)() {
  return &AnchorInfo__handle;
}

#if defined(__cplusplus)
}
#endif
