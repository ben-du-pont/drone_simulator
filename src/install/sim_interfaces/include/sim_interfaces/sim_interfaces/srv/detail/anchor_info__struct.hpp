// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_HPP_
#define SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_interfaces__srv__AnchorInfo_Request __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__srv__AnchorInfo_Request __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AnchorInfo_Request_
{
  using Type = AnchorInfo_Request_<ContainerAllocator>;

  explicit AnchorInfo_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit AnchorInfo_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__srv__AnchorInfo_Request
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__srv__AnchorInfo_Request
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnchorInfo_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnchorInfo_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnchorInfo_Request_

// alias to use template instance with default allocator
using AnchorInfo_Request =
  sim_interfaces::srv::AnchorInfo_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_interfaces


#ifndef _WIN32
# define DEPRECATED__sim_interfaces__srv__AnchorInfo_Response __attribute__((deprecated))
#else
# define DEPRECATED__sim_interfaces__srv__AnchorInfo_Response __declspec(deprecated)
#endif

namespace sim_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AnchorInfo_Response_
{
  using Type = AnchorInfo_Response_<ContainerAllocator>;

  explicit AnchorInfo_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit AnchorInfo_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _known_anchor_ids_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _known_anchor_ids_type known_anchor_ids;
  using _known_anchor_x_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_x_positions_type known_anchor_x_positions;
  using _known_anchor_y_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_y_positions_type known_anchor_y_positions;
  using _known_anchor_z_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_z_positions_type known_anchor_z_positions;
  using _known_anchor_biases_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_biases_type known_anchor_biases;
  using _known_anchor_linear_biases_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_linear_biases_type known_anchor_linear_biases;
  using _known_anchor_noise_variances_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _known_anchor_noise_variances_type known_anchor_noise_variances;
  using _unknown_anchor_ids_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _unknown_anchor_ids_type unknown_anchor_ids;
  using _unknown_anchor_x_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_x_positions_type unknown_anchor_x_positions;
  using _unknown_anchor_y_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_y_positions_type unknown_anchor_y_positions;
  using _unknown_anchor_z_positions_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_z_positions_type unknown_anchor_z_positions;
  using _unknown_anchor_biases_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_biases_type unknown_anchor_biases;
  using _unknown_anchor_linear_biases_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_linear_biases_type unknown_anchor_linear_biases;
  using _unknown_anchor_noise_variances_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _unknown_anchor_noise_variances_type unknown_anchor_noise_variances;

  // setters for named parameter idiom
  Type & set__known_anchor_ids(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->known_anchor_ids = _arg;
    return *this;
  }
  Type & set__known_anchor_x_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_x_positions = _arg;
    return *this;
  }
  Type & set__known_anchor_y_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_y_positions = _arg;
    return *this;
  }
  Type & set__known_anchor_z_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_z_positions = _arg;
    return *this;
  }
  Type & set__known_anchor_biases(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_biases = _arg;
    return *this;
  }
  Type & set__known_anchor_linear_biases(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_linear_biases = _arg;
    return *this;
  }
  Type & set__known_anchor_noise_variances(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->known_anchor_noise_variances = _arg;
    return *this;
  }
  Type & set__unknown_anchor_ids(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->unknown_anchor_ids = _arg;
    return *this;
  }
  Type & set__unknown_anchor_x_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_x_positions = _arg;
    return *this;
  }
  Type & set__unknown_anchor_y_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_y_positions = _arg;
    return *this;
  }
  Type & set__unknown_anchor_z_positions(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_z_positions = _arg;
    return *this;
  }
  Type & set__unknown_anchor_biases(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_biases = _arg;
    return *this;
  }
  Type & set__unknown_anchor_linear_biases(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_linear_biases = _arg;
    return *this;
  }
  Type & set__unknown_anchor_noise_variances(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->unknown_anchor_noise_variances = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_interfaces__srv__AnchorInfo_Response
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_interfaces__srv__AnchorInfo_Response
    std::shared_ptr<sim_interfaces::srv::AnchorInfo_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnchorInfo_Response_ & other) const
  {
    if (this->known_anchor_ids != other.known_anchor_ids) {
      return false;
    }
    if (this->known_anchor_x_positions != other.known_anchor_x_positions) {
      return false;
    }
    if (this->known_anchor_y_positions != other.known_anchor_y_positions) {
      return false;
    }
    if (this->known_anchor_z_positions != other.known_anchor_z_positions) {
      return false;
    }
    if (this->known_anchor_biases != other.known_anchor_biases) {
      return false;
    }
    if (this->known_anchor_linear_biases != other.known_anchor_linear_biases) {
      return false;
    }
    if (this->known_anchor_noise_variances != other.known_anchor_noise_variances) {
      return false;
    }
    if (this->unknown_anchor_ids != other.unknown_anchor_ids) {
      return false;
    }
    if (this->unknown_anchor_x_positions != other.unknown_anchor_x_positions) {
      return false;
    }
    if (this->unknown_anchor_y_positions != other.unknown_anchor_y_positions) {
      return false;
    }
    if (this->unknown_anchor_z_positions != other.unknown_anchor_z_positions) {
      return false;
    }
    if (this->unknown_anchor_biases != other.unknown_anchor_biases) {
      return false;
    }
    if (this->unknown_anchor_linear_biases != other.unknown_anchor_linear_biases) {
      return false;
    }
    if (this->unknown_anchor_noise_variances != other.unknown_anchor_noise_variances) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnchorInfo_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnchorInfo_Response_

// alias to use template instance with default allocator
using AnchorInfo_Response =
  sim_interfaces::srv::AnchorInfo_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_interfaces

namespace sim_interfaces
{

namespace srv
{

struct AnchorInfo
{
  using Request = sim_interfaces::srv::AnchorInfo_Request;
  using Response = sim_interfaces::srv::AnchorInfo_Response;
};

}  // namespace srv

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__STRUCT_HPP_
