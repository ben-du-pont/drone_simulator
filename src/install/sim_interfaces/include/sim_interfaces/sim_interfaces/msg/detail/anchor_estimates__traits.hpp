// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/anchor_estimates__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'linear_estimate'
// Member 'refined_estimate'
// Member 'final_estimate'
#include "sim_interfaces/msg/detail/anchor_estimate__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AnchorEstimates & msg,
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

  // member: linear_estimate
  {
    out << "linear_estimate: ";
    to_flow_style_yaml(msg.linear_estimate, out);
    out << ", ";
  }

  // member: refined_estimate
  {
    out << "refined_estimate: ";
    to_flow_style_yaml(msg.refined_estimate, out);
    out << ", ";
  }

  // member: final_estimate
  {
    out << "final_estimate: ";
    to_flow_style_yaml(msg.final_estimate, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnchorEstimates & msg,
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

  // member: linear_estimate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_estimate:\n";
    to_block_style_yaml(msg.linear_estimate, out, indentation + 2);
  }

  // member: refined_estimate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "refined_estimate:\n";
    to_block_style_yaml(msg.refined_estimate, out, indentation + 2);
  }

  // member: final_estimate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "final_estimate:\n";
    to_block_style_yaml(msg.final_estimate, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnchorEstimates & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::AnchorEstimates & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::AnchorEstimates & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::AnchorEstimates>()
{
  return "sim_interfaces::msg::AnchorEstimates";
}

template<>
inline const char * name<sim_interfaces::msg::AnchorEstimates>()
{
  return "sim_interfaces/msg/AnchorEstimates";
}

template<>
struct has_fixed_size<sim_interfaces::msg::AnchorEstimates>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::AnchorEstimates>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::AnchorEstimates>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__TRAITS_HPP_
