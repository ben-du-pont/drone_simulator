// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/waypoint_lists__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'reached'
// Member 'remaining'
#include "sim_interfaces/msg/detail/waypoint_list__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const WaypointLists & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: reached
  {
    out << "reached: ";
    to_flow_style_yaml(msg.reached, out);
    out << ", ";
  }

  // member: remaining
  {
    out << "remaining: ";
    to_flow_style_yaml(msg.remaining, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WaypointLists & msg,
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

  // member: reached
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reached:\n";
    to_block_style_yaml(msg.reached, out, indentation + 2);
  }

  // member: remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "remaining:\n";
    to_block_style_yaml(msg.remaining, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WaypointLists & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::WaypointLists & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::WaypointLists & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::WaypointLists>()
{
  return "sim_interfaces::msg::WaypointLists";
}

template<>
inline const char * name<sim_interfaces::msg::WaypointLists>()
{
  return "sim_interfaces/msg/WaypointLists";
}

template<>
struct has_fixed_size<sim_interfaces::msg::WaypointLists>
  : std::integral_constant<bool, has_fixed_size<sim_interfaces::msg::WaypointList>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<sim_interfaces::msg::WaypointLists>
  : std::integral_constant<bool, has_bounded_size<sim_interfaces::msg::WaypointList>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<sim_interfaces::msg::WaypointLists>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__TRAITS_HPP_
