"""SNVT_alarm standard datapoint type, originally defined in resource file
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


class SNVT_alarm(base.Structure):
    """SNVT_alarm standard datapoint type.  Alarm status."""

    def __init__(self):
        super().__init__(
            key=88,
            scope=0
        )

        self.__location = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(6)
            ]
        )
        self._register(('location', self.__location))

        self.__object_id = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('object_id', self.__object_id))

        self.__alarm_type = alarm_type_t(
        )
        self._register(('alarm_type', self.__alarm_type))

        self.__priority_level = priority_level_t(
        )
        self._register(('priority_level', self.__priority_level))

        self.__index_to_SNVT = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('index_to_SNVT', self.__index_to_SNVT))

        self.__value = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(4)
            ]
        )
        self._register(('value', self.__value))

        self.__year = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=3000
        )
        self._register(('year', self.__year))

        self.__month = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=12
        )
        self._register(('month', self.__month))

        self.__day = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=31
        )
        self._register(('day', self.__day))

        self.__hour = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=23
        )
        self._register(('hour', self.__hour))

        self.__minute = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__second = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('second', self.__second))

        self.__millisecond = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=999
        )
        self._register(('millisecond', self.__millisecond))

        self.__alarm_limit = base.Array(
            [
                base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                ) for i in range(4)
            ]
        )
        self._register(('alarm_limit', self.__alarm_limit))
        self._definition = standard.add(self)


    def __set_location(self, v):
        self.__location._value = v

    location = property(
        lambda self: self.__location._value,
        __set_location,
        None,
        """Location Location code for the node.  (array of 6 bytes.)."""
    )

    def __set_object_id(self, v):
        self.__object_id._value = v

    object_id = property(
        lambda self: self.__object_id._value,
        __set_object_id,
        None,
        """Object ID.  ID of object within node.  (object index.)."""
    )

    def __set_alarm_type(self, v):
        self.__alarm_type._value = v

    alarm_type = property(
        lambda self: self.__alarm_type._value,
        __set_alarm_type,
        None,
        """Alarm type.  (alarm type names.)."""
    )

    def __set_priority_level(self, v):
        self.__priority_level._value = v

    priority_level = property(
        lambda self: self.__priority_level._value,
        __set_priority_level,
        None,
        """Priority level.  (priority level names.)."""
    )

    def __set_index_to_SNVT(self, v):
        self.__index_to_SNVT._value = v

    index_to_SNVT = property(
        lambda self: self.__index_to_SNVT._value,
        __set_index_to_SNVT,
        None,
        """Index of NV.  (index of NV causing alarm.)."""
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None,
        """Value The type of this field is dependent on the NV causing the
        alarm condition.  (array of 4 bytes.)."""
    )

    def __set_year(self, v):
        self.__year._value = v

    year = property(
        lambda self: self.__year._value,
        __set_year,
        None,
        """Year Zero (0) means year not specified.  (years)."""
    )

    def __set_month(self, v):
        self.__month._value = v

    month = property(
        lambda self: self.__month._value,
        __set_month,
        None,
        """Month Zero (0) means month not specified.  (months)."""
    )

    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None,
        """Day Zero (0) means day not specified.  (days)."""
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None,
        """Hour This field uses a 24-hour value.  (hours)."""
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None,
        """Minute (minutes)."""
    )

    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None,
        """Second (seconds)."""
    )

    def __set_millisecond(self, v):
        self.__millisecond._value = v

    millisecond = property(
        lambda self: self.__millisecond._value,
        __set_millisecond,
        None,
        """Millisecond (milliseconds)."""
    )

    def __set_alarm_limit(self, v):
        self.__alarm_limit._value = v

    alarm_limit = property(
        lambda self: self.__alarm_limit._value,
        __set_alarm_limit,
        None,
        """Alarm limit.  The type of this field is dependent on the NV
        causing the alarm condition.  (array of 4 bytes.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_location(v.__location)
        self.__set_object_id(v.__object_id)
        self.__set_alarm_type(v.__alarm_type)
        self.__set_priority_level(v.__priority_level)
        self.__set_index_to_SNVT(v.__index_to_SNVT)
        self.__set_value(v.__value)
        self.__set_year(v.__year)
        self.__set_month(v.__month)
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)
        self.__set_millisecond(v.__millisecond)
        self.__set_alarm_limit(v.__alarm_limit)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 29


if __name__ == '__main__':
    # unit test code.
    item = SNVT_alarm()
    pass
