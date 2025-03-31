// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice
#include "sim_interfaces/srv/detail/trajectory_info__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "sim_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "sim_interfaces/srv/detail/trajectory_info__struct.h"
#include "sim_interfaces/srv/detail/trajectory_info__functions.h"
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


using _TrajectoryInfo_Request__ros_msg_type = sim_interfaces__srv__TrajectoryInfo_Request;

static bool _TrajectoryInfo_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TrajectoryInfo_Request__ros_msg_type * ros_message = static_cast<const _TrajectoryInfo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr << ros_message->structure_needs_at_least_one_member;
  }

  return true;
}

static bool _TrajectoryInfo_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TrajectoryInfo_Request__ros_msg_type * ros_message = static_cast<_TrajectoryInfo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: structure_needs_at_least_one_member
  {
    cdr >> ros_message->structure_needs_at_least_one_member;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t get_serialized_size_sim_interfaces__srv__TrajectoryInfo_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TrajectoryInfo_Request__ros_msg_type * ros_message = static_cast<const _TrajectoryInfo_Request__ros_msg_type *>(untyped_ros_message);
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

static uint32_t _TrajectoryInfo_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sim_interfaces__srv__TrajectoryInfo_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t max_serialized_size_sim_interfaces__srv__TrajectoryInfo_Request(
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
    using DataType = sim_interfaces__srv__TrajectoryInfo_Request;
    is_plain =
      (
      offsetof(DataType, structure_needs_at_least_one_member) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TrajectoryInfo_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_sim_interfaces__srv__TrajectoryInfo_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TrajectoryInfo_Request = {
  "sim_interfaces::srv",
  "TrajectoryInfo_Request",
  _TrajectoryInfo_Request__cdr_serialize,
  _TrajectoryInfo_Request__cdr_deserialize,
  _TrajectoryInfo_Request__get_serialized_size,
  _TrajectoryInfo_Request__max_serialized_size
};

static rosidl_message_type_support_t _TrajectoryInfo_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TrajectoryInfo_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, TrajectoryInfo_Request)() {
  return &_TrajectoryInfo_Request__type_support;
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
// #include "sim_interfaces/srv/detail/trajectory_info__struct.h"
// already included above
// #include "sim_interfaces/srv/detail/trajectory_info__functions.h"
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

#include "rosidl_runtime_c/primitives_sequence.h"  // waypoints_x, waypoints_y, waypoints_z
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // waypoints_x, waypoints_y, waypoints_z

// forward declare type support functions


using _TrajectoryInfo_Response__ros_msg_type = sim_interfaces__srv__TrajectoryInfo_Response;

static bool _TrajectoryInfo_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TrajectoryInfo_Response__ros_msg_type * ros_message = static_cast<const _TrajectoryInfo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: waypoints_x
  {
    size_t size = ros_message->waypoints_x.size;
    auto array_ptr = ros_message->waypoints_x.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: waypoints_y
  {
    size_t size = ros_message->waypoints_y.size;
    auto array_ptr = ros_message->waypoints_y.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: waypoints_z
  {
    size_t size = ros_message->waypoints_z.size;
    auto array_ptr = ros_message->waypoints_z.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _TrajectoryInfo_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TrajectoryInfo_Response__ros_msg_type * ros_message = static_cast<_TrajectoryInfo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: waypoints_x
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->waypoints_x.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->waypoints_x);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->waypoints_x, size)) {
      fprintf(stderr, "failed to create array for field 'waypoints_x'");
      return false;
    }
    auto array_ptr = ros_message->waypoints_x.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: waypoints_y
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->waypoints_y.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->waypoints_y);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->waypoints_y, size)) {
      fprintf(stderr, "failed to create array for field 'waypoints_y'");
      return false;
    }
    auto array_ptr = ros_message->waypoints_y.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: waypoints_z
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->waypoints_z.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->waypoints_z);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->waypoints_z, size)) {
      fprintf(stderr, "failed to create array for field 'waypoints_z'");
      return false;
    }
    auto array_ptr = ros_message->waypoints_z.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t get_serialized_size_sim_interfaces__srv__TrajectoryInfo_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TrajectoryInfo_Response__ros_msg_type * ros_message = static_cast<const _TrajectoryInfo_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name waypoints_x
  {
    size_t array_size = ros_message->waypoints_x.size;
    auto array_ptr = ros_message->waypoints_x.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name waypoints_y
  {
    size_t array_size = ros_message->waypoints_y.size;
    auto array_ptr = ros_message->waypoints_y.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name waypoints_z
  {
    size_t array_size = ros_message->waypoints_z.size;
    auto array_ptr = ros_message->waypoints_z.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TrajectoryInfo_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sim_interfaces__srv__TrajectoryInfo_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sim_interfaces
size_t max_serialized_size_sim_interfaces__srv__TrajectoryInfo_Response(
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

  // member: waypoints_x
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
  // member: waypoints_y
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
  // member: waypoints_z
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
    using DataType = sim_interfaces__srv__TrajectoryInfo_Response;
    is_plain =
      (
      offsetof(DataType, waypoints_z) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TrajectoryInfo_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_sim_interfaces__srv__TrajectoryInfo_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TrajectoryInfo_Response = {
  "sim_interfaces::srv",
  "TrajectoryInfo_Response",
  _TrajectoryInfo_Response__cdr_serialize,
  _TrajectoryInfo_Response__cdr_deserialize,
  _TrajectoryInfo_Response__get_serialized_size,
  _TrajectoryInfo_Response__max_serialized_size
};

static rosidl_message_type_support_t _TrajectoryInfo_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TrajectoryInfo_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, TrajectoryInfo_Response)() {
  return &_TrajectoryInfo_Response__type_support;
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
#include "sim_interfaces/srv/trajectory_info.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t TrajectoryInfo__callbacks = {
  "sim_interfaces::srv",
  "TrajectoryInfo",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, TrajectoryInfo_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, TrajectoryInfo_Response)(),
};

static rosidl_service_type_support_t TrajectoryInfo__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &TrajectoryInfo__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sim_interfaces, srv, TrajectoryInfo)() {
  return &TrajectoryInfo__handle;
}

#if defined(__cplusplus)
}
#endif
