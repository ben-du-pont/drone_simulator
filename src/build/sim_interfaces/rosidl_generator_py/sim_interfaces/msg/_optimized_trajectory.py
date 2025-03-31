# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_interfaces:msg/OptimizedTrajectory.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'waypoint_x'
# Member 'waypoint_y'
# Member 'waypoint_z'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_OptimizedTrajectory(type):
    """Metaclass of message 'OptimizedTrajectory'."""

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
                'sim_interfaces.msg.OptimizedTrajectory')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__optimized_trajectory
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__optimized_trajectory
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__optimized_trajectory
            cls._TYPE_SUPPORT = module.type_support_msg__msg__optimized_trajectory
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__optimized_trajectory

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


class OptimizedTrajectory(metaclass=Metaclass_OptimizedTrajectory):
    """Message class 'OptimizedTrajectory'."""

    __slots__ = [
        '_header',
        '_anchor_id',
        '_waypoint_count',
        '_waypoint_x',
        '_waypoint_y',
        '_waypoint_z',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'anchor_id': 'string',
        'waypoint_count': 'int32',
        'waypoint_x': 'sequence<double>',
        'waypoint_y': 'sequence<double>',
        'waypoint_z': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.anchor_id = kwargs.get('anchor_id', str())
        self.waypoint_count = kwargs.get('waypoint_count', int())
        self.waypoint_x = array.array('d', kwargs.get('waypoint_x', []))
        self.waypoint_y = array.array('d', kwargs.get('waypoint_y', []))
        self.waypoint_z = array.array('d', kwargs.get('waypoint_z', []))

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
        if self.waypoint_count != other.waypoint_count:
            return False
        if self.waypoint_x != other.waypoint_x:
            return False
        if self.waypoint_y != other.waypoint_y:
            return False
        if self.waypoint_z != other.waypoint_z:
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
    def waypoint_count(self):
        """Message field 'waypoint_count'."""
        return self._waypoint_count

    @waypoint_count.setter
    def waypoint_count(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waypoint_count' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'waypoint_count' field must be an integer in [-2147483648, 2147483647]"
        self._waypoint_count = value

    @builtins.property
    def waypoint_x(self):
        """Message field 'waypoint_x'."""
        return self._waypoint_x

    @waypoint_x.setter
    def waypoint_x(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'waypoint_x' array.array() must have the type code of 'd'"
            self._waypoint_x = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'waypoint_x' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._waypoint_x = array.array('d', value)

    @builtins.property
    def waypoint_y(self):
        """Message field 'waypoint_y'."""
        return self._waypoint_y

    @waypoint_y.setter
    def waypoint_y(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'waypoint_y' array.array() must have the type code of 'd'"
            self._waypoint_y = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'waypoint_y' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._waypoint_y = array.array('d', value)

    @builtins.property
    def waypoint_z(self):
        """Message field 'waypoint_z'."""
        return self._waypoint_z

    @waypoint_z.setter
    def waypoint_z(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'waypoint_z' array.array() must have the type code of 'd'"
            self._waypoint_z = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'waypoint_z' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._waypoint_z = array.array('d', value)
