"""
    SNVT_preset
"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pylon.resources import base
from pylon.resources.standard import standard

from pylon.resources.learn_mode_t import learn_mode_t


class SNVT_preset(base.Structure):
    """SNVT_preset standard datapoint type.

    Preset  (mode, data, time).

    Network variables of SNVT_preset type are used to allow a sensor or
    actuator functional block to control and adopt one of several programmable
    values and ramp rates, in addition to the normal control mode. For a usage
    example, see the definition for the Closed Loop Sensor
    (SFPTclosedLoopSensor).
    To program a preset, the SNVT_preset output is transmitted from a sensor
    with updated values for SNVT_preset.value, SNVT_preset.selector, and the
    time-related fields. In addition, SNVT_preset.learn is set to
    LN_LEARN_VALUE —or alternatively set to LN_LEARN_CURRENT, which causes the
    receiving actuator to learn whatever its current value is. A pre-programmed
    preset can be selected by transmitting the SNVT_preset output with the
    relevant preset number set in SNVT_preset.selector, and with SNVT_preset.
    learn set to LN_RECALL.
    The time-related fields specify the time period over which the actuator
    should progress from the current level to the newly selected preset level.
    A benefit of this mechanism is that any set of actuators that are preset
    with a common rate value for a particular preset number, will all arrive at
    this new value at the same time, regardless of the individual preset values
    to which they ramp.
    """

    def __init__(self,
                 learn=learn_mode_t.LN_NUL,
                 selector=0,
                 value=(0, 0, 0, 0),
                 day=0,
                 hour=0,
                 minute=0,
                 second=0,
                 millisecond=0):
        super().__init__(
            key=94,
            scope=0
        )
        self._definition = standard.add(self)

        self.__learn = learn_mode_t(learn)
        self._register(('learn', self.__learn))

        self.__selector = base.Scaled(
            size=2,
            signed=False,
            default=selector,
        )
        self._register(('selector', self.__selector))

        self.__value = base.Array(
            elements=(
                base.Scaled(
                    size=1,
                    signed=False,
                    default=value[0]
                ),
                base.Scaled(
                    size=1,
                    signed=False,
                    default=value[1]
                ),
                base.Scaled(
                    size=1,
                    signed=False,
                    default=value[2]
                ),
                base.Scaled(
                    size=1,
                    signed=False,
                    default=value[3]
                )
            )
        )
        self._register(('value', self.__value))

        self.__day = base.Scaled(
            size=2,
            signed=False,
            default=day
        )
        self._register(('day', self.__day))

        self.__hour = base.Scaled(
            size=1,
            signed=False,
            default=hour,
            maximum=23
        )
        self._register(('hour', self.__hour))

        self.__minute = base.Scaled(
            size=1,
            signed=False,
            default=minute,
            maximum=59
        )
        self._register(('minute', self.__minute))

        self.__second = base.Scaled(
            size=1,
            signed=False,
            default=second,
            maximum=59
        )
        self._register(('second', self.__second))

        self.__millisecond = base.Scaled(
            size=2,
            signed=False,
            default=millisecond,
            maximum=999
        )
        self._register(('millisecond', self.__millisecond))

    def __set_learn(self, v):
        self.__learn._value = v

    learn = property(
        lambda self: self.__learn._value,
        __set_learn,
        None, """
        Learn mode  (learn mode names).
        """
    )

    def __set_selector(self, v):
        self.__selector._value = v

    selector = property(
        lambda self: self.__selector._value,
        __set_selector,
        None, """
        Selector  (16-bit unsigned value).  The selector is used to choose
        which preset.
        """
    )

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None, """
        Value  (array of 4 bytes).
        """
    )

    def __set_day(self, v):
        self.__day._value = v

    day = property(
        lambda self: self.__day._value,
        __set_day,
        None, """
        Days  (days).  The value 65535 represents NULL or unknown elapsed time.
        """
    )

    def __set_hour(self, v):
        self.__hour._value = v

    hour = property(
        lambda self: self.__hour._value,
        __set_hour,
        None, """
        Hours  (hours).  This field uses a 24-hour value.
        """
    )

    def __set_minute(self, v):
        self.__minute._value = v

    minute = property(
        lambda self: self.__minute._value,
        __set_minute,
        None, """
        Minutes  (minutes).
        """
    )

    def __set_second(self, v):
        self.__second._value = v

    second = property(
        lambda self: self.__second._value,
        __set_second,
        None, """
        Seconds  (seconds).
        """
    )

    def __set_millisecond(self, v):
        self.__millisecond._value = v

    millisecond = property(
        lambda self: self.__millisecond._value,
        __set_millisecond,
        None, """
        Milliseconds  (milliseconds).
        """
    )

    def __set(self, v):
        if not isinstance(v, SNVT_preset):
            raise TypeError('Expected instance of SNVT_preset, got {0}'.format(
                type(v)
            ))
        self.__set_learn(v.__learn)
        self.__set_selector(v.__selector)
        self.__set_value(v.__value)
        self.__set_day(v.__day)
        self.__set_hour(v.__hour)
        self.__set_minute(v.__minute)
        self.__set_second(v.__second)
        self.__set_millisecond(v.__millisecond)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Returns the length of the data type, in bytes."""
        return 14
