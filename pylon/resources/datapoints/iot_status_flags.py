"""iot_status_flags userdefined datapoint type, originally defined in
resource file set iot 90:00:00:05:00:00:00:00-1.  """


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
from pylon.resources.userdefined import userdefined


class iot_status_flags(pylon.resources.base.Structure):
    """iot_status_flags userdefined datapoint type.  Status flags.  All flags
    are set to zero for normal operation."""

    def __init__(self):
        super().__init__(
            key=5,
            scope=1
        )

        self.___bf00 = pylon.resources.base.Scaled(
            size=1,
            signed=False
        )
        self._register(('___bf00', self.___bf00))
        self._original_name = 'UNVT_iot_status_flags'
        self._definition = userdefined.add(self)

    def __set_in_alarm(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=0
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_in_alarm(self):
        return self.___bf00._getbits(
            size=1,
            offset=0,
            signed=False
        )

    in_alarm = property(
        __get_in_alarm,
        __set_in_alarm,
        None,
        """Bitfield in_alarm"""
    )

    def __set_fault(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=1
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_fault(self):
        return self.___bf00._getbits(
            size=1,
            offset=1,
            signed=False
        )

    fault = property(
        __get_fault,
        __set_fault,
        None,
        """Bitfield fault"""
    )

    def __set_overridden(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=2
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_overridden(self):
        return self.___bf00._getbits(
            size=1,
            offset=2,
            signed=False
        )

    overridden = property(
        __get_overridden,
        __set_overridden,
        None,
        """Overridden flag.  External or local override in effect."""
    )

    def __set_out_of_service(self, v):
        if 0 <= v <= 1:
            self.___bf00._setbits(
                value=v,
                size=1,
                offset=3
            )
        else:
            raise ValueError('Not in range 0..1')

    def __get_out_of_service(self):
        return self.___bf00._getbits(
            size=1,
            offset=3,
            signed=False
        )

    out_of_service = property(
        __get_out_of_service,
        __set_out_of_service,
        None,
        """Bitfield out_of_service"""
    )


    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.___bf00._value = v.___bf00._value

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 1


if __name__ == '__main__':
    # unit test code.
    item = iot_status_flags()
    pass
