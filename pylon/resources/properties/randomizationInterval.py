"""randomizationInterval standard property type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.time_sec


class randomizationInterval(pylon.resources.base.Structure):
    """randomizationInterval standard property type.  Randomization
    interval.  Specifies an interval around a scheduled time that is used by
    a scheduler to calculate a random event time.  Used to reduce
    simultaneous startup and shutdown of many devices by multiple
    schedulers."""

    def __init__(self):
        super().__init__(
            key=376,
            scope=0
        )

        self.__earliest_time_offset = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('earliest_time_offset', self.__earliest_time_offset))

        self.__latest_time_offset = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('latest_time_offset', self.__latest_time_offset))
        self._default_bytes = b'\x00\x00\x00\x00'
        self._original_name = 'SCPTrandomizationInterval'
        self._property_scope, self._property_key = 0, 376
        self._definition = standard.add(self)

    def __set_earliest_time_offset(self, v):
        self.__earliest_time_offset._value = v

    earliest_time_offset = property(
        lambda self: self.__earliest_time_offset._value,
        __set_earliest_time_offset,
        None,
        """Earliest time offset."""
    )

    def __set_latest_time_offset(self, v):
        self.__latest_time_offset._value = v

    latest_time_offset = property(
        lambda self: self.__latest_time_offset._value,
        __set_latest_time_offset,
        None,
        """Latest time offset."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_earliest_time_offset(v.__earliest_time_offset)
        self.__set_latest_time_offset(v.__latest_time_offset)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = randomizationInterval()
    pass
