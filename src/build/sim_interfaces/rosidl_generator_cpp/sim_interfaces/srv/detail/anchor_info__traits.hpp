// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__TRAITS_HPP_
#define SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/srv/detail/anchor_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AnchorInfo_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnchorInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnchorInfo_Request & msg, bool use_flow_style = false)
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
  const sim_interfaces::srv::AnchorInfo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::srv::AnchorInfo_Request & msg)
{
  return sim_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::srv::AnchorInfo_Request>()
{
  return "sim_interfaces::srv::AnchorInfo_Request";
}

template<>
inline const char * name<sim_interfaces::srv::AnchorInfo_Request>()
{
  return "sim_interfaces/srv/AnchorInfo_Request";
}

template<>
struct has_fixed_size<sim_interfaces::srv::AnchorInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_interfaces::srv::AnchorInfo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_interfaces::srv::AnchorInfo_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace sim_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AnchorInfo_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: known_anchor_ids
  {
    if (msg.known_anchor_ids.size() == 0) {
      out << "known_anchor_ids: []";
    } else {
      out << "known_anchor_ids: [";
      size_t pending_items = msg.known_anchor_ids.size();
      for (auto item : msg.known_anchor_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_x_positions
  {
    if (msg.known_anchor_x_positions.size() == 0) {
      out << "known_anchor_x_positions: []";
    } else {
      out << "known_anchor_x_positions: [";
      size_t pending_items = msg.known_anchor_x_positions.size();
      for (auto item : msg.known_anchor_x_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_y_positions
  {
    if (msg.known_anchor_y_positions.size() == 0) {
      out << "known_anchor_y_positions: []";
    } else {
      out << "known_anchor_y_positions: [";
      size_t pending_items = msg.known_anchor_y_positions.size();
      for (auto item : msg.known_anchor_y_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_z_positions
  {
    if (msg.known_anchor_z_positions.size() == 0) {
      out << "known_anchor_z_positions: []";
    } else {
      out << "known_anchor_z_positions: [";
      size_t pending_items = msg.known_anchor_z_positions.size();
      for (auto item : msg.known_anchor_z_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_biases
  {
    if (msg.known_anchor_biases.size() == 0) {
      out << "known_anchor_biases: []";
    } else {
      out << "known_anchor_biases: [";
      size_t pending_items = msg.known_anchor_biases.size();
      for (auto item : msg.known_anchor_biases) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_linear_biases
  {
    if (msg.known_anchor_linear_biases.size() == 0) {
      out << "known_anchor_linear_biases: []";
    } else {
      out << "known_anchor_linear_biases: [";
      size_t pending_items = msg.known_anchor_linear_biases.size();
      for (auto item : msg.known_anchor_linear_biases) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: known_anchor_noise_variances
  {
    if (msg.known_anchor_noise_variances.size() == 0) {
      out << "known_anchor_noise_variances: []";
    } else {
      out << "known_anchor_noise_variances: [";
      size_t pending_items = msg.known_anchor_noise_variances.size();
      for (auto item : msg.known_anchor_noise_variances) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_ids
  {
    if (msg.unknown_anchor_ids.size() == 0) {
      out << "unknown_anchor_ids: []";
    } else {
      out << "unknown_anchor_ids: [";
      size_t pending_items = msg.unknown_anchor_ids.size();
      for (auto item : msg.unknown_anchor_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_x_positions
  {
    if (msg.unknown_anchor_x_positions.size() == 0) {
      out << "unknown_anchor_x_positions: []";
    } else {
      out << "unknown_anchor_x_positions: [";
      size_t pending_items = msg.unknown_anchor_x_positions.size();
      for (auto item : msg.unknown_anchor_x_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_y_positions
  {
    if (msg.unknown_anchor_y_positions.size() == 0) {
      out << "unknown_anchor_y_positions: []";
    } else {
      out << "unknown_anchor_y_positions: [";
      size_t pending_items = msg.unknown_anchor_y_positions.size();
      for (auto item : msg.unknown_anchor_y_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_z_positions
  {
    if (msg.unknown_anchor_z_positions.size() == 0) {
      out << "unknown_anchor_z_positions: []";
    } else {
      out << "unknown_anchor_z_positions: [";
      size_t pending_items = msg.unknown_anchor_z_positions.size();
      for (auto item : msg.unknown_anchor_z_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_biases
  {
    if (msg.unknown_anchor_biases.size() == 0) {
      out << "unknown_anchor_biases: []";
    } else {
      out << "unknown_anchor_biases: [";
      size_t pending_items = msg.unknown_anchor_biases.size();
      for (auto item : msg.unknown_anchor_biases) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_linear_biases
  {
    if (msg.unknown_anchor_linear_biases.size() == 0) {
      out << "unknown_anchor_linear_biases: []";
    } else {
      out << "unknown_anchor_linear_biases: [";
      size_t pending_items = msg.unknown_anchor_linear_biases.size();
      for (auto item : msg.unknown_anchor_linear_biases) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: unknown_anchor_noise_variances
  {
    if (msg.unknown_anchor_noise_variances.size() == 0) {
      out << "unknown_anchor_noise_variances: []";
    } else {
      out << "unknown_anchor_noise_variances: [";
      size_t pending_items = msg.unknown_anchor_noise_variances.size();
      for (auto item : msg.unknown_anchor_noise_variances) {
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
  const AnchorInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: known_anchor_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_ids.size() == 0) {
      out << "known_anchor_ids: []\n";
    } else {
      out << "known_anchor_ids:\n";
      for (auto item : msg.known_anchor_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_x_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_x_positions.size() == 0) {
      out << "known_anchor_x_positions: []\n";
    } else {
      out << "known_anchor_x_positions:\n";
      for (auto item : msg.known_anchor_x_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_y_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_y_positions.size() == 0) {
      out << "known_anchor_y_positions: []\n";
    } else {
      out << "known_anchor_y_positions:\n";
      for (auto item : msg.known_anchor_y_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_z_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_z_positions.size() == 0) {
      out << "known_anchor_z_positions: []\n";
    } else {
      out << "known_anchor_z_positions:\n";
      for (auto item : msg.known_anchor_z_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_biases
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_biases.size() == 0) {
      out << "known_anchor_biases: []\n";
    } else {
      out << "known_anchor_biases:\n";
      for (auto item : msg.known_anchor_biases) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_linear_biases
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_linear_biases.size() == 0) {
      out << "known_anchor_linear_biases: []\n";
    } else {
      out << "known_anchor_linear_biases:\n";
      for (auto item : msg.known_anchor_linear_biases) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: known_anchor_noise_variances
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.known_anchor_noise_variances.size() == 0) {
      out << "known_anchor_noise_variances: []\n";
    } else {
      out << "known_anchor_noise_variances:\n";
      for (auto item : msg.known_anchor_noise_variances) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_ids.size() == 0) {
      out << "unknown_anchor_ids: []\n";
    } else {
      out << "unknown_anchor_ids:\n";
      for (auto item : msg.unknown_anchor_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_x_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_x_positions.size() == 0) {
      out << "unknown_anchor_x_positions: []\n";
    } else {
      out << "unknown_anchor_x_positions:\n";
      for (auto item : msg.unknown_anchor_x_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_y_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_y_positions.size() == 0) {
      out << "unknown_anchor_y_positions: []\n";
    } else {
      out << "unknown_anchor_y_positions:\n";
      for (auto item : msg.unknown_anchor_y_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_z_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_z_positions.size() == 0) {
      out << "unknown_anchor_z_positions: []\n";
    } else {
      out << "unknown_anchor_z_positions:\n";
      for (auto item : msg.unknown_anchor_z_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_biases
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_biases.size() == 0) {
      out << "unknown_anchor_biases: []\n";
    } else {
      out << "unknown_anchor_biases:\n";
      for (auto item : msg.unknown_anchor_biases) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_linear_biases
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_linear_biases.size() == 0) {
      out << "unknown_anchor_linear_biases: []\n";
    } else {
      out << "unknown_anchor_linear_biases:\n";
      for (auto item : msg.unknown_anchor_linear_biases) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: unknown_anchor_noise_variances
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.unknown_anchor_noise_variances.size() == 0) {
      out << "unknown_anchor_noise_variances: []\n";
    } else {
      out << "unknown_anchor_noise_variances:\n";
      for (auto item : msg.unknown_anchor_noise_variances) {
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

inline std::string to_yaml(const AnchorInfo_Response & msg, bool use_flow_style = false)
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
  const sim_interfaces::srv::AnchorInfo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::srv::AnchorInfo_Response & msg)
{
  return sim_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::srv::AnchorInfo_Response>()
{
  return "sim_interfaces::srv::AnchorInfo_Response";
}

template<>
inline const char * name<sim_interfaces::srv::AnchorInfo_Response>()
{
  return "sim_interfaces/srv/AnchorInfo_Response";
}

template<>
struct has_fixed_size<sim_interfaces::srv::AnchorInfo_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::srv::AnchorInfo_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::srv::AnchorInfo_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sim_interfaces::srv::AnchorInfo>()
{
  return "sim_interfaces::srv::AnchorInfo";
}

template<>
inline const char * name<sim_interfaces::srv::AnchorInfo>()
{
  return "sim_interfaces/srv/AnchorInfo";
}

template<>
struct has_fixed_size<sim_interfaces::srv::AnchorInfo>
  : std::integral_constant<
    bool,
    has_fixed_size<sim_interfaces::srv::AnchorInfo_Request>::value &&
    has_fixed_size<sim_interfaces::srv::AnchorInfo_Response>::value
  >
{
};

template<>
struct has_bounded_size<sim_interfaces::srv::AnchorInfo>
  : std::integral_constant<
    bool,
    has_bounded_size<sim_interfaces::srv::AnchorInfo_Request>::value &&
    has_bounded_size<sim_interfaces::srv::AnchorInfo_Response>::value
  >
{
};

template<>
struct is_service<sim_interfaces::srv::AnchorInfo>
  : std::true_type
{
};

template<>
struct is_service_request<sim_interfaces::srv::AnchorInfo_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sim_interfaces::srv::AnchorInfo_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__TRAITS_HPP_
