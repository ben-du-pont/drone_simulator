// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/DronePosition.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/drone_position__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const DronePosition & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
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

  // member: waypoints_achieved
  {
    out << "waypoints_achieved: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoints_achieved, out);
    out << ", ";
  }

  // member: total_waypoints
  {
    out << "total_waypoints: ";
    rosidl_generator_traits::value_to_yaml(msg.total_waypoints, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DronePosition & msg,
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

  // member: waypoints_achieved
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoints_achieved: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoints_achieved, out);
    out << "\n";
  }

  // member: total_waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "total_waypoints: ";
    rosidl_generator_traits::value_to_yaml(msg.total_waypoints, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DronePosition & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::DronePosition & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::DronePosition & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::DronePosition>()
{
  return "sim_interfaces::msg::DronePosition";
}

template<>
inline const char * name<sim_interfaces::msg::DronePosition>()
{
  return "sim_interfaces/msg/DronePosition";
}

template<>
struct has_fixed_size<sim_interfaces::msg::DronePosition>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<sim_interfaces::msg::DronePosition>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<sim_interfaces::msg::DronePosition>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__TRAITS_HPP_
