// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/waypoint_lists__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_WaypointLists_remaining
{
public:
  explicit Init_WaypointLists_remaining(::sim_interfaces::msg::WaypointLists & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::WaypointLists remaining(::sim_interfaces::msg::WaypointLists::_remaining_type arg)
  {
    msg_.remaining = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointLists msg_;
};

class Init_WaypointLists_reached
{
public:
  explicit Init_WaypointLists_reached(::sim_interfaces::msg::WaypointLists & msg)
  : msg_(msg)
  {}
  Init_WaypointLists_remaining reached(::sim_interfaces::msg::WaypointLists::_reached_type arg)
  {
    msg_.reached = std::move(arg);
    return Init_WaypointLists_remaining(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointLists msg_;
};

class Init_WaypointLists_header
{
public:
  Init_WaypointLists_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WaypointLists_reached header(::sim_interfaces::msg::WaypointLists::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WaypointLists_reached(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointLists msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::WaypointLists>()
{
  return sim_interfaces::msg::builder::Init_WaypointLists_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__BUILDER_HPP_
