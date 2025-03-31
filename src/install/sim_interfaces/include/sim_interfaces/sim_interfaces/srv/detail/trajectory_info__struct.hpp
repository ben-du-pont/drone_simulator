// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:srv/TrajectoryInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_HPP_
#define SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Request __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Request __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TrajectoryInfo_Request_
{
  using Type = TrajectoryInfo_Request_<ContainerAllocator>;

  explicit TrajectoryInfo_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit TrajectoryInfo_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Request
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Request
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrajectoryInfo_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrajectoryInfo_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrajectoryInfo_Request_

// alias to use template instance with default allocator
using TrajectoryInfo_Request =
  sim_interfaces::srv::TrajectoryInfo_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_interfaces


#ifndef _WIN32
# define DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Response __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Response __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TrajectoryInfo_Response_
{
  using Type = TrajectoryInfo_Response_<ContainerAllocator>;

  explicit TrajectoryInfo_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TrajectoryInfo_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _waypoints_x_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoints_x_type waypoints_x;
  using _waypoints_y_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoints_y_type waypoints_y;
  using _waypoints_z_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _waypoints_z_type waypoints_z;

  // setters for named parameter idiom
  Type & set__waypoints_x(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoints_x = _arg;
    return *this;
  }
  Type & set__waypoints_y(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoints_y = _arg;
    return *this;
  }
  Type & set__waypoints_z(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->waypoints_z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Response
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__srv__TrajectoryInfo_Response
    std::shared_ptr<sim_interfaces::srv::TrajectoryInfo_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrajectoryInfo_Response_ & other) const
  {
    if (this->waypoints_x != other.waypoints_x) {
      return false;
    }
    if (this->waypoints_y != other.waypoints_y) {
      return false;
    }
    if (this->waypoints_z != other.waypoints_z) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrajectoryInfo_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrajectoryInfo_Response_

// alias to use template instance with default allocator
using TrajectoryInfo_Response =
  sim_interfaces::srv::TrajectoryInfo_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_interfaces

namespace sim_interfaces
{

namespace srv
{

struct TrajectoryInfo
{
  using Request = sim_interfaces::srv::TrajectoryInfo_Request;
  using Response = sim_interfaces::srv::TrajectoryInfo_Response;
};

}  // namespace srv

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__SRV__DETAIL__TRAJECTORY_INFO__STRUCT_HPP_
