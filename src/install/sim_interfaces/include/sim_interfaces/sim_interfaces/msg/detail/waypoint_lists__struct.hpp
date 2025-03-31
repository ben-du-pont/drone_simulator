// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/WaypointLists.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_HPP_

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
// Member 'reached'
// Member 'remaining'
#include "sim_interfaces/msg/detail/waypoint_list__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_interfaces__msg__WaypointLists __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__WaypointLists __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WaypointLists_
{
  using Type = WaypointLists_<ContainerAllocator>;

  explicit WaypointLists_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    reached(_init),
    remaining(_init)
  {
    (void)_init;
  }

  explicit WaypointLists_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    reached(_alloc, _init),
    remaining(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _reached_type =
    sim_interfaces::msg::WaypointList_<ContainerAllocator>;
  _reached_type reached;
  using _remaining_type =
    sim_interfaces::msg::WaypointList_<ContainerAllocator>;
  _remaining_type remaining;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__reached(
    const sim_interfaces::msg::WaypointList_<ContainerAllocator> & _arg)
  {
    this->reached = _arg;
    return *this;
  }
  Type & set__remaining(
    const sim_interfaces::msg::WaypointList_<ContainerAllocator> & _arg)
  {
    this->remaining = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::WaypointLists_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::WaypointLists_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::WaypointLists_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::WaypointLists_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__WaypointLists
    std::shared_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__WaypointLists
    std::shared_ptr<sim_interfaces::msg::WaypointLists_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WaypointLists_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->reached != other.reached) {
      return false;
    }
    if (this->remaining != other.remaining) {
      return false;
    }
    return true;
  }
  bool operator!=(const WaypointLists_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WaypointLists_

// alias to use template instance with default allocator
using WaypointLists =
  sim_interfaces::msg::WaypointLists_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LISTS__STRUCT_HPP_
