# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_interfaces:msg/AnchorError.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AnchorError(type):
    """Metaclass of message 'AnchorError'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('sim_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'sim_interfaces.msg.AnchorError')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__anchor_error
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__anchor_error
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__anchor_error
            cls._TYPE_SUPPORT = module.type_support_msg__msg__anchor_error
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__anchor_error

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnchorError(metaclass=Metaclass_AnchorError):
    """Message class 'AnchorError'."""

    __slots__ = [
        '_header',
        '_anchor_id',
        '_position_error',
        '_constant_bias_error',
        '_linear_bias_error',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'anchor_id': 'string',
        'position_error': 'double',
        'constant_bias_error': 'double',
        'linear_bias_error': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.anchor_id = kwargs.get('anchor_id', str())
        self.position_error = kwargs.get('position_error', float())
        self.constant_bias_error = kwargs.get('constant_bias_error', float())
        self.linear_bias_error = kwargs.get('linear_bias_error', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.anchor_id != other.anchor_id:
            return False
        if self.position_error != other.position_error:
            return False
        if self.constant_bias_error != other.constant_bias_error:
            return False
        if self.linear_bias_error != other.linear_bias_error:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def anchor_id(self):
        """Message field 'anchor_id'."""
        return self._anchor_id

    @anchor_id.setter
    def anchor_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'anchor_id' field must be of type 'str'"
        self._anchor_id = value

    @builtins.property
    def position_error(self):
        """Message field 'position_error'."""
        return self._position_error

    @position_error.setter
    def position_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position_error' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'position_error' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._position_error = value

    @builtins.property
    def constant_bias_error(self):
        """Message field 'constant_bias_error'."""
        return self._constant_bias_error

    @constant_bias_error.setter
    def constant_bias_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'constant_bias_error' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'constant_bias_error' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._constant_bias_error = value

    @builtins.property
    def linear_bias_error(self):
        """Message field 'linear_bias_error'."""
        return self._linear_bias_error

    @linear_bias_error.setter
    def linear_bias_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear_bias_error' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'linear_bias_error' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._linear_bias_error = value
