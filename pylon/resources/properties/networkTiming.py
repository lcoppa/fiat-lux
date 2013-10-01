"""networkTiming userdefined property type, originally defined in resource
file set iot 90:00:00:05:00:00:00:00-1."""


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
import pylon.resources.datapoints.time_sec
import pylon.resources.datapoints.lev_percent


class networkTiming(pylon.resources.base.Structure):
    """networkTiming userdefined property type.  Network timing.  Defines
    heartbeat, randomization, throttle, and minimum delta values to control
    propagation of one or more output values;  heartbeat and randomization
    values are specified both for normal operation as well as short periods
    of fast updates."""

    def __init__(self):
        super().__init__(
            key=11,
            scope=1
        )

        self.__standard_heartbeat = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('standard_heartbeat', self.__standard_heartbeat))

        self.__standard_randomization = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('standard_randomization', self.__standard_randomization))

        self.__fast_heartbeat = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('fast_heartbeat', self.__fast_heartbeat))

        self.__fast_randomization = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('fast_randomization', self.__fast_randomization))

        self.__throttle = pylon.resources.datapoints.time_sec.time_sec(
        )
        self._register(('throttle', self.__throttle))

        self.__min_delta = pylon.resources.datapoints.lev_percent.lev_percent(
        )
        self._register(('min_delta', self.__min_delta))
        self._default_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00'
        self._original_name = 'UCPTnetworkTiming'
        self._property_scope, self._property_key = 1, 11
        self._definition = userdefined.add(self)

    def __set_standard_heartbeat(self, v):
        self.__standard_heartbeat._value = v

    standard_heartbeat = property(
        lambda self: self.__standard_heartbeat._value,
        __set_standard_heartbeat,
        None,
        """Standard heartbeat.  The maximum period of time between
        consecutive transmissions of the current value when fast updates are
        not enabled;  used to specify a heartbeat update."""
    )

    def __set_standard_randomization(self, v):
        self.__standard_randomization._value = v

    standard_randomization = property(
        lambda self: self.__standard_randomization._value,
        __set_standard_randomization,
        None,
        """Standard randomization.  An interval of time around the standard
        heartbeat period used to prevent synchronization of heartbeat outputs
        on multiple devices;  a calculated heartbeat time is added to +/- one
        half this interval."""
    )

    def __set_fast_heartbeat(self, v):
        self.__fast_heartbeat._value = v

    fast_heartbeat = property(
        lambda self: self.__fast_heartbeat._value,
        __set_fast_heartbeat,
        None,
        """Fast hearbeat.  The maximum period of time between consecutive
        transmissions of the current value when fast updates are enabled;
        used to specify a heartbeat update."""
    )

    def __set_fast_randomization(self, v):
        self.__fast_randomization._value = v

    fast_randomization = property(
        lambda self: self.__fast_randomization._value,
        __set_fast_randomization,
        None,
        """Fast randomization.  An interval of time around the fast heartbeat
        period used to prevent synchronization of heartbeat outputs on
        multiple devices;  a calculated heartbeat time is added to +/- one
        half this interval."""
    )

    def __set_throttle(self, v):
        self.__throttle._value = v

    throttle = property(
        lambda self: self.__throttle._value,
        __set_throttle,
        None,
        """Throttle The minimum period of time between consecutive
        transmissions of the current value;  used to a throttle an output to
        reduce network bandwidth utilization."""
    )

    def __set_min_delta(self, v):
        self.__min_delta._value = v

    min_delta = property(
        lambda self: self.__min_delta._value,
        __set_min_delta,
        None,
        """Minimum delta.  The minimum percentage change required to force
        transmission of the output value subject to the throttle value;  if
        zero, any change forces transmission subject to the throttle value;
        applies to all value fields for a structure--a transmission is
        triggered if any value field changes by more than the specified delta
        since the last transmission;  for accumulated values such as energy
        (kWh), the percentage is applied to the previous day's accumulated
        value as of the daily freeze time or the meter's rated maximum daily
        accumlated value change if the previous day's accumulated value is
        not available;  set to invalid value to rely on the heartbeat;  if
        the output value is zero, any change to the output value forces
        transmission of the output value if min_delta is valid and non-zero.
        (percent)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_standard_heartbeat(v.__standard_heartbeat)
        self.__set_standard_randomization(v.__standard_randomization)
        self.__set_fast_heartbeat(v.__fast_heartbeat)
        self.__set_fast_randomization(v.__fast_randomization)
        self.__set_throttle(v.__throttle)
        self.__set_min_delta(v.__min_delta)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 12


if __name__ == '__main__':
    # unit test code.
    item = networkTiming()
    pass
