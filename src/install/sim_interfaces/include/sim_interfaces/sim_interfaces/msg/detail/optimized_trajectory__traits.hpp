// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/OptimizedTrajectory.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/optimized_trajectory__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const OptimizedTrajectory & msg,
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

  // member: waypoint_count
  {
    out << "waypoint_count: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_count, out);
    out << ", ";
  }

  // member: waypoint_x
  {
    if (msg.waypoint_x.size() == 0) {
      out << "waypoint_x: []";
    } else {
      out << "waypoint_x: [";
      size_t pending_items = msg.waypoint_x.size();
      for (auto item : msg.waypoint_x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: waypoint_y
  {
    if (msg.waypoint_y.size() == 0) {
      out << "waypoint_y: []";
    } else {
      out << "waypoint_y: [";
      size_t pending_items = msg.waypoint_y.size();
      for (auto item : msg.waypoint_y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: waypoint_z
  {
    if (msg.waypoint_z.size() == 0) {
      out << "waypoint_z: []";
    } else {
      out << "waypoint_z: [";
      size_t pending_items = msg.waypoint_z.size();
      for (auto item : msg.waypoint_z) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OptimizedTrajectory & msg,
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

  // member: waypoint_count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_count: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_count, out);
    out << "\n";
  }

  // member: waypoint_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoint_x.size() == 0) {
      out << "waypoint_x: []\n";
    } else {
      out << "waypoint_x:\n";
      for (auto item : msg.waypoint_x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: waypoint_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoint_y.size() == 0) {
      out << "waypoint_y: []\n";
    } else {
      out << "waypoint_y:\n";
      for (auto item : msg.waypoint_y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: waypoint_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoint_z.size() == 0) {
      out << "waypoint_z: []\n";
    } else {
      out << "waypoint_z:\n";
      for (auto item : msg.waypoint_z) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OptimizedTrajectory & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::OptimizedTrajectory & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::OptimizedTrajectory & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::OptimizedTrajectory>()
{
  return "sim_interfaces::msg::OptimizedTrajectory";
}

template<>
inline const char * name<sim_interfaces::msg::OptimizedTrajectory>()
{
  return "sim_interfaces/msg/OptimizedTrajectory";
}

template<>
struct has_fixed_size<sim_interfaces::msg::OptimizedTrajectory>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::OptimizedTrajectory>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::OptimizedTrajectory>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__TRAITS_HPP_
