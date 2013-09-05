"""
    SNVT_switch
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


class SNVT_switch(base.Structure):
    """SNVT_switch  standard datapoint type.

    Switch  (value, state).

    A structure reporting a percentage level or load value and a discrete
    on/off state. Separate fields report the percentage value and state.
    This type should be used for both discrete (on/off) and analog control.

    The value field is used to control the load's value, i.e. position, speed,
    or intensity, the state field being used to control whether the load is on
    or off (enabled or disabled).

    When used as the output of a discrete sensor device, the OFF state is
    represented by a SNVT_switch network variable with state = FALSE and
    value = 0. The other discrete states are represented by state = TRUE and
    value > 0. When used as the output of a two-state sensor device, the ON
    state is represented by state = TRUE and value = 200 (meaning 100%).

    When used as the input of a two-state discrete actuator, a SNVT_switch
    network variable with state = TRUE will be interpreted as the ON state if
    value > 0, and as the OFF state if value = 0. Additionally, a SNVT_switch
    input network variable with state = FALSE should be interpreted as the
    OFF state, whether or not value = 0.
    A state value of 0xFF indicates the switch value is undefined.
    """

    def __init__(self, value=0, state=0):
        super().__init__(
            key=95,
            scope=0
        )

        self._definition = standard.add(self)

        self.__value = base.Scaled(
            size=1,
            signed=False,
            default=value,
            scaling=(0.5, 0),
            minimum=0,
            maximum=200
        )
        self._register(('value', self.__value))

        self.__state = base.Scaled(
            size=1,
            signed=True,
            default=state,
            minimum=-1,
            maximum=+1,
            invalid=-1
        )
        self._register(('state', self.__state))

    def __set_value(self, v):
        self.__value._value = v

    value = property(
        lambda self: self.__value._value,
        __set_value,
        None, """
        Value (%) of full level.
        """
    )

    def __set_state(self, v):
        self.__state._value = v

    state = property(
        lambda self: self.__state._value,
        __set_state,
        None, """
        State (state code). This field can be either -1 (NULL), 0 (OFF) or 1
        (ON).
        """
    )

    def __set(self, v):
        if not isinstance(v, SNVT_switch):
            raise TypeError('Expected instance of SNVT_switch, got {0}'.format(
                type(v)
            ))
        self.__set_value(v.__value)
        self.__set_state(v.__state)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Returns the length of the data type, in bytes."""
        # No need to compute at runtime, as the size is fixed.
        return 2
