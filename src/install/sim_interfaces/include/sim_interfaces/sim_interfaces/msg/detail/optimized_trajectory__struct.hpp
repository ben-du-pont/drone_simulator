// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/OptimizedTrajectory.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_HPP_

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
# define DEPRECATED__sim_interfaces__msg__OptimizedTrajectory __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__OptimizedTrajectory __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct OptimizedTrajectory_
{
  using Type = OptimizedTrajectory_<ContainerAllocator>;

  explicit OptimizedTrajectory_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anchor_id = "";
      this->waypoint_count = 0l;
    }
  }

  explicit OptimizedTrajectory_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    anchor_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anchor_id = "";
      this->waypoint_count = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _anchor_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _anchor_id_type anchor_id;
  using _waypoint_count_type =
    int32_t;
  _waypoint_count_type waypoint_count;
  using _waypoint_x_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoint_x_type waypoint_x;
  using _waypoint_y_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoint_y_type waypoint_y;
  using _waypoint_z_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoint_z_type waypoint_z;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__anchor_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->anchor_id = _arg;
    return *this;
  }
  Type & set__waypoint_count(
    const int32_t & _arg)
  {
    this->waypoint_count = _arg;
    return *this;
  }
  Type & set__waypoint_x(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoint_x = _arg;
    return *this;
  }
  Type & set__waypoint_y(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoint_y = _arg;
    return *this;
  }
  Type & set__waypoint_z(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoint_z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__OptimizedTrajectory
    std::shared_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__OptimizedTrajectory
    std::shared_ptr<sim_interfaces::msg::OptimizedTrajectory_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const OptimizedTrajectory_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->anchor_id != other.anchor_id) {
      return false;
    }
    if (this->waypoint_count != other.waypoint_count) {
      return false;
    }
    if (this->waypoint_x != other.waypoint_x) {
      return false;
    }
    if (this->waypoint_y != other.waypoint_y) {
      return false;
    }
    if (this->waypoint_z != other.waypoint_z) {
      return false;
    }
    return true;
  }
  bool operator!=(const OptimizedTrajectory_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct OptimizedTrajectory_

// alias to use template instance with default allocator
using OptimizedTrajectory =
  sim_interfaces::msg::OptimizedTrajectory_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__OPTIMIZED_TRAJECTORY__STRUCT_HPP_
