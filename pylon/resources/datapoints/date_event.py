"""date_event standard datapoint type, originally defined in resource file
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


class date_event(pylon.resources.base.Structure):
    """date_event standard datapoint type.  Date event.  Reports the status
    of a schedule."""

    def __init__(self):
        super().__init__(
            key=176,
            scope=0
        )

        self.__days_to_active = pylon.resources.base.Scaled(
            size=2,
            signed=True,
            invalid=32767,
            minimum=-32768,
            maximum=32767
        )
        self._register(('days_to_active', self.__days_to_active))

        self.__days_to_inactive = pylon.resources.base.Scaled(
            size=2,
            signed=True,
            invalid=-32768,
            minimum=-32768,
            maximum=32767
        )
        self._register(('days_to_inactive', self.__days_to_inactive))

        self.__name = pylon.resources.base.Array(
            [
                pylon.resources.base.Scaled(
                    size=1,
                    signed=False,
                    minimum=32,
                    maximum=126
                ) for i in range(22)
            ]
        )
        self._register(('name', self.__name))
        self._original_name = 'SNVT_date_event'
        self._definition = standard.add(self)


    def __set_days_to_active(self, v):
        self.__days_to_active._value = v

    days_to_active = property(
        lambda self: self.__days_to_active._value,
        __set_days_to_active,
        None,
        """Days to active.  Number of days until this schedule will be
        active.  Positive if a schedule is inactive;  zero or negative if a
        schedule is active.  (days)."""
    )

    def __set_days_to_inactive(self, v):
        self.__days_to_inactive._value = v

    days_to_inactive = property(
        lambda self: self.__days_to_inactive._value,
        __set_days_to_inactive,
        None,
        """Days to inactive.  Number of days until this schedule will be
        inactive.  Positive if a schedule is active;  zero or negative if a
        schedule is inactive.  (days)."""
    )

    def __set_name(self, v):
        self.__name._value = v

    name = property(
        lambda self: self.__name._value,
        __set_name,
        None,
        """Schedule name.  Nul-terminated schedule name.  The nul terminator
        is not required if the name is 22 characters.  (array of 22
        characters.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_days_to_active(v.__days_to_active)
        self.__set_days_to_inactive(v.__days_to_inactive)
        self.__set_name(v.__name)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 26


if __name__ == '__main__':
    # unit test code.
    item = date_event()
    pass
