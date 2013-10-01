"""pumpCharacteristic standard property type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.rpm
import pylon.resources.datapoints.press
import pylon.resources.datapoints.flow_p


class pumpCharacteristic(pylon.resources.base.Structure):
    """pumpCharacteristic standard property type.  Pump characteristic.  The
    basic characteristic data for a pump.  (speedmax, pressmax, flowmax.)."""

    def __init__(self):
        super().__init__(
            key=233,
            scope=0
        )

        self.__speedMax = pylon.resources.datapoints.rpm.rpm(
        )
        self._register(('speedMax', self.__speedMax))

        self.__pressMax = pylon.resources.datapoints.press.press(
        )
        self._register(('pressMax', self.__pressMax))

        self.__flowMax = pylon.resources.datapoints.flow_p.flow_p(
        )
        self._register(('flowMax', self.__flowMax))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00'
        self._original_name = 'SCPTpumpCharacteristic'
        self._property_scope, self._property_key = 0, 233
        self._definition = standard.add(self)

    def __set_speedMax(self, v):
        self.__speedMax._value = v

    speedMax = property(
        lambda self: self.__speedMax._value,
        __set_speedMax,
        None,
        """Maximum speed."""
    )

    def __set_pressMax(self, v):
        self.__pressMax._value = v

    pressMax = property(
        lambda self: self.__pressMax._value,
        __set_pressMax,
        None,
        """Maximum pressure.  Maximum pressure at zero flow."""
    )

    def __set_flowMax(self, v):
        self.__flowMax._value = v

    flowMax = property(
        lambda self: self.__flowMax._value,
        __set_flowMax,
        None,
        """Maximum flow.  maximum flow at zero pressure."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_speedMax(v.__speedMax)
        self.__set_pressMax(v.__pressMax)
        self.__set_flowMax(v.__flowMax)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = pumpCharacteristic()
    pass
