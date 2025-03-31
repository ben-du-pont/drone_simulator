// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/anchor_errors__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'linear_error'
// Member 'nonlinear_error'
// Member 'final_error'
#include "sim_interfaces/msg/detail/anchor_error__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AnchorErrors & msg,
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

  // member: linear_error
  {
    out << "linear_error: ";
    to_flow_style_yaml(msg.linear_error, out);
    out << ", ";
  }

  // member: nonlinear_error
  {
    out << "nonlinear_error: ";
    to_flow_style_yaml(msg.nonlinear_error, out);
    out << ", ";
  }

  // member: final_error
  {
    out << "final_error: ";
    to_flow_style_yaml(msg.final_error, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnchorErrors & msg,
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

  // member: linear_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_error:\n";
    to_block_style_yaml(msg.linear_error, out, indentation + 2);
  }

  // member: nonlinear_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nonlinear_error:\n";
    to_block_style_yaml(msg.nonlinear_error, out, indentation + 2);
  }

  // member: final_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "final_error:\n";
    to_block_style_yaml(msg.final_error, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnchorErrors & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::AnchorErrors & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::AnchorErrors & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::AnchorErrors>()
{
  return "sim_interfaces::msg::AnchorErrors";
}

template<>
inline const char * name<sim_interfaces::msg::AnchorErrors>()
{
  return "sim_interfaces/msg/AnchorErrors";
}

template<>
struct has_fixed_size<sim_interfaces::msg::AnchorErrors>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::AnchorErrors>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::AnchorErrors>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__TRAITS_HPP_
