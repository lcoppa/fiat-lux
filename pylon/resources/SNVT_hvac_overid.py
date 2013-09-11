"""SNVT_hvac_overid standard datapoint type, originally defined in resource
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.hvac_overid_t import hvac_overid_t


class SNVT_hvac_overid(base.Structure):
    """SNVT_hvac_overid standard datapoint type.  HVAC override.  (state,
    pct, flow.)."""

    def __init__(self):
        super().__init__(
            key=111,
            scope=0
        )

        self.__state = hvac_overid_t(
        )
        self._register(('state', self.__state))

        self.__percent = base.Scaled(
            size=2,
            signed=True,
            scaling=(0.005, 0),
            invalid=163.835,
            minimum=-163.84,
            maximum=163.835
        )
        self._register(('percent', self.__percent))

        self.__flow = base.Scaled(
            size=2,
            signed=False,
            invalid=65535,
            minimum=0,
            maximum=65535
        )
        self._register(('flow', self.__flow))
        self._definition = standard.add(self)


    def __set_state(self, v):
        self.__state._value = v

    state = property(
        lambda self: self.__state._value,
        __set_state,
        None,
        """HVAC override state.  (override state names.)."""
    )

    def __set_percent(self, v):
        self.__percent._value = v

    percent = property(
        lambda self: self.__percent._value,
        __set_percent,
        None,
        """Percent Position or flow override value.  (% of full scale.)."""
    )

    def __set_flow(self, v):
        self.__flow._value = v

    flow = property(
        lambda self: self.__flow._value,
        __set_flow,
        None,
        """Flow (liters/second)."""
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
        self.__set_percent(v.__percent)
        self.__set_flow(v.__flow)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 5


if __name__ == '__main__':
    # unit test code.
    item = SNVT_hvac_overid()
    pass
