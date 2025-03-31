// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/DronePosition.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_interfaces__msg__DronePosition __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__DronePosition __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DronePosition_
{
  using Type = DronePosition_<ContainerAllocator>;

  explicit DronePosition_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position_x = 0.0;
      this->position_y = 0.0;
      this->position_z = 0.0;
      this->waypoints_achieved = 0l;
      this->total_waypoints = 0l;
    }
  }

  explicit DronePosition_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position_x = 0.0;
      this->position_y = 0.0;
      this->position_z = 0.0;
      this->waypoints_achieved = 0l;
      this->total_waypoints = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _position_x_type =
    double;
  _position_x_type position_x;
  using _position_y_type =
    double;
  _position_y_type position_y;
  using _position_z_type =
    double;
  _position_z_type position_z;
  using _waypoints_achieved_type =
    int32_t;
  _waypoints_achieved_type waypoints_achieved;
  using _total_waypoints_type =
    int32_t;
  _total_waypoints_type total_waypoints;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__position_x(
    const double & _arg)
  {
    this->position_x = _arg;
    return *this;
  }
  Type & set__position_y(
    const double & _arg)
  {
    this->position_y = _arg;
    return *this;
  }
  Type & set__position_z(
    const double & _arg)
  {
    this->position_z = _arg;
    return *this;
  }
  Type & set__waypoints_achieved(
    const int32_t & _arg)
  {
    this->waypoints_achieved = _arg;
    return *this;
  }
  Type & set__total_waypoints(
    const int32_t & _arg)
  {
    this->total_waypoints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::DronePosition_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::DronePosition_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::DronePosition_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::DronePosition_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__DronePosition
    std::shared_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__DronePosition
    std::shared_ptr<sim_interfaces::msg::DronePosition_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DronePosition_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->position_x != other.position_x) {
      return false;
    }
    if (this->position_y != other.position_y) {
      return false;
    }
    if (this->position_z != other.position_z) {
      return false;
    }
    if (this->waypoints_achieved != other.waypoints_achieved) {
      return false;
    }
    if (this->total_waypoints != other.total_waypoints) {
      return false;
    }
    return true;
  }
  bool operator!=(const DronePosition_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DronePosition_

// alias to use template instance with default allocator
using DronePosition =
  sim_interfaces::msg::DronePosition_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__DRONE_POSITION__STRUCT_HPP_
