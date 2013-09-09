"""SCPTnvPriority standard property type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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


class SCPTnvPriority(base.Structure):
    """SCPTnvPriority standard property type.  UNVT Flag.  Defines whether
    the NV is of SNVT (=0) or UNVT (=1)."""

    def __init__(self):
        super().__init__(
            key=296,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))
        self._default_bytes = b'\x00'
        self._property_scope, self._property_key = 0, 296
        self._definition = standard.add(self)
    def __set_user_flag(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_user_flag(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    user_flag = property(
        __get_user_flag,
        __set_user_flag,
        None,
        """UNVT Flag.  Defines whether the NV is of SNVT (=0) or UNVT (=1)"""
    )

    def __set_nv(self, v):
        if 0 <= v <= 127:
            self.___bf00._setbits(
                value=v,
                size=7,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..127')

    def __get_nv(self):
        return self.___bf00._getbits(
            size=7,
            offset=1,
            signed=False
        )

    nv = property(
        __get_nv,
        __set_nv,
        None,
        """NV Declaration Index.  The member index from the profile."""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.___bf00(v.___bf00)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 1


if __name__ == '__main__':
    # unit test code.
    item = SCPTnvPriority()
    pass
