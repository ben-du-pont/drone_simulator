// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/DronePosition.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/drone_position__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_DronePosition_total_waypoints
{
public:
  explicit Init_DronePosition_total_waypoints(::sim_interfaces::msg::DronePosition & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::DronePosition total_waypoints(::sim_interfaces::msg::DronePosition::_total_waypoints_type arg)
  {
    msg_.total_waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

class Init_DronePosition_waypoints_achieved
{
public:
  explicit Init_DronePosition_waypoints_achieved(::sim_interfaces::msg::DronePosition & msg)
  : msg_(msg)
  {}
  Init_DronePosition_total_waypoints waypoints_achieved(::sim_interfaces::msg::DronePosition::_waypoints_achieved_type arg)
  {
    msg_.waypoints_achieved = std::move(arg);
    return Init_DronePosition_total_waypoints(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

class Init_DronePosition_position_z
{
public:
  explicit Init_DronePosition_position_z(::sim_interfaces::msg::DronePosition & msg)
  : msg_(msg)
  {}
  Init_DronePosition_waypoints_achieved position_z(::sim_interfaces::msg::DronePosition::_position_z_type arg)
  {
    msg_.position_z = std::move(arg);
    return Init_DronePosition_waypoints_achieved(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

class Init_DronePosition_position_y
{
public:
  explicit Init_DronePosition_position_y(::sim_interfaces::msg::DronePosition & msg)
  : msg_(msg)
  {}
  Init_DronePosition_position_z position_y(::sim_interfaces::msg::DronePosition::_position_y_type arg)
  {
    msg_.position_y = std::move(arg);
    return Init_DronePosition_position_z(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

class Init_DronePosition_position_x
{
public:
  explicit Init_DronePosition_position_x(::sim_interfaces::msg::DronePosition & msg)
  : msg_(msg)
  {}
  Init_DronePosition_position_y position_x(::sim_interfaces::msg::DronePosition::_position_x_type arg)
  {
    msg_.position_x = std::move(arg);
    return Init_DronePosition_position_y(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

class Init_DronePosition_header
{
public:
  Init_DronePosition_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DronePosition_position_x header(::sim_interfaces::msg::DronePosition::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_DronePosition_position_x(msg_);
  }

private:
  ::sim_interfaces::msg::DronePosition msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::DronePosition>()
{
  return sim_interfaces::msg::builder::Init_DronePosition_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__BUILDER_HPP_
