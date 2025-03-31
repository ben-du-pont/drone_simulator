// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/anchor_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_AnchorInfo_types
{
public:
  explicit Init_AnchorInfo_types(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::AnchorInfo types(::sim_interfaces::msg::AnchorInfo::_types_type arg)
  {
    msg_.types = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_linear_bias
{
public:
  explicit Init_AnchorInfo_linear_bias(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_types linear_bias(::sim_interfaces::msg::AnchorInfo::_linear_bias_type arg)
  {
    msg_.linear_bias = std::move(arg);
    return Init_AnchorInfo_types(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_constant_bias
{
public:
  explicit Init_AnchorInfo_constant_bias(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_linear_bias constant_bias(::sim_interfaces::msg::AnchorInfo::_constant_bias_type arg)
  {
    msg_.constant_bias = std::move(arg);
    return Init_AnchorInfo_linear_bias(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_z
{
public:
  explicit Init_AnchorInfo_z(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_constant_bias z(::sim_interfaces::msg::AnchorInfo::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_AnchorInfo_constant_bias(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_y
{
public:
  explicit Init_AnchorInfo_y(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_z y(::sim_interfaces::msg::AnchorInfo::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_AnchorInfo_z(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_x
{
public:
  explicit Init_AnchorInfo_x(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_y x(::sim_interfaces::msg::AnchorInfo::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_AnchorInfo_y(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_ids
{
public:
  explicit Init_AnchorInfo_ids(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_x ids(::sim_interfaces::msg::AnchorInfo::_ids_type arg)
  {
    msg_.ids = std::move(arg);
    return Init_AnchorInfo_x(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_count
{
public:
  explicit Init_AnchorInfo_count(::sim_interfaces::msg::AnchorInfo & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_ids count(::sim_interfaces::msg::AnchorInfo::_count_type arg)
  {
    msg_.count = std::move(arg);
    return Init_AnchorInfo_ids(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

class Init_AnchorInfo_header
{
public:
  Init_AnchorInfo_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorInfo_count header(::sim_interfaces::msg::AnchorInfo::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AnchorInfo_count(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::AnchorInfo>()
{
  return sim_interfaces::msg::builder::Init_AnchorInfo_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_INFO__BUILDER_HPP_
