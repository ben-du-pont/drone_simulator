// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_interfaces/srv/detail/anchor_info__rosidl_typesupport_introspection_c.h"
#include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_interfaces/srv/detail/anchor_info__functions.h"
#include "sim_interfaces/srv/detail/anchor_info__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__srv__AnchorInfo_Request__init(message_memory);
}

void sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_fini_function(void * message_memory)
{
  sim_interfaces__srv__AnchorInfo_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_members = {
  "sim_interfaces__srv",  // message namespace
  "AnchorInfo_Request",  // message name
  1,  // number of fields
  sizeof(sim_interfaces__srv__AnchorInfo_Request),
  sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_member_array,  // message members
  sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_type_support_handle = {
  0,
  &sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Request)() {
  if (!sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__srv__AnchorInfo_Request__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__functions.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__struct.h"


// Include directives for member types
// Member `known_anchor_ids`
// Member `unknown_anchor_ids`
#include "rosidl_runtime_c/string_functions.h"
// Member `known_anchor_x_positions`
// Member `known_anchor_y_positions`
// Member `known_anchor_z_positions`
// Member `known_anchor_biases`
// Member `known_anchor_linear_biases`
// Member `known_anchor_noise_variances`
// Member `unknown_anchor_x_positions`
// Member `unknown_anchor_y_positions`
// Member `unknown_anchor_z_positions`
// Member `unknown_anchor_biases`
// Member `unknown_anchor_linear_biases`
// Member `unknown_anchor_noise_variances`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_interfaces__srv__AnchorInfo_Response__init(message_memory);
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_fini_function(void * message_memory)
{
  sim_interfaces__srv__AnchorInfo_Response__fini(message_memory);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_ids(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_ids(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_ids(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_ids(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_ids(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_ids(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_x_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_x_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_x_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_x_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_x_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_x_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_x_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_x_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_y_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_y_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_y_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_y_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_y_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_y_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_y_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_y_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_z_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_z_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_z_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_z_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_z_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_z_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_z_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_z_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_biases(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_biases(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_biases(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_biases(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_biases(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_biases(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_linear_biases(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_linear_biases(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_linear_biases(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_linear_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_linear_biases(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_linear_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_linear_biases(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_linear_biases(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_noise_variances(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_noise_variances(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_noise_variances(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_noise_variances(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_noise_variances(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_noise_variances(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_noise_variances(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_noise_variances(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_ids(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_ids(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_ids(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_ids(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_ids(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_ids(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_x_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_x_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_x_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_x_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_x_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_x_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_x_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_x_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_y_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_y_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_y_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_y_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_y_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_y_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_y_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_y_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_z_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_z_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_z_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_z_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_z_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_z_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_z_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_z_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_biases(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_biases(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_biases(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_biases(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_biases(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_biases(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_linear_biases(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_linear_biases(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_noise_variances(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_noise_variances(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_member_array[14] = {
  {
    "known_anchor_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_ids),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_ids,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_ids,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_ids,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_ids,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_ids,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_ids  // resize(index) function pointer
  },
  {
    "known_anchor_x_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_x_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_x_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_x_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_x_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_x_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_x_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_x_positions  // resize(index) function pointer
  },
  {
    "known_anchor_y_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_y_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_y_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_y_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_y_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_y_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_y_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_y_positions  // resize(index) function pointer
  },
  {
    "known_anchor_z_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_z_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_z_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_z_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_z_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_z_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_z_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_z_positions  // resize(index) function pointer
  },
  {
    "known_anchor_biases",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_biases),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_biases,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_biases,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_biases,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_biases,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_biases,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_biases  // resize(index) function pointer
  },
  {
    "known_anchor_linear_biases",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_linear_biases),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_linear_biases,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_linear_biases,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_linear_biases,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_linear_biases,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_linear_biases,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_linear_biases  // resize(index) function pointer
  },
  {
    "known_anchor_noise_variances",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, known_anchor_noise_variances),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__known_anchor_noise_variances,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__known_anchor_noise_variances,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__known_anchor_noise_variances,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__known_anchor_noise_variances,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__known_anchor_noise_variances,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__known_anchor_noise_variances  // resize(index) function pointer
  },
  {
    "unknown_anchor_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_ids),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_ids,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_ids,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_ids,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_ids,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_ids,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_ids  // resize(index) function pointer
  },
  {
    "unknown_anchor_x_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_x_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_x_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_x_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_x_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_x_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_x_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_x_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_y_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_y_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_y_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_y_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_y_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_y_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_y_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_y_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_z_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_z_positions),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_z_positions,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_z_positions,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_z_positions,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_z_positions,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_z_positions,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_z_positions  // resize(index) function pointer
  },
  {
    "unknown_anchor_biases",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_biases),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_biases,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_biases,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_biases,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_biases,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_biases,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_biases  // resize(index) function pointer
  },
  {
    "unknown_anchor_linear_biases",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_linear_biases),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_linear_biases,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_linear_biases  // resize(index) function pointer
  },
  {
    "unknown_anchor_noise_variances",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_interfaces__srv__AnchorInfo_Response, unknown_anchor_noise_variances),  // bytes offset in struct
    NULL,  // default value
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__size_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // size() function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_const_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // get_const(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__get_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // get(index) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__fetch_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // fetch(index, &value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__assign_function__AnchorInfo_Response__unknown_anchor_noise_variances,  // assign(index, value) function pointer
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__resize_function__AnchorInfo_Response__unknown_anchor_noise_variances  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_members = {
  "sim_interfaces__srv",  // message namespace
  "AnchorInfo_Response",  // message name
  14,  // number of fields
  sizeof(sim_interfaces__srv__AnchorInfo_Response),
  sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_member_array,  // message members
  sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_type_support_handle = {
  0,
  &sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Response)() {
  if (!sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_interfaces__srv__AnchorInfo_Response__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "sim_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "sim_interfaces/srv/detail/anchor_info__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_members = {
  "sim_interfaces__srv",  // service namespace
  "AnchorInfo",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_Request_message_type_support_handle,
  NULL  // response message
  // sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_Response_message_type_support_handle
};

static rosidl_service_type_support_t sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_type_support_handle = {
  0,
  &sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo)() {
  if (!sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_type_support_handle.typesupport_identifier) {
    sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_interfaces, srv, AnchorInfo_Response)()->data;
  }

  return &sim_interfaces__srv__detail__anchor_info__rosidl_typesupport_introspection_c__AnchorInfo_service_type_support_handle;
}
