"""sblnd_state standard datapoint type, originally defined in resource file
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
# Generated at 23-Sep-2013 09:14.

import pylon.resources.base
from pylon.resources.standard import standard
import pylon.resources.datapoints.setting
import pylon.resources.enumerations.sblnd_cmd_source_t
import pylon.resources.enumerations.sblnd_error_t


class sblnd_state(pylon.resources.base.Structure):
    """sblnd_state standard datapoint type.  Sunblind State.  Provides the
    present state of a sunblind."""

    def __init__(self):
        super().__init__(
            key=180,
            scope=0
        )

        self.__pos = pylon.resources.datapoints.setting.setting(
        )
        self._register(('pos', self.__pos))

        self.__cmd_source = pylon.resources.enumerations.sblnd_cmd_source_t.sblnd_cmd_source_t(
        )
        self._register(('cmd_source', self.__cmd_source))

        self.__error_code = pylon.resources.enumerations.sblnd_error_t.sblnd_error_t(
        )
        self._register(('error_code', self.__error_code))
        self._original_name = 'SNVT_sblnd_state'
        self._definition = standard.add(self)


    def __set_pos(self, v):
        self.__pos._value = v

    pos = property(
        lambda self: self.__pos._value,
        __set_pos,
        None,
        """."""
    )

    def __set_cmd_source(self, v):
        self.__cmd_source._value = v

    cmd_source = property(
        lambda self: self.__cmd_source._value,
        __set_cmd_source,
        None,
        """."""
    )

    def __set_error_code(self, v):
        self.__error_code._value = v

    error_code = property(
        lambda self: self.__error_code._value,
        __set_error_code,
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
        self.__set_pos(v.__pos)
        self.__set_cmd_source(v.__cmd_source)
        self.__set_error_code(v.__error_code)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = sblnd_state()
    pass
