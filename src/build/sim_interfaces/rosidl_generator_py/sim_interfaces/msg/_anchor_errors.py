# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_interfaces:msg/AnchorErrors.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AnchorErrors(type):
    """Metaclass of message 'AnchorErrors'."""

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
                'sim_interfaces.msg.AnchorErrors')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__anchor_errors
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__anchor_errors
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__anchor_errors
            cls._TYPE_SUPPORT = module.type_support_msg__msg__anchor_errors
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__anchor_errors

            from sim_interfaces.msg import AnchorError
            if AnchorError.__class__._TYPE_SUPPORT is None:
                AnchorError.__class__.__import_type_support__()

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


class AnchorErrors(metaclass=Metaclass_AnchorErrors):
    """Message class 'AnchorErrors'."""

    __slots__ = [
        '_header',
        '_anchor_id',
        '_linear_error',
        '_nonlinear_error',
        '_final_error',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'anchor_id': 'string',
        'linear_error': 'sim_interfaces/AnchorError',
        'nonlinear_error': 'sim_interfaces/AnchorError',
        'final_error': 'sim_interfaces/AnchorError',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_interfaces', 'msg'], 'AnchorError'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_interfaces', 'msg'], 'AnchorError'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_interfaces', 'msg'], 'AnchorError'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.anchor_id = kwargs.get('anchor_id', str())
        from sim_interfaces.msg import AnchorError
        self.linear_error = kwargs.get('linear_error', AnchorError())
        from sim_interfaces.msg import AnchorError
        self.nonlinear_error = kwargs.get('nonlinear_error', AnchorError())
        from sim_interfaces.msg import AnchorError
        self.final_error = kwargs.get('final_error', AnchorError())

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
        if self.linear_error != other.linear_error:
            return False
        if self.nonlinear_error != other.nonlinear_error:
            return False
        if self.final_error != other.final_error:
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
    def linear_error(self):
        """Message field 'linear_error'."""
        return self._linear_error

    @linear_error.setter
    def linear_error(self, value):
        if __debug__:
            from sim_interfaces.msg import AnchorError
            assert \
                isinstance(value, AnchorError), \
                "The 'linear_error' field must be a sub message of type 'AnchorError'"
        self._linear_error = value

    @builtins.property
    def nonlinear_error(self):
        """Message field 'nonlinear_error'."""
        return self._nonlinear_error

    @nonlinear_error.setter
    def nonlinear_error(self, value):
        if __debug__:
            from sim_interfaces.msg import AnchorError
            assert \
                isinstance(value, AnchorError), \
                "The 'nonlinear_error' field must be a sub message of type 'AnchorError'"
        self._nonlinear_error = value

    @builtins.property
    def final_error(self):
        """Message field 'final_error'."""
        return self._final_error

    @final_error.setter
    def final_error(self, value):
        if __debug__:
            from sim_interfaces.msg import AnchorError
            assert \
                isinstance(value, AnchorError), \
                "The 'final_error' field must be a sub message of type 'AnchorError'"
        self._final_error = value
