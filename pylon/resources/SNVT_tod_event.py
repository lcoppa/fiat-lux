"""SNVT_tod_event standard datapoint type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0.  """


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
from pylon.resources.occup_t import occup_t


class SNVT_tod_event(base.Structure):
    """SNVT_tod_event standard datapoint type.  Time of day event.  Occupancy
    scheduling event.  (current, next, time.)."""

    def __init__(self):
        super().__init__(
            key=128,
            scope=0
        )

        self.__current_state = occup_t(
        )
        self._register(('current_state', self.__current_state))

        self.__next_state = occup_t(
        )
        self._register(('next_state', self.__next_state))

        self.__time_to_next_state = base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('time_to_next_state', self.__time_to_next_state))
        self._definition = standard.add(self)


    def __set_current_state(self, v):
        self.__current_state._value = v

    current_state = property(
        lambda self: self.__current_state._value,
        __set_current_state,
        None,
        """Occupancy, current.  (occupancy code names.)."""
    )

    def __set_next_state(self, v):
        self.__next_state._value = v

    next_state = property(
        lambda self: self.__next_state._value,
        __set_next_state,
        None,
        """Occupancy, next.  (occupancy code names.)."""
    )

    def __set_time_to_next_state(self, v):
        self.__time_to_next_state._value = v

    time_to_next_state = property(
        lambda self: self.__time_to_next_state._value,
        __set_time_to_next_state,
        None,
        """Time to next state.  (minutes)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_current_state(v.__current_state)
        self.__set_next_state(v.__next_state)
        self.__set_time_to_next_state(v.__time_to_next_state)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = SNVT_tod_event()
    pass
