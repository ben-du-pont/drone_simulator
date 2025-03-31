// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/OptimizedTrajectory.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/optimized_trajectory__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_OptimizedTrajectory_waypoint_z
{
public:
  explicit Init_OptimizedTrajectory_waypoint_z(::sim_interfaces::msg::OptimizedTrajectory & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::OptimizedTrajectory waypoint_z(::sim_interfaces::msg::OptimizedTrajectory::_waypoint_z_type arg)
  {
    msg_.waypoint_z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

class Init_OptimizedTrajectory_waypoint_y
{
public:
  explicit Init_OptimizedTrajectory_waypoint_y(::sim_interfaces::msg::OptimizedTrajectory & msg)
  : msg_(msg)
  {}
  Init_OptimizedTrajectory_waypoint_z waypoint_y(::sim_interfaces::msg::OptimizedTrajectory::_waypoint_y_type arg)
  {
    msg_.waypoint_y = std::move(arg);
    return Init_OptimizedTrajectory_waypoint_z(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

class Init_OptimizedTrajectory_waypoint_x
{
public:
  explicit Init_OptimizedTrajectory_waypoint_x(::sim_interfaces::msg::OptimizedTrajectory & msg)
  : msg_(msg)
  {}
  Init_OptimizedTrajectory_waypoint_y waypoint_x(::sim_interfaces::msg::OptimizedTrajectory::_waypoint_x_type arg)
  {
    msg_.waypoint_x = std::move(arg);
    return Init_OptimizedTrajectory_waypoint_y(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

class Init_OptimizedTrajectory_waypoint_count
{
public:
  explicit Init_OptimizedTrajectory_waypoint_count(::sim_interfaces::msg::OptimizedTrajectory & msg)
  : msg_(msg)
  {}
  Init_OptimizedTrajectory_waypoint_x waypoint_count(::sim_interfaces::msg::OptimizedTrajectory::_waypoint_count_type arg)
  {
    msg_.waypoint_count = std::move(arg);
    return Init_OptimizedTrajectory_waypoint_x(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

class Init_OptimizedTrajectory_anchor_id
{
public:
  explicit Init_OptimizedTrajectory_anchor_id(::sim_interfaces::msg::OptimizedTrajectory & msg)
  : msg_(msg)
  {}
  Init_OptimizedTrajectory_waypoint_count anchor_id(::sim_interfaces::msg::OptimizedTrajectory::_anchor_id_type arg)
  {
    msg_.anchor_id = std::move(arg);
    return Init_OptimizedTrajectory_waypoint_count(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

class Init_OptimizedTrajectory_header
{
public:
  Init_OptimizedTrajectory_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_OptimizedTrajectory_anchor_id header(::sim_interfaces::msg::OptimizedTrajectory::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_OptimizedTrajectory_anchor_id(msg_);
  }

private:
  ::sim_interfaces::msg::OptimizedTrajectory msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::OptimizedTrajectory>()
{
  return sim_interfaces::msg::builder::Init_OptimizedTrajectory_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__BUILDER_HPP_
