// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__TRAITS_HPP_
#define SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/srv/detail/trajectory_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrajectoryInfo_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrajectoryInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrajectoryInfo_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sim_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use sim_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_interfaces::srv::TrajectoryInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::srv::TrajectoryInfo_Request & msg)
{
  return sim_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::srv::TrajectoryInfo_Request>()
{
  return "sim_interfaces::srv::TrajectoryInfo_Request";
}

template<>
inline const char * name<sim_interfaces::srv::TrajectoryInfo_Request>()
{
  return "sim_interfaces/srv/TrajectoryInfo_Request";
}

template<>
struct has_fixed_size<sim_interfaces::srv::TrajectoryInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_interfaces::srv::TrajectoryInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_interfaces::srv::TrajectoryInfo_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace sim_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrajectoryInfo_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: waypoints_x
  {
    if (msg.waypoints_x.size() == 0) {
      out << "waypoints_x: []";
    } else {
      out << "waypoints_x: [";
      size_t pending_items = msg.waypoints_x.size();
      for (auto item : msg.waypoints_x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: waypoints_y
  {
    if (msg.waypoints_y.size() == 0) {
      out << "waypoints_y: []";
    } else {
      out << "waypoints_y: [";
      size_t pending_items = msg.waypoints_y.size();
      for (auto item : msg.waypoints_y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: waypoints_z
  {
    if (msg.waypoints_z.size() == 0) {
      out << "waypoints_z: []";
    } else {
      out << "waypoints_z: [";
      size_t pending_items = msg.waypoints_z.size();
      for (auto item : msg.waypoints_z) {
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
  const TrajectoryInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: waypoints_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoints_x.size() == 0) {
      out << "waypoints_x: []\n";
    } else {
      out << "waypoints_x:\n";
      for (auto item : msg.waypoints_x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: waypoints_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoints_y.size() == 0) {
      out << "waypoints_y: []\n";
    } else {
      out << "waypoints_y:\n";
      for (auto item : msg.waypoints_y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: waypoints_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoints_z.size() == 0) {
      out << "waypoints_z: []\n";
    } else {
      out << "waypoints_z:\n";
      for (auto item : msg.waypoints_z) {
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

inline std::string to_yaml(const TrajectoryInfo_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sim_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use sim_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_interfaces::srv::TrajectoryInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::srv::TrajectoryInfo_Response & msg)
{
  return sim_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::srv::TrajectoryInfo_Response>()
{
  return "sim_interfaces::srv::TrajectoryInfo_Response";
}

template<>
inline const char * name<sim_interfaces::srv::TrajectoryInfo_Response>()
{
  return "sim_interfaces/srv/TrajectoryInfo_Response";
}

template<>
struct has_fixed_size<sim_interfaces::srv::TrajectoryInfo_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::srv::TrajectoryInfo_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::srv::TrajectoryInfo_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sim_interfaces::srv::TrajectoryInfo>()
{
  return "sim_interfaces::srv::TrajectoryInfo";
}

template<>
inline const char * name<sim_interfaces::srv::TrajectoryInfo>()
{
  return "sim_interfaces/srv/TrajectoryInfo";
}

template<>
struct has_fixed_size<sim_interfaces::srv::TrajectoryInfo>
  : std::integral_constant<
    bool,
    has_fixed_size<sim_interfaces::srv::TrajectoryInfo_Request>::value &&
    has_fixed_size<sim_interfaces::srv::TrajectoryInfo_Response>::value
  >
{
};

template<>
struct has_bounded_size<sim_interfaces::srv::TrajectoryInfo>
  : std::integral_constant<
    bool,
    has_bounded_size<sim_interfaces::srv::TrajectoryInfo_Request>::value &&
    has_bounded_size<sim_interfaces::srv::TrajectoryInfo_Response>::value
  >
{
};

template<>
struct is_service<sim_interfaces::srv::TrajectoryInfo>
  : std::true_type
{
};

template<>
struct is_service_request<sim_interfaces::srv::TrajectoryInfo_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sim_interfaces::srv::TrajectoryInfo_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__TRAITS_HPP_
