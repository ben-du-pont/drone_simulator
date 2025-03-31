# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_interfaces:srv/AnchorInfo.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AnchorInfo_Request(type):
    """Metaclass of message 'AnchorInfo_Request'."""

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
                'sim_interfaces.srv.AnchorInfo_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__anchor_info__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__anchor_info__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__anchor_info__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__anchor_info__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__anchor_info__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnchorInfo_Request(metaclass=Metaclass_AnchorInfo_Request):
    """Message class 'AnchorInfo_Request'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

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
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

# Member 'known_anchor_x_positions'
# Member 'known_anchor_y_positions'
# Member 'known_anchor_z_positions'
# Member 'known_anchor_biases'
# Member 'known_anchor_linear_biases'
# Member 'known_anchor_noise_variances'
# Member 'unknown_anchor_x_positions'
# Member 'unknown_anchor_y_positions'
# Member 'unknown_anchor_z_positions'
# Member 'unknown_anchor_biases'
# Member 'unknown_anchor_linear_biases'
# Member 'unknown_anchor_noise_variances'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_AnchorInfo_Response(type):
    """Metaclass of message 'AnchorInfo_Response'."""

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
                'sim_interfaces.srv.AnchorInfo_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__anchor_info__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__anchor_info__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__anchor_info__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__anchor_info__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__anchor_info__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnchorInfo_Response(metaclass=Metaclass_AnchorInfo_Response):
    """Message class 'AnchorInfo_Response'."""

    __slots__ = [
        '_known_anchor_ids',
        '_known_anchor_x_positions',
        '_known_anchor_y_positions',
        '_known_anchor_z_positions',
        '_known_anchor_biases',
        '_known_anchor_linear_biases',
        '_known_anchor_noise_variances',
        '_unknown_anchor_ids',
        '_unknown_anchor_x_positions',
        '_unknown_anchor_y_positions',
        '_unknown_anchor_z_positions',
        '_unknown_anchor_biases',
        '_unknown_anchor_linear_biases',
        '_unknown_anchor_noise_variances',
    ]

    _fields_and_field_types = {
        'known_anchor_ids': 'sequence<string>',
        'known_anchor_x_positions': 'sequence<double>',
        'known_anchor_y_positions': 'sequence<double>',
        'known_anchor_z_positions': 'sequence<double>',
        'known_anchor_biases': 'sequence<double>',
        'known_anchor_linear_biases': 'sequence<double>',
        'known_anchor_noise_variances': 'sequence<double>',
        'unknown_anchor_ids': 'sequence<string>',
        'unknown_anchor_x_positions': 'sequence<double>',
        'unknown_anchor_y_positions': 'sequence<double>',
        'unknown_anchor_z_positions': 'sequence<double>',
        'unknown_anchor_biases': 'sequence<double>',
        'unknown_anchor_linear_biases': 'sequence<double>',
        'unknown_anchor_noise_variances': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.known_anchor_ids = kwargs.get('known_anchor_ids', [])
        self.known_anchor_x_positions = array.array('d', kwargs.get('known_anchor_x_positions', []))
        self.known_anchor_y_positions = array.array('d', kwargs.get('known_anchor_y_positions', []))
        self.known_anchor_z_positions = array.array('d', kwargs.get('known_anchor_z_positions', []))
        self.known_anchor_biases = array.array('d', kwargs.get('known_anchor_biases', []))
        self.known_anchor_linear_biases = array.array('d', kwargs.get('known_anchor_linear_biases', []))
        self.known_anchor_noise_variances = array.array('d', kwargs.get('known_anchor_noise_variances', []))
        self.unknown_anchor_ids = kwargs.get('unknown_anchor_ids', [])
        self.unknown_anchor_x_positions = array.array('d', kwargs.get('unknown_anchor_x_positions', []))
        self.unknown_anchor_y_positions = array.array('d', kwargs.get('unknown_anchor_y_positions', []))
        self.unknown_anchor_z_positions = array.array('d', kwargs.get('unknown_anchor_z_positions', []))
        self.unknown_anchor_biases = array.array('d', kwargs.get('unknown_anchor_biases', []))
        self.unknown_anchor_linear_biases = array.array('d', kwargs.get('unknown_anchor_linear_biases', []))
        self.unknown_anchor_noise_variances = array.array('d', kwargs.get('unknown_anchor_noise_variances', []))

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
        if self.known_anchor_ids != other.known_anchor_ids:
            return False
        if self.known_anchor_x_positions != other.known_anchor_x_positions:
            return False
        if self.known_anchor_y_positions != other.known_anchor_y_positions:
            return False
        if self.known_anchor_z_positions != other.known_anchor_z_positions:
            return False
        if self.known_anchor_biases != other.known_anchor_biases:
            return False
        if self.known_anchor_linear_biases != other.known_anchor_linear_biases:
            return False
        if self.known_anchor_noise_variances != other.known_anchor_noise_variances:
            return False
        if self.unknown_anchor_ids != other.unknown_anchor_ids:
            return False
        if self.unknown_anchor_x_positions != other.unknown_anchor_x_positions:
            return False
        if self.unknown_anchor_y_positions != other.unknown_anchor_y_positions:
            return False
        if self.unknown_anchor_z_positions != other.unknown_anchor_z_positions:
            return False
        if self.unknown_anchor_biases != other.unknown_anchor_biases:
            return False
        if self.unknown_anchor_linear_biases != other.unknown_anchor_linear_biases:
            return False
        if self.unknown_anchor_noise_variances != other.unknown_anchor_noise_variances:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def known_anchor_ids(self):
        """Message field 'known_anchor_ids'."""
        return self._known_anchor_ids

    @known_anchor_ids.setter
    def known_anchor_ids(self, value):
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
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'known_anchor_ids' field must be a set or sequence and each value of type 'str'"
        self._known_anchor_ids = value

    @builtins.property
    def known_anchor_x_positions(self):
        """Message field 'known_anchor_x_positions'."""
        return self._known_anchor_x_positions

    @known_anchor_x_positions.setter
    def known_anchor_x_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_x_positions' array.array() must have the type code of 'd'"
            self._known_anchor_x_positions = value
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
                "The 'known_anchor_x_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_x_positions = array.array('d', value)

    @builtins.property
    def known_anchor_y_positions(self):
        """Message field 'known_anchor_y_positions'."""
        return self._known_anchor_y_positions

    @known_anchor_y_positions.setter
    def known_anchor_y_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_y_positions' array.array() must have the type code of 'd'"
            self._known_anchor_y_positions = value
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
                "The 'known_anchor_y_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_y_positions = array.array('d', value)

    @builtins.property
    def known_anchor_z_positions(self):
        """Message field 'known_anchor_z_positions'."""
        return self._known_anchor_z_positions

    @known_anchor_z_positions.setter
    def known_anchor_z_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_z_positions' array.array() must have the type code of 'd'"
            self._known_anchor_z_positions = value
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
                "The 'known_anchor_z_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_z_positions = array.array('d', value)

    @builtins.property
    def known_anchor_biases(self):
        """Message field 'known_anchor_biases'."""
        return self._known_anchor_biases

    @known_anchor_biases.setter
    def known_anchor_biases(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_biases' array.array() must have the type code of 'd'"
            self._known_anchor_biases = value
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
                "The 'known_anchor_biases' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_biases = array.array('d', value)

    @builtins.property
    def known_anchor_linear_biases(self):
        """Message field 'known_anchor_linear_biases'."""
        return self._known_anchor_linear_biases

    @known_anchor_linear_biases.setter
    def known_anchor_linear_biases(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_linear_biases' array.array() must have the type code of 'd'"
            self._known_anchor_linear_biases = value
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
                "The 'known_anchor_linear_biases' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_linear_biases = array.array('d', value)

    @builtins.property
    def known_anchor_noise_variances(self):
        """Message field 'known_anchor_noise_variances'."""
        return self._known_anchor_noise_variances

    @known_anchor_noise_variances.setter
    def known_anchor_noise_variances(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'known_anchor_noise_variances' array.array() must have the type code of 'd'"
            self._known_anchor_noise_variances = value
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
                "The 'known_anchor_noise_variances' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._known_anchor_noise_variances = array.array('d', value)

    @builtins.property
    def unknown_anchor_ids(self):
        """Message field 'unknown_anchor_ids'."""
        return self._unknown_anchor_ids

    @unknown_anchor_ids.setter
    def unknown_anchor_ids(self, value):
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
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'unknown_anchor_ids' field must be a set or sequence and each value of type 'str'"
        self._unknown_anchor_ids = value

    @builtins.property
    def unknown_anchor_x_positions(self):
        """Message field 'unknown_anchor_x_positions'."""
        return self._unknown_anchor_x_positions

    @unknown_anchor_x_positions.setter
    def unknown_anchor_x_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_x_positions' array.array() must have the type code of 'd'"
            self._unknown_anchor_x_positions = value
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
                "The 'unknown_anchor_x_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_x_positions = array.array('d', value)

    @builtins.property
    def unknown_anchor_y_positions(self):
        """Message field 'unknown_anchor_y_positions'."""
        return self._unknown_anchor_y_positions

    @unknown_anchor_y_positions.setter
    def unknown_anchor_y_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_y_positions' array.array() must have the type code of 'd'"
            self._unknown_anchor_y_positions = value
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
                "The 'unknown_anchor_y_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_y_positions = array.array('d', value)

    @builtins.property
    def unknown_anchor_z_positions(self):
        """Message field 'unknown_anchor_z_positions'."""
        return self._unknown_anchor_z_positions

    @unknown_anchor_z_positions.setter
    def unknown_anchor_z_positions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_z_positions' array.array() must have the type code of 'd'"
            self._unknown_anchor_z_positions = value
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
                "The 'unknown_anchor_z_positions' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_z_positions = array.array('d', value)

    @builtins.property
    def unknown_anchor_biases(self):
        """Message field 'unknown_anchor_biases'."""
        return self._unknown_anchor_biases

    @unknown_anchor_biases.setter
    def unknown_anchor_biases(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_biases' array.array() must have the type code of 'd'"
            self._unknown_anchor_biases = value
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
                "The 'unknown_anchor_biases' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_biases = array.array('d', value)

    @builtins.property
    def unknown_anchor_linear_biases(self):
        """Message field 'unknown_anchor_linear_biases'."""
        return self._unknown_anchor_linear_biases

    @unknown_anchor_linear_biases.setter
    def unknown_anchor_linear_biases(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_linear_biases' array.array() must have the type code of 'd'"
            self._unknown_anchor_linear_biases = value
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
                "The 'unknown_anchor_linear_biases' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_linear_biases = array.array('d', value)

    @builtins.property
    def unknown_anchor_noise_variances(self):
        """Message field 'unknown_anchor_noise_variances'."""
        return self._unknown_anchor_noise_variances

    @unknown_anchor_noise_variances.setter
    def unknown_anchor_noise_variances(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'unknown_anchor_noise_variances' array.array() must have the type code of 'd'"
            self._unknown_anchor_noise_variances = value
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
                "The 'unknown_anchor_noise_variances' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._unknown_anchor_noise_variances = array.array('d', value)


class Metaclass_AnchorInfo(type):
    """Metaclass of service 'AnchorInfo'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('sim_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'sim_interfaces.srv.AnchorInfo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__anchor_info

            from sim_interfaces.srv import _anchor_info
            if _anchor_info.Metaclass_AnchorInfo_Request._TYPE_SUPPORT is None:
                _anchor_info.Metaclass_AnchorInfo_Request.__import_type_support__()
            if _anchor_info.Metaclass_AnchorInfo_Response._TYPE_SUPPORT is None:
                _anchor_info.Metaclass_AnchorInfo_Response.__import_type_support__()


class AnchorInfo(metaclass=Metaclass_AnchorInfo):
    from sim_interfaces.srv._anchor_info import AnchorInfo_Request as Request
    from sim_interfaces.srv._anchor_info import AnchorInfo_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
