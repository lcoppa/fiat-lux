"""SNVT_load_offsets standard datapoint type, originally defined in resource
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
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent


class SNVT_load_offsets(base.Structure):
    """SNVT_load_offsets standard datapoint type.  Load control offsets."""

    def __init__(self):
        super().__init__(
            key=203,
            scope=0
        )

        self.__standby_offset = SNVT_lev_percent(
        )
        self._register(('standby_offset', self.__standby_offset))

        self.__standby_rotation = base.Scaled(
            size=1,
            signed=True,
            scaling=(2, 0),
            invalid=-256,
            minimum=-180,
            maximum=180
        )
        self._register(('standby_rotation', self.__standby_rotation))

        self.__demand_response_offset = SNVT_lev_percent(
        )
        self._register(('demand_response_offset', self.__demand_response_offset))

        self.__demand_response_rotation = base.Scaled(
            size=1,
            signed=True,
            scaling=(2, 0),
            invalid=-256,
            minimum=-180,
            maximum=180
        )
        self._register(('demand_response_rotation', self.__demand_response_rotation))
        self._definition = standard.add(self)


    def __set_standby_offset(self, v):
        self.__standby_offset._value = v

    standby_offset = property(
        lambda self: self.__standby_offset._value,
        __set_standby_offset,
        None,
        """Standby mode offset.  Offset to be applied to a load control value
        during standby mode.  (percent)."""
    )

    def __set_standby_rotation(self, v):
        self.__standby_rotation._value = v

    standby_rotation = property(
        lambda self: self.__standby_rotation._value,
        __set_standby_rotation,
        None,
        """Standby mode rotation setting."""
    )

    def __set_demand_response_offset(self, v):
        self.__demand_response_offset._value = v

    demand_response_offset = property(
        lambda self: self.__demand_response_offset._value,
        __set_demand_response_offset,
        None,
        """Demand response mode offset.  Offset to be applied to a load
        control value during demand-response mode.  (percent)."""
    )

    def __set_demand_response_rotation(self, v):
        self.__demand_response_rotation._value = v

    demand_response_rotation = property(
        lambda self: self.__demand_response_rotation._value,
        __set_demand_response_rotation,
        None,
        """Demand-response mode rotation setting."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_standby_offset(v.__standby_offset)
        self.__set_standby_rotation(v.__standby_rotation)
        self.__set_demand_response_offset(v.__demand_response_offset)
        self.__set_demand_response_rotation(v.__demand_response_rotation)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 6


if __name__ == '__main__':
    # unit test code.
    item = SNVT_load_offsets()
    pass
