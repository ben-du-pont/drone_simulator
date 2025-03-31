// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/AnchorError.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/anchor_error__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_AnchorError_linear_bias_error
{
public:
  explicit Init_AnchorError_linear_bias_error(::sim_interfaces::msg::AnchorError & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::AnchorError linear_bias_error(::sim_interfaces::msg::AnchorError::_linear_bias_error_type arg)
  {
    msg_.linear_bias_error = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorError msg_;
};

class Init_AnchorError_constant_bias_error
{
public:
  explicit Init_AnchorError_constant_bias_error(::sim_interfaces::msg::AnchorError & msg)
  : msg_(msg)
  {}
  Init_AnchorError_linear_bias_error constant_bias_error(::sim_interfaces::msg::AnchorError::_constant_bias_error_type arg)
  {
    msg_.constant_bias_error = std::move(arg);
    return Init_AnchorError_linear_bias_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorError msg_;
};

class Init_AnchorError_position_error
{
public:
  explicit Init_AnchorError_position_error(::sim_interfaces::msg::AnchorError & msg)
  : msg_(msg)
  {}
  Init_AnchorError_constant_bias_error position_error(::sim_interfaces::msg::AnchorError::_position_error_type arg)
  {
    msg_.position_error = std::move(arg);
    return Init_AnchorError_constant_bias_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorError msg_;
};

class Init_AnchorError_anchor_id
{
public:
  explicit Init_AnchorError_anchor_id(::sim_interfaces::msg::AnchorError & msg)
  : msg_(msg)
  {}
  Init_AnchorError_position_error anchor_id(::sim_interfaces::msg::AnchorError::_anchor_id_type arg)
  {
    msg_.anchor_id = std::move(arg);
    return Init_AnchorError_position_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorError msg_;
};

class Init_AnchorError_header
{
public:
  Init_AnchorError_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorError_anchor_id header(::sim_interfaces::msg::AnchorError::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AnchorError_anchor_id(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorError msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::AnchorError>()
{
  return sim_interfaces::msg::builder::Init_AnchorError_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERROR__BUILDER_HPP_
