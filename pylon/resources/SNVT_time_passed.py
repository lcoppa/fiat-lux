"""SNVT_time_passed standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  Note this resource is marked as
obsolete.  It should not be used for new development, but continued use in
existing designs is permitted."""


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


class SNVT_time_passed(base.Structure):
    """SNVT_time_passed standard datapoint type.  Elapsed time.  This SNVT is
    obsolete.  Use SNVT_elapsed_tm instead.  (hours, minutes, secs,
    10-msecs.)."""

    def __init__(self):
        super().__init__(
            key=40,
            scope=0
        )

        self.__hours = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('hours', self.__hours))

        self.__minutes = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('minutes', self.__minutes))

        self.__seconds = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=59
        )
        self._register(('seconds', self.__seconds))

        self.__milliseconds = base.Scaled(
            size=1,
            signed=False,
            scaling=(10, 0),
            minimum=0,
            maximum=990
        )
        self._register(('milliseconds', self.__milliseconds))
        self._mark_obsolete()
        self._definition = standard.add(self)


    def __set_hours(self, v):
        self.__hours._value = v

    hours = property(
        lambda self: self.__hours._value,
        __set_hours,
        None,
        """Hours (hours)."""
    )

    def __set_minutes(self, v):
        self.__minutes._value = v

    minutes = property(
        lambda self: self.__minutes._value,
        __set_minutes,
        None,
        """Minutes (minutes)."""
    )

    def __set_seconds(self, v):
        self.__seconds._value = v

    seconds = property(
        lambda self: self.__seconds._value,
        __set_seconds,
        None,
        """Seconds (seconds)."""
    )

    def __set_milliseconds(self, v):
        self.__milliseconds._value = v

    milliseconds = property(
        lambda self: self.__milliseconds._value,
        __set_milliseconds,
        None,
        """Milliseconds (milliseconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_hours(v.__hours)
        self.__set_minutes(v.__minutes)
        self.__set_seconds(v.__seconds)
        self.__set_milliseconds(v.__milliseconds)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SNVT_time_passed()
    pass
