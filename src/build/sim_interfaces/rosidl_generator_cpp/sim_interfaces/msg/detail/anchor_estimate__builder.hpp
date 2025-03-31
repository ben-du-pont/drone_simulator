// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/anchor_estimate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_AnchorEstimate_linear_bias
{
public:
  explicit Init_AnchorEstimate_linear_bias(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::AnchorEstimate linear_bias(::sim_interfaces::msg::AnchorEstimate::_linear_bias_type arg)
  {
    msg_.linear_bias = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_constant_bias
{
public:
  explicit Init_AnchorEstimate_constant_bias(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimate_linear_bias constant_bias(::sim_interfaces::msg::AnchorEstimate::_constant_bias_type arg)
  {
    msg_.constant_bias = std::move(arg);
    return Init_AnchorEstimate_linear_bias(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_position_z
{
public:
  explicit Init_AnchorEstimate_position_z(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimate_constant_bias position_z(::sim_interfaces::msg::AnchorEstimate::_position_z_type arg)
  {
    msg_.position_z = std::move(arg);
    return Init_AnchorEstimate_constant_bias(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_position_y
{
public:
  explicit Init_AnchorEstimate_position_y(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimate_position_z position_y(::sim_interfaces::msg::AnchorEstimate::_position_y_type arg)
  {
    msg_.position_y = std::move(arg);
    return Init_AnchorEstimate_position_z(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_position_x
{
public:
  explicit Init_AnchorEstimate_position_x(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimate_position_y position_x(::sim_interfaces::msg::AnchorEstimate::_position_x_type arg)
  {
    msg_.position_x = std::move(arg);
    return Init_AnchorEstimate_position_y(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_anchor_id
{
public:
  explicit Init_AnchorEstimate_anchor_id(::sim_interfaces::msg::AnchorEstimate & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimate_position_x anchor_id(::sim_interfaces::msg::AnchorEstimate::_anchor_id_type arg)
  {
    msg_.anchor_id = std::move(arg);
    return Init_AnchorEstimate_position_x(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

class Init_AnchorEstimate_header
{
public:
  Init_AnchorEstimate_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorEstimate_anchor_id header(::sim_interfaces::msg::AnchorEstimate::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AnchorEstimate_anchor_id(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimate msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::AnchorEstimate>()
{
  return sim_interfaces::msg::builder::Init_AnchorEstimate_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATE__BUILDER_HPP_
