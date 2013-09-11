"""UNVT_iot_alarm userdefined datapoint type, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1.  """


# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software" to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file is generated from device resource files using an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.  The machine-generated code may not meet
# compliance with PEP-8 and PEP-257 recommendations at all times.
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.userdefined import userdefined
from pylon.resources.alarm_type_t import alarm_type_t
from pylon.resources.command_priority_t import command_priority_t
from pylon.resources.event_state_t import event_state_t
from pylon.resources.UNVT_iot_timestamp import UNVT_iot_timestamp
from pylon.resources.resource_scope_t import resource_scope_t
from pylon.resources.char_encoding_t import char_encoding_t


class UNVT_iot_alarm(base.Structure):
    """UNVT_iot_alarm userdefined datapoint type.  IoT alarm.  Alarm report
    for a functional block or device."""

    class object_idType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__profile_scope = resource_scope_t(
            )
            self._register(('profile_scope', self.__profile_scope))

            self.__profile_index = base.Scaled(
                size=2,
                signed=False,
                minimum=0,
                maximum=127
            )
            self._register(('profile_index', self.__profile_index))

            self.__block_index = base.Scaled(
                size=2,
                signed=False,
                minimum=0,
                maximum=127
            )
            self._register(('block_index', self.__block_index))

        def __set_profile_scope(self, v):
            self.__profile_scope._value = v

        profile_scope = property(
            lambda self: self.__profile_scope._value,
            __set_profile_scope,
            None,
            """."""
        )

        def __set_profile_index(self, v):
            self.__profile_index._value = v

        profile_index = property(
            lambda self: self.__profile_index._value,
            __set_profile_index,
            None,
            """Profile index.  Index of the profile definition for the
            functional block reporting an error;  specify zero for
            device-level alarms."""
        )

        def __set_block_index(self, v):
            self.__block_index._value = v

        block_index = property(
            lambda self: self.__block_index._value,
            __set_block_index,
            None,
            """Object index.  Object index on the device of the functional
            block reporting an error;  specify the invalid value (0xFFFF) for
            device-level alarms."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_profile_scope(v.__profile_scope)
            self.__set_profile_index(v.__profile_index)
            self.__set_block_index(v.__block_index)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 5

    class text_descriptionType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__field1 = char_encoding_t(
            )
            self._register(('field1', self.__field1))

            self.__description = base.Array(
                [
                    base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=127
                    ) for i in range(120)
                ]
            )
            self._register(('description', self.__description))

        def __set_field1(self, v):
            self.__field1._value = v

        field1 = property(
            lambda self: self.__field1._value,
            __set_field1,
            None,
            """Character encoding.  Character encoding method for the
            descripton field."""
        )

        def __set_description(self, v):
            self.__description._value = v

        description = property(
            lambda self: self.__description._value,
            __set_description,
            None,
            """."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_field1(v.__field1)
            self.__set_description(v.__description)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 121

    def __init__(self):
        super().__init__(
            key=1,
            scope=1
        )

        self.__alarm_type = alarm_type_t(
        )
        self._register(('alarm_type', self.__alarm_type))

        self.__priority_level = command_priority_t(
        )
        self._register(('priority_level', self.__priority_level))

        self.__event_state = event_state_t(
        )
        self._register(('event_state', self.__event_state))

        self.__alarm_time = UNVT_iot_timestamp(
        )
        self._register(('alarm_time', self.__alarm_time))

        self.__sequence_number = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=127
        )
        self._register(('sequence_number', self.__sequence_number))

        self.__object_id = UNVT_iot_alarm.object_idType(
        )
        self._register(('object_id', self.__object_id))

        self.__text_description = UNVT_iot_alarm.text_descriptionType(
        )
        self._register(('text_description', self.__text_description))
        self._definition = userdefined.add(self)


    def __set_alarm_type(self, v):
        self.__alarm_type._value = v

    alarm_type = property(
        lambda self: self.__alarm_type._value,
        __set_alarm_type,
        None,
        """Alarm type.  Reported alarm condition."""
    )

    def __set_priority_level(self, v):
        self.__priority_level._value = v

    priority_level = property(
        lambda self: self.__priority_level._value,
        __set_priority_level,
        None,
        """Priority level.  Reported alarm priority level."""
    )

    def __set_event_state(self, v):
        self.__event_state._value = v

    event_state = property(
        lambda self: self.__event_state._value,
        __set_event_state,
        None,
        """Event state.  Reported alarm event state."""
    )

    def __set_alarm_time(self, v):
        self.__alarm_time._value = v

    alarm_time = property(
        lambda self: self.__alarm_time._value,
        __set_alarm_time,
        None,
        """Alarm time.  Date and time when the alarm occurred."""
    )

    def __set_sequence_number(self, v):
        self.__sequence_number._value = v

    sequence_number = property(
        lambda self: self.__sequence_number._value,
        __set_sequence_number,
        None,
        """Sequence number.  Sequence number for this update;  incremented by
        one for each update from an alarm source;  wraps to zero after
        reaching 0xFF;  an alarm receiver can use the sequence number to
        detect missed alarm messages."""
    )

    def __set_object_id(self, v):
        self.__object_id._value = v

    object_id = property(
        lambda self: self.__object_id._value,
        __set_object_id,
        None,
        """Object ID.  Object identifier for a functional block."""
    )

    def __set_text_description(self, v):
        self.__text_description._value = v

    text_description = property(
        lambda self: self.__text_description._value,
        __set_text_description,
        None,
        """Text description.  Text describing the alarm condition."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_alarm_type(v.__alarm_type)
        self.__set_priority_level(v.__priority_level)
        self.__set_event_state(v.__event_state)
        self.__set_alarm_time(v.__alarm_time)
        self.__set_sequence_number(v.__sequence_number)
        self.__set_object_id(v.__object_id)
        self.__set_text_description(v.__text_description)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 138


if __name__ == '__main__':
    # unit test code.
    item = UNVT_iot_alarm()
    pass
