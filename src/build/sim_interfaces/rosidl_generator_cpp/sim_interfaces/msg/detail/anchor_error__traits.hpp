// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/AnchorError.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/anchor_error__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AnchorError & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: anchor_id
  {
    out << "anchor_id: ";
    rosidl_generator_traits::value_to_yaml(msg.anchor_id, out);
    out << ", ";
  }

  // member: position_error
  {
    out << "position_error: ";
    rosidl_generator_traits::value_to_yaml(msg.position_error, out);
    out << ", ";
  }

  // member: constant_bias_error
  {
    out << "constant_bias_error: ";
    rosidl_generator_traits::value_to_yaml(msg.constant_bias_error, out);
    out << ", ";
  }

  // member: linear_bias_error
  {
    out << "linear_bias_error: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_bias_error, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnchorError & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: anchor_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "anchor_id: ";
    rosidl_generator_traits::value_to_yaml(msg.anchor_id, out);
    out << "\n";
  }

  // member: position_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_error: ";
    rosidl_generator_traits::value_to_yaml(msg.position_error, out);
    out << "\n";
  }

  // member: constant_bias_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "constant_bias_error: ";
    rosidl_generator_traits::value_to_yaml(msg.constant_bias_error, out);
    out << "\n";
  }

  // member: linear_bias_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_bias_error: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_bias_error, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnchorError & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace sim_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use sim_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_interfaces::msg::AnchorError & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::AnchorError & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::AnchorError>()
{
  return "sim_interfaces::msg::AnchorError";
}

template<>
inline const char * name<sim_interfaces::msg::AnchorError>()
{
  return "sim_interfaces/msg/AnchorError";
}

template<>
struct has_fixed_size<sim_interfaces::msg::AnchorError>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::AnchorError>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::AnchorError>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__TRAITS_HPP_
