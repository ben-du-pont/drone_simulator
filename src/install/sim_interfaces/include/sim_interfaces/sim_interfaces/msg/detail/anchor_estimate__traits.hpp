// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/anchor_estimate__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AnchorEstimate & msg,
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

  // member: position_x
  {
    out << "position_x: ";
    rosidl_generator_traits::value_to_yaml(msg.position_x, out);
    out << ", ";
  }

  // member: position_y
  {
    out << "position_y: ";
    rosidl_generator_traits::value_to_yaml(msg.position_y, out);
    out << ", ";
  }

  // member: position_z
  {
    out << "position_z: ";
    rosidl_generator_traits::value_to_yaml(msg.position_z, out);
    out << ", ";
  }

  // member: constant_bias
  {
    out << "constant_bias: ";
    rosidl_generator_traits::value_to_yaml(msg.constant_bias, out);
    out << ", ";
  }

  // member: linear_bias
  {
    out << "linear_bias: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_bias, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnchorEstimate & msg,
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

  // member: position_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_x: ";
    rosidl_generator_traits::value_to_yaml(msg.position_x, out);
    out << "\n";
  }

  // member: position_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_y: ";
    rosidl_generator_traits::value_to_yaml(msg.position_y, out);
    out << "\n";
  }

  // member: position_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_z: ";
    rosidl_generator_traits::value_to_yaml(msg.position_z, out);
    out << "\n";
  }

  // member: constant_bias
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "constant_bias: ";
    rosidl_generator_traits::value_to_yaml(msg.constant_bias, out);
    out << "\n";
  }

  // member: linear_bias
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_bias: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_bias, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnchorEstimate & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::AnchorEstimate & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::AnchorEstimate & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::AnchorEstimate>()
{
  return "sim_interfaces::msg::AnchorEstimate";
}

template<>
inline const char * name<sim_interfaces::msg::AnchorEstimate>()
{
  return "sim_interfaces/msg/AnchorEstimate";
}

template<>
struct has_fixed_size<sim_interfaces::msg::AnchorEstimate>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::AnchorEstimate>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::AnchorEstimate>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__TRAITS_HPP_
