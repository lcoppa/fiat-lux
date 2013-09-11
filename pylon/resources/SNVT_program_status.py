"""SNVT_program_status standard datapoint type, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0.  """


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
from pylon.resources.program_state_t import program_state_t
from pylon.resources.SNVT_elapsed_tm import SNVT_elapsed_tm
from pylon.resources.program_status_error_t import program_status_error_t
from pylon.resources.SNVT_time_stamp import SNVT_time_stamp


class SNVT_program_status(base.Structure):
    """SNVT_program_status standard datapoint type.  Program status.
    Indicates the current status info for the Program object, including
    state, runtime total, and error code with time stamp."""

    def __init__(self):
        super().__init__(
            key=202,
            scope=0
        )

        self.__state = program_state_t(
        )
        self._register(('state', self.__state))

        self.__runtime = SNVT_elapsed_tm(
        )
        self._register(('runtime', self.__runtime))

        self.__last_error = program_status_error_t(
        )
        self._register(('last_error', self.__last_error))

        self.__time_of_last_error = SNVT_time_stamp(
        )
        self._register(('time_of_last_error', self.__time_of_last_error))
        self._definition = standard.add(self)


    def __set_state(self, v):
        self.__state._value = v

    state = property(
        lambda self: self.__state._value,
        __set_state,
        None,
        """."""
    )

    def __set_runtime(self, v):
        self.__runtime._value = v

    runtime = property(
        lambda self: self.__runtime._value,
        __set_runtime,
        None,
        """."""
    )

    def __set_last_error(self, v):
        self.__last_error._value = v

    last_error = property(
        lambda self: self.__last_error._value,
        __set_last_error,
        None,
        """."""
    )

    def __set_time_of_last_error(self, v):
        self.__time_of_last_error._value = v

    time_of_last_error = property(
        lambda self: self.__time_of_last_error._value,
        __set_time_of_last_error,
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
        self.__set_state(v.__state)
        self.__set_runtime(v.__runtime)
        self.__set_last_error(v.__last_error)
        self.__set_time_of_last_error(v.__time_of_last_error)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 16


if __name__ == '__main__':
    # unit test code.
    item = SNVT_program_status()
    pass
