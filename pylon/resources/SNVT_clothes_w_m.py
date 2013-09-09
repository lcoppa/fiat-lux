"""SNVT_clothes_w_m standard datapoint type, originally defined in resource
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
# Generated at 06-Sep-2013 08:58.

from pylon.resources import base
from pylon.resources.standard import standard


class SNVT_clothes_w_m(base.Structure):
    """SNVT_clothes_w_m standard datapoint type.  Clothes Washer-Management
    Status.  Provides status of door/lid and drain."""

    def __init__(self):
        super().__init__(
            key=185,
            scope=0
        )

        self.___bf00 = base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))
        self._definition = standard.add(self)

    def __set_door_ajar(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_door_ajar(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    door_ajar = property(
        __get_door_ajar,
        __set_door_ajar,
        None,
        """Door/Lid Ajar.  The door/lid of the washer is not fully closed."""
    )

    def __set_drain_on(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_drain_on(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    drain_on = property(
        __get_drain_on,
        __set_drain_on,
        None,
        """Drain On.  The drain is on."""
    )

    def __set_reserved(self, v):
        if 0 <= v <= 63:
            self.___bf00._setbits(
                value=v,
                size=6,
                offset=2,
                signed=False
            )
        else:
            raise ValueError('Not in range 0..63')

    def __get_reserved(self):
        return self.___bf00._getbits(
            size=6,
            offset=2,
            signed=False
        )

    reserved = property(
        __get_reserved,
        __set_reserved,
        None,
        """This field is reserved.  This field is reserved."""
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
    item = SNVT_clothes_w_m()
    pass
