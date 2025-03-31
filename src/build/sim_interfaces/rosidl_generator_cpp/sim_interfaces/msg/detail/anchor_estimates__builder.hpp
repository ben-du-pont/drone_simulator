// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/anchor_estimates__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_AnchorEstimates_final_estimate
{
public:
  explicit Init_AnchorEstimates_final_estimate(::sim_interfaces::msg::AnchorEstimates & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::AnchorEstimates final_estimate(::sim_interfaces::msg::AnchorEstimates::_final_estimate_type arg)
  {
    msg_.final_estimate = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimates msg_;
};

class Init_AnchorEstimates_refined_estimate
{
public:
  explicit Init_AnchorEstimates_refined_estimate(::sim_interfaces::msg::AnchorEstimates & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimates_final_estimate refined_estimate(::sim_interfaces::msg::AnchorEstimates::_refined_estimate_type arg)
  {
    msg_.refined_estimate = std::move(arg);
    return Init_AnchorEstimates_final_estimate(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimates msg_;
};

class Init_AnchorEstimates_linear_estimate
{
public:
  explicit Init_AnchorEstimates_linear_estimate(::sim_interfaces::msg::AnchorEstimates & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimates_refined_estimate linear_estimate(::sim_interfaces::msg::AnchorEstimates::_linear_estimate_type arg)
  {
    msg_.linear_estimate = std::move(arg);
    return Init_AnchorEstimates_refined_estimate(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimates msg_;
};

class Init_AnchorEstimates_anchor_id
{
public:
  explicit Init_AnchorEstimates_anchor_id(::sim_interfaces::msg::AnchorEstimates & msg)
  : msg_(msg)
  {}
  Init_AnchorEstimates_linear_estimate anchor_id(::sim_interfaces::msg::AnchorEstimates::_anchor_id_type arg)
  {
    msg_.anchor_id = std::move(arg);
    return Init_AnchorEstimates_linear_estimate(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimates msg_;
};

class Init_AnchorEstimates_header
{
public:
  Init_AnchorEstimates_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorEstimates_anchor_id header(::sim_interfaces::msg::AnchorEstimates::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AnchorEstimates_anchor_id(msg_);
  }

private:
  ::sim_interfaces::msg::AnchorEstimates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::AnchorEstimates>()
{
  return sim_interfaces::msg::builder::Init_AnchorEstimates_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__BUILDER_HPP_
