// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/WaypointList.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_HPP_

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
# define DEPRECATED__sim_interfaces__msg__WaypointList __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__WaypointList __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WaypointList_
{
  using Type = WaypointList_<ContainerAllocator>;

  explicit WaypointList_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->count = 0l;
    }
  }

  explicit WaypointList_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->count = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _count_type =
    int32_t;
  _count_type count;
  using _x_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _x_type x;
  using _y_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _y_type y;
  using _z_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _z_type z;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__count(
    const int32_t & _arg)
  {
    this->count = _arg;
    return *this;
  }
  Type & set__x(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::WaypointList_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::WaypointList_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::WaypointList_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::WaypointList_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__WaypointList
    std::shared_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__WaypointList
    std::shared_ptr<sim_interfaces::msg::WaypointList_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WaypointList_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->count != other.count) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const WaypointList_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WaypointList_

// alias to use template instance with default allocator
using WaypointList =
  sim_interfaces::msg::WaypointList_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__WAYPOINT_LIST__STRUCT_HPP_
