// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__BUILDER_HPP_
#define SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/srv/detail/trajectory_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::srv::TrajectoryInfo_Request>()
{
  return ::sim_interfaces::srv::TrajectoryInfo_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sim_interfaces


namespace sim_interfaces
{

namespace srv
{

namespace builder
{

class Init_TrajectoryInfo_Response_waypoints_z
{
public:
  explicit Init_TrajectoryInfo_Response_waypoints_z(::sim_interfaces::srv::TrajectoryInfo_Response & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::srv::TrajectoryInfo_Response waypoints_z(::sim_interfaces::srv::TrajectoryInfo_Response::_waypoints_z_type arg)
  {
    msg_.waypoints_z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::srv::TrajectoryInfo_Response msg_;
};

class Init_TrajectoryInfo_Response_waypoints_y
{
public:
  explicit Init_TrajectoryInfo_Response_waypoints_y(::sim_interfaces::srv::TrajectoryInfo_Response & msg)
  : msg_(msg)
  {}
  Init_TrajectoryInfo_Response_waypoints_z waypoints_y(::sim_interfaces::srv::TrajectoryInfo_Response::_waypoints_y_type arg)
  {
    msg_.waypoints_y = std::move(arg);
    return Init_TrajectoryInfo_Response_waypoints_z(msg_);
  }

private:
  ::sim_interfaces::srv::TrajectoryInfo_Response msg_;
};

class Init_TrajectoryInfo_Response_waypoints_x
{
public:
  Init_TrajectoryInfo_Response_waypoints_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrajectoryInfo_Response_waypoints_y waypoints_x(::sim_interfaces::srv::TrajectoryInfo_Response::_waypoints_x_type arg)
  {
    msg_.waypoints_x = std::move(arg);
    return Init_TrajectoryInfo_Response_waypoints_y(msg_);
  }

private:
  ::sim_interfaces::srv::TrajectoryInfo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::srv::TrajectoryInfo_Response>()
{
  return sim_interfaces::srv::builder::Init_TrajectoryInfo_Response_waypoints_x();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__BUILDER_HPP_
