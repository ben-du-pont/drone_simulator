// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/AnchorErrors.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__STRUCT_HPP_

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
// Member 'linear_error'
// Member 'nonlinear_error'
// Member 'final_error'
#include "sim_interfaces/msg/detail/anchor_error__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_interfaces__msg__AnchorErrors __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__AnchorErrors __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AnchorErrors_
{
  using Type = AnchorErrors_<ContainerAllocator>;

  explicit AnchorErrors_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    linear_error(_init),
    nonlinear_error(_init),
    final_error(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anchor_id = "";
    }
  }

  explicit AnchorErrors_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    anchor_id(_alloc),
    linear_error(_alloc, _init),
    nonlinear_error(_alloc, _init),
    final_error(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anchor_id = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _anchor_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _anchor_id_type anchor_id;
  using _linear_error_type =
    sim_interfaces::msg::AnchorError_<ContainerAllocator>;
  _linear_error_type linear_error;
  using _nonlinear_error_type =
    sim_interfaces::msg::AnchorError_<ContainerAllocator>;
  _nonlinear_error_type nonlinear_error;
  using _final_error_type =
    sim_interfaces::msg::AnchorError_<ContainerAllocator>;
  _final_error_type final_error;

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
  Type & set__linear_error(
    const sim_interfaces::msg::AnchorError_<ContainerAllocator> & _arg)
  {
    this->linear_error = _arg;
    return *this;
  }
  Type & set__nonlinear_error(
    const sim_interfaces::msg::AnchorError_<ContainerAllocator> & _arg)
  {
    this->nonlinear_error = _arg;
    return *this;
  }
  Type & set__final_error(
    const sim_interfaces::msg::AnchorError_<ContainerAllocator> & _arg)
  {
    this->final_error = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::AnchorErrors_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::AnchorErrors_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::AnchorErrors_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::AnchorErrors_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__AnchorErrors
    std::shared_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__AnchorErrors
    std::shared_ptr<sim_interfaces::msg::AnchorErrors_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnchorErrors_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->anchor_id != other.anchor_id) {
      return false;
    }
    if (this->linear_error != other.linear_error) {
      return false;
    }
    if (this->nonlinear_error != other.nonlinear_error) {
      return false;
    }
    if (this->final_error != other.final_error) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnchorErrors_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnchorErrors_

// alias to use template instance with default allocator
using AnchorErrors =
  sim_interfaces::msg::AnchorErrors_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ERRORS__STRUCT_HPP_
