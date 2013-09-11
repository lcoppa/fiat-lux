"""SCPTschedule standard property type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.standard import standard


class SCPTschedule(base.Structure):
    """SCPTschedule standard property type.  Schedule Describes the
    attributes of a daily schedule definition."""

    def __init__(self):
        super().__init__(
            key=274,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))

        self.__time_value_index = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65535
        )
        self._register(('time_value_index', self.__time_value_index))
        self._default_bytes = b'\x7f\xff\xff'
        self._property_scope, self._property_key = 0, 274
        self._definition = standard.add(self)
    def __set_temporary(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_temporary(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    temporary = property(
        __get_temporary,
        __set_temporary,
        None,
        """Temporary flag.  Identifies a temporary schedule.  Temporary
        schedules are deleted at the end of the day that they are active."""
    )

    def __set_schedule_priority(self, v):
        if 0 <= v <= 127:
            self.___bf00._setbits(
                value=v,
                size=7,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..127')

    def __get_schedule_priority(self):
        return self.___bf00._getbits(
            size=7,
            offset=1,
            signed=False
        )

    schedule_priority = property(
        __get_schedule_priority,
        __set_schedule_priority,
        None,
        """Schedule priority.  Specifies the priority for this schedule.  Low
        priority values specify high priority, and high priority values
        specify low priority.  Zero (0) is the highest priority and 255 is
        the lowest."""
    )


    def __set_time_value_index(self, v):
        self.__time_value_index._value = v

    time_value_index = property(
        lambda self: self.__time_value_index._value,
        __set_time_value_index,
        None,
        """Time-value array index.  Identifies the starting entry of a list
        of time-value events in a SCPTscheduleTimeValue array.  The end of
        the list is identified by the terminator field in the
        SCPTscheduleTime entry."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_temporary(v.__temporary)
        self.__set_schedule_priority(v.__schedule_priority)
        self.__set_time_value_index(v.__time_value_index)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SCPTschedule()
    pass
