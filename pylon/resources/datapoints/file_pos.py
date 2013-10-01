"""file_pos standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  """


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


class file_pos(pylon.resources.base.Structure):
    """file_pos standard datapoint type.  File position.  (pointer,
    length.)."""

    def __init__(self):
        super().__init__(
            key=90,
            scope=0
        )

        self.__rw_ptr = pylon.resources.base.Scaled(
            size=4,
            signed=True,
            minimum=0,
            maximum=2147483647
        )
        self._register(('rw_ptr', self.__rw_ptr))

        self.__rw_length = pylon.resources.base.Scaled(
            size=2,
            signed=False,
            minimum=0,
            maximum=65535
        )
        self._register(('rw_length', self.__rw_length))
        self._original_name = 'SNVT_file_pos'
        self._definition = standard.add(self)


    def __set_rw_ptr(self, v):
        self.__rw_ptr._value = v

    rw_ptr = property(
        lambda self: self.__rw_ptr._value,
        __set_rw_ptr,
        None,
        """Read/Write pointer.  (file byte address.)."""
    )

    def __set_rw_length(self, v):
        self.__rw_length._value = v

    rw_length = property(
        lambda self: self.__rw_length._value,
        __set_rw_length,
        None,
        """Read/Write length.  (number of bytes.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_rw_ptr(v.__rw_ptr)
        self.__set_rw_length(v.__rw_length)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = file_pos()
    pass
