// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sim_interfaces:msg/AnchorEstimate.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "sim_interfaces/msg/detail/anchor_estimate__struct.h"
#include "sim_interfaces/msg/detail/anchor_estimate__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool sim_interfaces__msg__anchor_estimate__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[51];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("sim_interfaces.msg._anchor_estimate.AnchorEstimate", full_classname_dest, 50) == 0);
  }
  sim_interfaces__msg__AnchorEstimate * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // anchor_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "anchor_id");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->anchor_id, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // position_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_z = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // constant_bias
    PyObject * field = PyObject_GetAttrString(_pymsg, "constant_bias");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->constant_bias = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // linear_bias
    PyObject * field = PyObject_GetAttrString(_pymsg, "linear_bias");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->linear_bias = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_interfaces__msg__anchor_estimate__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of AnchorEstimate */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_interfaces.msg._anchor_estimate");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "AnchorEstimate");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_interfaces__msg__AnchorEstimate * ros_message = (sim_interfaces__msg__AnchorEstimate *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // anchor_id
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->anchor_id.data,
      strlen(ros_message->anchor_id.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "anchor_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // constant_bias
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->constant_bias);
    {
      int rc = PyObject_SetAttrString(_pymessage, "constant_bias", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // linear_bias
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->linear_bias);
    {
      int rc = PyObject_SetAttrString(_pymessage, "linear_bias", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
