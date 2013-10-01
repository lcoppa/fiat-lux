"""time_stamp_p standard datapoint type, originally defined in resource file
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
# Generated at 23-Sep-2013 09:15.

import pylon.resources.base
from pylon.resources.standard import standard


class time_stamp_p(pylon.resources.base.Structure):
    """time_stamp_p standard datapoint type.  Precision timestamp.  Timestamp
    with hundredths of a second resolution.  (seconds)."""

    def __init__(self):
        super().__init__(
            key=192,
            scope=0
        )

        self.__second = pylon.resources.base.Scaled(
            size=4,
            signed=False,
            minimum=0,
            maximum=-1
        )
        self._register(('second', self.__second))

        self.__hundredths = pylon.resources.base.Scaled(
            size=1,
            signed=False,
            scaling=(0.01, 0),
            invalid=2.55,
            minimum=0,
            maximum=0.99
        )
        self._register(('hundredths', self.__hundredths))
        self._original_name = 'SNVT_time_stamp_p'
        self._definition = standard.add(self)


    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None,
        """Time in seconds.  Time in seconds since 2000-01-01T00:00:00Z (the
        0 hour of 1 January 2000, Coordinated Universal Time) (seconds)."""
    )

    def __set_hundredths(self, v):
        self.__hundredths._value = v

    hundredths = property(
        lambda self: self.__hundredths._value,
        __set_hundredths,
        None,
        """Hundredths of a second.  Hundredths portion of a the timestamp.
        (seconds)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_second(v.__second)
        self.__set_hundredths(v.__hundredths)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = time_stamp_p()
    pass
