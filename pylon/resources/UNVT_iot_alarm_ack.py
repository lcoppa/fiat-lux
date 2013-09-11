"""UNVT_iot_alarm_ack userdefined datapoint type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1.  """


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
from pylon.resources.resource_scope_t import resource_scope_t
from pylon.resources.event_state_t import event_state_t
from pylon.resources.UNVT_iot_timestamp import UNVT_iot_timestamp
from pylon.resources.char_encoding_t import char_encoding_t
from pylon.resources.boolean_t import boolean_t
from pylon.resources.alarm_ack_result_t import alarm_ack_result_t


class UNVT_iot_alarm_ack(base.Structure):
    """UNVT_iot_alarm_ack userdefined datapoint type.  Alarm
    acknowledgement."""

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
            """Profile scope.  Scope of the profile definition for the
            funtional block reporting an error;  specifiy zero for
            device-level alarms."""
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
            """Block index.  Block index on the device of the functional
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

    class acknowledgement_sourceType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__encoding = char_encoding_t(
            )
            self._register(('encoding', self.__encoding))

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

        def __set_encoding(self, v):
            self.__encoding._value = v

        encoding = property(
            lambda self: self.__encoding._value,
            __set_encoding,
            None,
            """Character encoding.  Character encoding method for the
            acknowledgement source."""
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
            self.__set_encoding(v.__encoding)
            self.__set_description(v.__description)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 121

    def __init__(self):
        super().__init__(
            key=3,
            scope=1
        )

        self.__object_id = UNVT_iot_alarm_ack.object_idType(
        )
        self._register(('object_id', self.__object_id))

        self.__event_state_acknowledged = event_state_t(
        )
        self._register(('event_state_acknowledged', self.__event_state_acknowledged))

        self.__alarm_time = UNVT_iot_timestamp(
        )
        self._register(('alarm_time', self.__alarm_time))

        self.__acknowledgement_time = UNVT_iot_timestamp(
        )
        self._register(('acknowledgement_time', self.__acknowledgement_time))

        self.__acknowledgement_source = UNVT_iot_alarm_ack.acknowledgement_sourceType(
        )
        self._register(('acknowledgement_source', self.__acknowledgement_source))

        self.__acknowledgement_result = boolean_t(
        )
        self._register(('acknowledgement_result', self.__acknowledgement_result))

        self.__result_error_type = alarm_ack_result_t(
        )
        self._register(('result_error_type', self.__result_error_type))
        self._definition = userdefined.add(self)


    def __set_object_id(self, v):
        self.__object_id._value = v

    object_id = property(
        lambda self: self.__object_id._value,
        __set_object_id,
        None,
        """Object ID.  Alarm functional block identifier."""
    )

    def __set_event_state_acknowledged(self, v):
        self.__event_state_acknowledged._value = v

    event_state_acknowledged = property(
        lambda self: self.__event_state_acknowledged._value,
        __set_event_state_acknowledged,
        None,
        """Event state acknowldged.  Event state for the acknowledged
        alarm."""
    )

    def __set_alarm_time(self, v):
        self.__alarm_time._value = v

    alarm_time = property(
        lambda self: self.__alarm_time._value,
        __set_alarm_time,
        None,
        """Alarm time.  Date and time when the acknowledged alarm
        occurred."""
    )

    def __set_acknowledgement_time(self, v):
        self.__acknowledgement_time._value = v

    acknowledgement_time = property(
        lambda self: self.__acknowledgement_time._value,
        __set_acknowledgement_time,
        None,
        """Acknowledgement time.  Date and time of the acknowledgement."""
    )

    def __set_acknowledgement_source(self, v):
        self.__acknowledgement_source._value = v

    acknowledgement_source = property(
        lambda self: self.__acknowledgement_source._value,
        __set_acknowledgement_source,
        None,
        """Acknowledgement source.  Text string describing the source of the
        acknowledgement."""
    )

    def __set_acknowledgement_result(self, v):
        self.__acknowledgement_result._value = v

    acknowledgement_result = property(
        lambda self: self.__acknowledgement_result._value,
        __set_acknowledgement_result,
        None,
        """Acknowledgement result.  True if acknowledgement was successful;
        false if an error is reported in result_error_type;  invalid on
        input."""
    )

    def __set_result_error_type(self, v):
        self.__result_error_type._value = v

    result_error_type = property(
        lambda self: self.__result_error_type._value,
        __set_result_error_type,
        None,
        """Acknowledgement error.  Error code if an acknowledgement request
        failed."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_object_id(v.__object_id)
        self.__set_event_state_acknowledged(v.__event_state_acknowledged)
        self.__set_alarm_time(v.__alarm_time)
        self.__set_acknowledgement_time(v.__acknowledgement_time)
        self.__set_acknowledgement_source(v.__acknowledgement_source)
        self.__set_acknowledgement_result(v.__acknowledgement_result)
        self.__set_result_error_type(v.__result_error_type)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 145


if __name__ == '__main__':
    # unit test code.
    item = UNVT_iot_alarm_ack()
    pass
