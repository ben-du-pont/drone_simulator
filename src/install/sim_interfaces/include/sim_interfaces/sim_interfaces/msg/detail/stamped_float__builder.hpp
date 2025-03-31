// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/StampedFloat.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/stamped_float__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_StampedFloat_data
{
public:
  explicit Init_StampedFloat_data(::sim_interfaces::msg::StampedFloat & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::StampedFloat data(::sim_interfaces::msg::StampedFloat::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::StampedFloat msg_;
};

class Init_StampedFloat_header
{
public:
  Init_StampedFloat_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StampedFloat_data header(::sim_interfaces::msg::StampedFloat::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_StampedFloat_data(msg_);
  }

private:
  ::sim_interfaces::msg::StampedFloat msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::StampedFloat>()
{
  return sim_interfaces::msg::builder::Init_StampedFloat_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__BUILDER_HPP_
