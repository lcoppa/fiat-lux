"""SCPTweeklySchedule standard property type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SCPTweeklySchedule(base.Structure):
    """SCPTweeklySchedule standard property type.  Weekly schedule.
    Identifies a schedule to be active for each day of the week."""

    def __init__(self):
        super().__init__(
            key=278,
            scope=0
        )

        self.__schedule_index = base.Array(
            [
                base.Scaled(
                    size=2,
                    signed=False,
                    invalid=65535,
                    minimum=0,
                    maximum=65535
                ) for i in range(7)
            ]
        )
        self._register(('schedule_index', self.__schedule_index))
        self._default_bytes = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
            b'\xff\xff\xff'
        self._property_scope, self._property_key = 0, 278
        self._definition = standard.add(self)

    def __set_schedule_index(self, v):
        self.__schedule_index._value = v

    schedule_index = property(
        lambda self: self.__schedule_index._value,
        __set_schedule_index,
        None,
        """Time-value index array.  Identifies the starting entry of a list
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
        self.__set_schedule_index(v.__schedule_index)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 14


if __name__ == '__main__':
    # unit test code.
    item = SCPTweeklySchedule()
    pass
