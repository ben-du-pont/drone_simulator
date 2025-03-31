// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/anchor_errors__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_AnchorErrors_final_error
{
public:
  explicit Init_AnchorErrors_final_error(::sim_interfaces::msg::AnchorErrors & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::AnchorErrors final_error(::sim_interfaces::msg::AnchorErrors::_final_error_type arg)
  {
    msg_.final_error = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorErrors msg_;
};

class Init_AnchorErrors_nonlinear_error
{
public:
  explicit Init_AnchorErrors_nonlinear_error(::sim_interfaces::msg::AnchorErrors & msg)
  : msg_(msg)
  {}
  Init_AnchorErrors_final_error nonlinear_error(::sim_interfaces::msg::AnchorErrors::_nonlinear_error_type arg)
  {
    msg_.nonlinear_error = std::move(arg);
    return Init_AnchorErrors_final_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorErrors msg_;
};

class Init_AnchorErrors_linear_error
{
public:
  explicit Init_AnchorErrors_linear_error(::sim_interfaces::msg::AnchorErrors & msg)
  : msg_(msg)
  {}
  Init_AnchorErrors_nonlinear_error linear_error(::sim_interfaces::msg::AnchorErrors::_linear_error_type arg)
  {
    msg_.linear_error = std::move(arg);
    return Init_AnchorErrors_nonlinear_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorErrors msg_;
};

class Init_AnchorErrors_anchor_id
{
public:
  explicit Init_AnchorErrors_anchor_id(::sim_interfaces::msg::AnchorErrors & msg)
  : msg_(msg)
  {}
  Init_AnchorErrors_linear_error anchor_id(::sim_interfaces::msg::AnchorErrors::_anchor_id_type arg)
  {
    msg_.anchor_id = std::move(arg);
    return Init_AnchorErrors_linear_error(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorErrors msg_;
};

class Init_AnchorErrors_header
{
public:
  Init_AnchorErrors_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorErrors_anchor_id header(::sim_interfaces::msg::AnchorErrors::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AnchorErrors_anchor_id(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorErrors msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::AnchorErrors>()
{
  return sim_interfaces::msg::builder::Init_AnchorErrors_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__BUILDER_HPP_
