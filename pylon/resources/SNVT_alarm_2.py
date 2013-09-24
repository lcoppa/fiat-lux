"""SNVT_alarm_2 standard datapoint type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0.  """


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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.alarm_type_t import alarm_type_t
from pylon.resources.priority_level_t import priority_level_t


class SNVT_alarm_2(base.Structure):
    """SNVT_alarm_2 standard datapoint type.  Alarm status 2.  Used to report
    alarm status for a functional block or device.  Replaces SNVT_alarm."""

    def __init__(self):
        super().__init__(
            key=164,
            scope=0
        )

        self.__alarm_type = alarm_type_t(
        )
        self._register(('alarm_type', self.__alarm_type))

        self.__priority_level = priority_level_t(
        )
        self._register(('priority_level', self.__priority_level))

        self.__alarm_time = base.Scaled(
            size=4,
            signed=False,
            invalid=-1,
            minimum=0,
            maximum=-1
        )
        self._register(('alarm_time', self.__alarm_time))

        self.__milliseconds = base.Scaled(
            size=2,
            signed=True,
            invalid=-1,
            minimum=-1,
            maximum=999
        )
        self._register(('milliseconds', self.__milliseconds))

        self.__sequence_number = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('sequence_number', self.__sequence_number))

        self.__description = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=32,
                    maximum=126
                ) for i in range(22)
            ]
        )
        self._register(('description', self.__description))
        self._definition = standard.add(self)


    def __set_alarm_type(self, v):
        self.__alarm_type._value = v

    alarm_type = property(
        lambda self: self.__alarm_type._value,
        __set_alarm_type,
        None,
        """Alarm type.  Alarm condition reported by this update.  (alarm type
        names.)."""
    )

    def __set_priority_level(self, v):
        self.__priority_level._value = v

    priority_level = property(
        lambda self: self.__priority_level._value,
        __set_priority_level,
        None,
        """Priority level.  Priority level of the alarm reported by this
        update.  (priority level names.)."""
    )

    def __set_alarm_time(self, v):
        self.__alarm_time._value = v

    alarm_time = property(
        lambda self: self.__alarm_time._value,
        __set_alarm_time,
        None,
        """Alarm time.  Alarm time in seconds since 2000-01-01T00:00:00Z (the
        0 hour of 1 January 2000, Coordinated Universal Time) (seconds)."""
    )

    def __set_milliseconds(self, v):
        self.__milliseconds._value = v

    milliseconds = property(
        lambda self: self.__milliseconds._value,
        __set_milliseconds,
        None,
        """Milliseconds Alarm time in milliseconds since the second specified
        by the alarm_time field.  (milliseconds)."""
    )

    def __set_sequence_number(self, v):
        self.__sequence_number._value = v

    sequence_number = property(
        lambda self: self.__sequence_number._value,
        __set_sequence_number,
        None,
        """Sequence number.  Sequence number for this update.  Incremented by
        one for each update from an alarm source.  Wraps to zero after
        reaching 255.  An alarm receiver can use the sequence number to
        detect missed alarm messages.  (count)."""
    )

    def __set_description(self, v):
        self.__description._value = v

    description = property(
        lambda self: self.__description._value,
        __set_description,
        None,
        """Description Alarm description with NUL terminator.  The terminator
        is not required if the description requires 22 characters.  May
        include a reference to a language string, delimited by a 0x80 value.
        (array of 22 characters.)."""
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
        self.__set_alarm_time(v.__alarm_time)
        self.__set_milliseconds(v.__milliseconds)
        self.__set_sequence_number(v.__sequence_number)
        self.__set_description(v.__description)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 31


if __name__ == '__main__':
    # unit test code.
    item = SNVT_alarm_2()
    pass
