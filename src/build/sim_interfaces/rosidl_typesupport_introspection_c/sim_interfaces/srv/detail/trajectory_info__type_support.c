// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_interfaces/srv/detail/trajectory_info__rosidl_typesupport_introspection_c.h"
#include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_interfaces/srv/detail/trajectory_info__functions.h"
#include "sim_interfaces/srv/detail/trajectory_info__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__srv__TrajectoryInfo_Request__init(message_memory);
}

void sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_fini_function(void * message_memory)
{
  sim_interfaces__srv__TrajectoryInfo_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__TrajectoryInfo_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_members = {
  "sim_interfaces__srv",  // message namespace
  "TrajectoryInfo_Request",  // message name
  1,  // number of fields
  sizeof(sim_interfaces__srv__TrajectoryInfo_Request),
  sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_member_array,  // message members
  sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_type_support_handle = {
  0,
  &sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Request)() {
  if (!sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__srv__TrajectoryInfo_Request__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "sim_interfaces/srv/detail/trajectory_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "sim_interfaces/srv/detail/trajectory_info__functions.h"
// already included above
// #include "sim_interfaces/srv/detail/trajectory_info__struct.h"


// Include directives for member types
// Member `waypoints_x`
// Member `waypoints_y`
// Member `waypoints_z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__srv__TrajectoryInfo_Response__init(message_memory);
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_fini_function(void * message_memory)
{
  sim_interfaces__srv__TrajectoryInfo_Response__fini(message_memory);
}

size_t sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_x(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_x(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_x(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_y(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_y(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_y(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_z(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_z(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_z(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_z(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_z(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_z(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_member_array[3] = {
  {
    "waypoints_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__TrajectoryInfo_Response, waypoints_x),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_x,  // size() function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_x,  // get_const(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_x,  // get(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_x,  // fetch(index, &value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_x,  // assign(index, value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_x  // resize(index) function pointer
  },
  {
    "waypoints_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__TrajectoryInfo_Response, waypoints_y),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_y,  // size() function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_y,  // get_const(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_y,  // get(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_y,  // fetch(index, &value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_y,  // assign(index, value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_y  // resize(index) function pointer
  },
  {
    "waypoints_z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__TrajectoryInfo_Response, waypoints_z),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__size_function__TrajectoryInfo_Response__waypoints_z,  // size() function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_const_function__TrajectoryInfo_Response__waypoints_z,  // get_const(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__get_function__TrajectoryInfo_Response__waypoints_z,  // get(index) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__fetch_function__TrajectoryInfo_Response__waypoints_z,  // fetch(index, &value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__assign_function__TrajectoryInfo_Response__waypoints_z,  // assign(index, value) function pointer
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__resize_function__TrajectoryInfo_Response__waypoints_z  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_members = {
  "sim_interfaces__srv",  // message namespace
  "TrajectoryInfo_Response",  // message name
  3,  // number of fields
  sizeof(sim_interfaces__srv__TrajectoryInfo_Response),
  sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_member_array,  // message members
  sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_type_support_handle = {
  0,
  &sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Response)() {
  if (!sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__srv__TrajectoryInfo_Response__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "sim_interfaces/srv/detail/trajectory_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_members = {
  "sim_interfaces__srv",  // service namespace
  "TrajectoryInfo",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_Request_message_type_support_handle,
  NULL  // response message
  // sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_Response_message_type_support_handle
};

static rosidl_service_type_support_t sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_type_support_handle = {
  0,
  &sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo)() {
  if (!sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, TrajectoryInfo_Response)()->data;
  }

  return &sim_interfaces__srv__detail__trajectory_info__rosidl_typesupport_introspection_c__TrajectoryInfo_service_type_support_handle;
}
