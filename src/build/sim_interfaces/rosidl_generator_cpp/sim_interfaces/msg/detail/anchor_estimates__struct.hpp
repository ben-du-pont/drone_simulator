// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:msg/AnchorEstimates.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_HPP_
#define SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_HPP_

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
// Member 'linear_estimate'
// Member 'refined_estimate'
// Member 'final_estimate'
#include "sim_interfaces/msg/detail/anchor_estimate__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_interfaces__msg__AnchorEstimates __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__msg__AnchorEstimates __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AnchorEstimates_
{
  using Type = AnchorEstimates_<ContainerAllocator>;

  explicit AnchorEstimates_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    linear_estimate(_init),
    refined_estimate(_init),
    final_estimate(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anchor_id = "";
    }
  }

  explicit AnchorEstimates_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    anchor_id(_alloc),
    linear_estimate(_alloc, _init),
    refined_estimate(_alloc, _init),
    final_estimate(_alloc, _init)
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
  using _linear_estimate_type =
    sim_interfaces::msg::AnchorEstimate_<ContainerAllocator>;
  _linear_estimate_type linear_estimate;
  using _refined_estimate_type =
    sim_interfaces::msg::AnchorEstimate_<ContainerAllocator>;
  _refined_estimate_type refined_estimate;
  using _final_estimate_type =
    sim_interfaces::msg::AnchorEstimate_<ContainerAllocator>;
  _final_estimate_type final_estimate;

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
  Type & set__linear_estimate(
    const sim_interfaces::msg::AnchorEstimate_<ContainerAllocator> & _arg)
  {
    this->linear_estimate = _arg;
    return *this;
  }
  Type & set__refined_estimate(
    const sim_interfaces::msg::AnchorEstimate_<ContainerAllocator> & _arg)
  {
    this->refined_estimate = _arg;
    return *this;
  }
  Type & set__final_estimate(
    const sim_interfaces::msg::AnchorEstimate_<ContainerAllocator> & _arg)
  {
    this->final_estimate = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__msg__AnchorEstimates
    std::shared_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__msg__AnchorEstimates
    std::shared_ptr<sim_interfaces::msg::AnchorEstimates_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnchorEstimates_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->anchor_id != other.anchor_id) {
      return false;
    }
    if (this->linear_estimate != other.linear_estimate) {
      return false;
    }
    if (this->refined_estimate != other.refined_estimate) {
      return false;
    }
    if (this->final_estimate != other.final_estimate) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnchorEstimates_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnchorEstimates_

// alias to use template instance with default allocator
using AnchorEstimates =
  sim_interfaces::msg::AnchorEstimates_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__MSG__DETAIL__ANCHOR_ESTIMATES__STRUCT_HPP_
