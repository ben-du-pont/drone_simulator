// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_interfaces:msg/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__TRAITS_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_interfaces/msg/detail/anchor_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace sim_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AnchorInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: count
  {
    out << "count: ";
    rosidl_generator_traits::value_to_yaml(msg.count, out);
    out << ", ";
  }

  // member: ids
  {
    if (msg.ids.size() == 0) {
      out << "ids: []";
    } else {
      out << "ids: [";
      size_t pending_items = msg.ids.size();
      for (auto item : msg.ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: x
  {
    if (msg.x.size() == 0) {
      out << "x: []";
    } else {
      out << "x: [";
      size_t pending_items = msg.x.size();
      for (auto item : msg.x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: y
  {
    if (msg.y.size() == 0) {
      out << "y: []";
    } else {
      out << "y: [";
      size_t pending_items = msg.y.size();
      for (auto item : msg.y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: z
  {
    if (msg.z.size() == 0) {
      out << "z: []";
    } else {
      out << "z: [";
      size_t pending_items = msg.z.size();
      for (auto item : msg.z) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: constant_bias
  {
    if (msg.constant_bias.size() == 0) {
      out << "constant_bias: []";
    } else {
      out << "constant_bias: [";
      size_t pending_items = msg.constant_bias.size();
      for (auto item : msg.constant_bias) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: linear_bias
  {
    if (msg.linear_bias.size() == 0) {
      out << "linear_bias: []";
    } else {
      out << "linear_bias: [";
      size_t pending_items = msg.linear_bias.size();
      for (auto item : msg.linear_bias) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: types
  {
    if (msg.types.size() == 0) {
      out << "types: []";
    } else {
      out << "types: [";
      size_t pending_items = msg.types.size();
      for (auto item : msg.types) {
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
  const AnchorInfo & msg,
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

  // member: count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "count: ";
    rosidl_generator_traits::value_to_yaml(msg.count, out);
    out << "\n";
  }

  // member: ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ids.size() == 0) {
      out << "ids: []\n";
    } else {
      out << "ids:\n";
      for (auto item : msg.ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.x.size() == 0) {
      out << "x: []\n";
    } else {
      out << "x:\n";
      for (auto item : msg.x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.y.size() == 0) {
      out << "y: []\n";
    } else {
      out << "y:\n";
      for (auto item : msg.y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.z.size() == 0) {
      out << "z: []\n";
    } else {
      out << "z:\n";
      for (auto item : msg.z) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: constant_bias
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.constant_bias.size() == 0) {
      out << "constant_bias: []\n";
    } else {
      out << "constant_bias:\n";
      for (auto item : msg.constant_bias) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: linear_bias
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.linear_bias.size() == 0) {
      out << "linear_bias: []\n";
    } else {
      out << "linear_bias:\n";
      for (auto item : msg.linear_bias) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: types
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.types.size() == 0) {
      out << "types: []\n";
    } else {
      out << "types:\n";
      for (auto item : msg.types) {
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

inline std::string to_yaml(const AnchorInfo & msg, bool use_flow_style = false)
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
  const sim_interfaces::msg::AnchorInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_interfaces::msg::AnchorInfo & msg)
{
  return sim_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_interfaces::msg::AnchorInfo>()
{
  return "sim_interfaces::msg::AnchorInfo";
}

template<>
inline const char * name<sim_interfaces::msg::AnchorInfo>()
{
  return "sim_interfaces/msg/AnchorInfo";
}

template<>
struct has_fixed_size<sim_interfaces::msg::AnchorInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sim_interfaces::msg::AnchorInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sim_interfaces::msg::AnchorInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__TRAITS_HPP_
