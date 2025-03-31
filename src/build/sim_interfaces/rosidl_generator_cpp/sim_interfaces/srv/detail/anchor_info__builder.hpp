// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_interfaces:srv/AnchorInfo.idl
// generated code does not contain a copyright notice

#ifndef SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__BUILDER_HPP_
#define SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_interfaces/srv/detail/anchor_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::srv::AnchorInfo_Request>()
{
  return ::sim_interfaces::srv::AnchorInfo_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace sim_interfaces


namespace sim_interfaces
{

namespace srv
{

namespace builder
{

class Init_AnchorInfo_Response_unknown_anchor_noise_variances
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_noise_variances(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  ::sim_interfaces::srv::AnchorInfo_Response unknown_anchor_noise_variances(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_noise_variances_type arg)
  {
    msg_.unknown_anchor_noise_variances = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_linear_biases
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_linear_biases(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_noise_variances unknown_anchor_linear_biases(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_linear_biases_type arg)
  {
    msg_.unknown_anchor_linear_biases = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_noise_variances(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_biases
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_biases(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_linear_biases unknown_anchor_biases(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_biases_type arg)
  {
    msg_.unknown_anchor_biases = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_linear_biases(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_z_positions
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_z_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_biases unknown_anchor_z_positions(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_z_positions_type arg)
  {
    msg_.unknown_anchor_z_positions = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_biases(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_y_positions
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_y_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_z_positions unknown_anchor_y_positions(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_y_positions_type arg)
  {
    msg_.unknown_anchor_y_positions = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_z_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_x_positions
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_x_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_y_positions unknown_anchor_x_positions(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_x_positions_type arg)
  {
    msg_.unknown_anchor_x_positions = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_y_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_unknown_anchor_ids
{
public:
  explicit Init_AnchorInfo_Response_unknown_anchor_ids(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_x_positions unknown_anchor_ids(::sim_interfaces::srv::AnchorInfo_Response::_unknown_anchor_ids_type arg)
  {
    msg_.unknown_anchor_ids = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_x_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_noise_variances
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_noise_variances(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_unknown_anchor_ids known_anchor_noise_variances(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_noise_variances_type arg)
  {
    msg_.known_anchor_noise_variances = std::move(arg);
    return Init_AnchorInfo_Response_unknown_anchor_ids(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_linear_biases
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_linear_biases(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_known_anchor_noise_variances known_anchor_linear_biases(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_linear_biases_type arg)
  {
    msg_.known_anchor_linear_biases = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_noise_variances(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_biases
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_biases(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_known_anchor_linear_biases known_anchor_biases(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_biases_type arg)
  {
    msg_.known_anchor_biases = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_linear_biases(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_z_positions
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_z_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_known_anchor_biases known_anchor_z_positions(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_z_positions_type arg)
  {
    msg_.known_anchor_z_positions = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_biases(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_y_positions
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_y_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_known_anchor_z_positions known_anchor_y_positions(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_y_positions_type arg)
  {
    msg_.known_anchor_y_positions = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_z_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_x_positions
{
public:
  explicit Init_AnchorInfo_Response_known_anchor_x_positions(::sim_interfaces::srv::AnchorInfo_Response & msg)
  : msg_(msg)
  {}
  Init_AnchorInfo_Response_known_anchor_y_positions known_anchor_x_positions(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_x_positions_type arg)
  {
    msg_.known_anchor_x_positions = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_y_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

class Init_AnchorInfo_Response_known_anchor_ids
{
public:
  Init_AnchorInfo_Response_known_anchor_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnchorInfo_Response_known_anchor_x_positions known_anchor_ids(::sim_interfaces::srv::AnchorInfo_Response::_known_anchor_ids_type arg)
  {
    msg_.known_anchor_ids = std::move(arg);
    return Init_AnchorInfo_Response_known_anchor_x_positions(msg_);
  }

private:
  ::sim_interfaces::srv::AnchorInfo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_interfaces::srv::AnchorInfo_Response>()
{
  return sim_interfaces::srv::builder::Init_AnchorInfo_Response_known_anchor_ids();
}

}  // namespace sim_interfaces

#endif  // SIM_INTERFACES__SRV__DETAIL__ANCHOR_INFO__BUILDER_HPP_
