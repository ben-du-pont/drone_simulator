// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/StampedFloat.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_HPP_

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
# define DEPRECATED__sim_interfaces__msg__StampedFloat __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__StampedFloat __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StampedFloat_
{
  using Type = StampedFloat_<ContainerAllocator>;

  explicit StampedFloat_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  explicit StampedFloat_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _data_type =
    double;
  _data_type data;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__data(
    const double & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::StampedFloat_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::StampedFloat_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::StampedFloat_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::StampedFloat_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__StampedFloat
    std::shared_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__StampedFloat
    std::shared_ptr<sim_interfaces::msg::StampedFloat_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StampedFloat_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const StampedFloat_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StampedFloat_

// alias to use template instance with default allocator
using StampedFloat =
  sim_interfaces::msg::StampedFloat_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__STAMPED_FLOAT__STRUCT_HPP_
