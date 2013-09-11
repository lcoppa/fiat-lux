"""SCPTnvDynamicAssignment standard property type, originally defined in
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_nv_type import SNVT_nv_type


class SCPTnvDynamicAssignment(base.Structure):
    """SCPTnvDynamicAssignment standard property type.  Network variable
    dynamic assignment.  Assigns a dynamic network variable to a functional
    block member."""

    def __init__(self):
        super().__init__(
            key=256,
            scope=0
        )

        self.__nv_index = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=4095
        )
        self._register(('nv_index', self.__nv_index))

        self.__fblock_index = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=4095
        )
        self._register(('fblock_index', self.__fblock_index))

        self.__member_number = base.Scaled(
            size=2,
            signed=False,
            minimum=1,
            maximum=4095
        )
        self._register(('member_number', self.__member_number))

        self.__nv_type = SNVT_nv_type(
        )
        self._register(('nv_type', self.__nv_type))
        self._default_bytes = b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00' \
            b'\x00\x00\x00'
        self._property_scope, self._property_key = 0, 256
        self._definition = standard.add(self)

    def __set_nv_index(self, v):
        self.__nv_index._value = v

    nv_index = property(
        lambda self: self.__nv_index._value,
        __set_nv_index,
        None,
        """Network variable index.  Network variable index within the
        device.  (nv index.)."""
    )

    def __set_fblock_index(self, v):
        self.__fblock_index._value = v

    fblock_index = property(
        lambda self: self.__fblock_index._value,
        __set_fblock_index,
        None,
        """Functional block index.  Index of the functional block to which
        the network variable is assigned.  (fblock index.)."""
    )

    def __set_member_number(self, v):
        self.__member_number._value = v

    member_number = property(
        lambda self: self.__member_number._value,
        __set_member_number,
        None,
        """Member number.  Member number of the functional block network
        variable member to which the network variable is assigned.  (nv
        member number.)."""
    )

    def __set_nv_type(self, v):
        self.__nv_type._value = v

    nv_type = property(
        lambda self: self.__nv_type._value,
        __set_nv_type,
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
        self.__set_nv_index(v.__nv_index)
        self.__set_fblock_index(v.__fblock_index)
        self.__set_member_number(v.__member_number)
        self.__set_nv_type(v.__nv_type)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 25


if __name__ == '__main__':
    # unit test code.
    item = SCPTnvDynamicAssignment()
    pass
