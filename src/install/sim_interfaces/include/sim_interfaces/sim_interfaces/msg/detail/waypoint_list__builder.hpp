// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:msg/WaypointList.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__BUILDER_HPP_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/msg/detail/waypoint_list__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace msg
{

namespace builder
{

class Init_WaypointList_z
{
public:
  explicit Init_WaypointList_z(::sim_interfaces::msg::WaypointList & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::msg::WaypointList z(::sim_interfaces::msg::WaypointList::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointList msg_;
};

class Init_WaypointList_y
{
public:
  explicit Init_WaypointList_y(::sim_interfaces::msg::WaypointList & msg)
  : msg_(msg)
  {}
  Init_WaypointList_z y(::sim_interfaces::msg::WaypointList::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_WaypointList_z(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointList msg_;
};

class Init_WaypointList_x
{
public:
  explicit Init_WaypointList_x(::sim_interfaces::msg::WaypointList & msg)
  : msg_(msg)
  {}
  Init_WaypointList_y x(::sim_interfaces::msg::WaypointList::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_WaypointList_y(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointList msg_;
};

class Init_WaypointList_count
{
public:
  explicit Init_WaypointList_count(::sim_interfaces::msg::WaypointList & msg)
  : msg_(msg)
  {}
  Init_WaypointList_x count(::sim_interfaces::msg::WaypointList::_count_type arg)
  {
    msg_.count = std::move(arg);
    return Init_WaypointList_x(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointList msg_;
};

class Init_WaypointList_header
{
public:
  Init_WaypointList_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WaypointList_count header(::sim_interfaces::msg::WaypointList::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WaypointList_count(msg_);
  }

private:
  ::sim_interfaces::msg::WaypointList msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::msg::WaypointList>()
{
  return sim_interfaces::msg::builder::Init_WaypointList_header();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__BUILDER_HPP_
