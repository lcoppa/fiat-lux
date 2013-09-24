"""SNVT_chlr_status standard datapoint type, originally defined in resource
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.chiller_t import chiller_t
from pylon.resources.hvac_t import hvac_t


class SNVT_chlr_status(base.Structure):
    """SNVT_chlr_status standard datapoint type.  Chiller status.  (run mode,
    op mode, state bits.)."""

    class chlr_stateType(base.Structure):

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.___bf00 = base.Scaled(
                size=1,
                signed=False
            )
            self._register(('___bf00', self.___bf00))
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
            """boolean"""
        )

        def __set_run_enabled(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=1
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_run_enabled(self):
            return self.___bf00._getbits(
                size=1,
                offset=1,
                signed=False
            )

        run_enabled = property(
            __get_run_enabled,
            __set_run_enabled,
            None,
            """boolean"""
        )

        def __set_local(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=2
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_local(self):
            return self.___bf00._getbits(
                size=1,
                offset=2,
                signed=False
            )

        local = property(
            __get_local,
            __set_local,
            None,
            """boolean"""
        )

        def __set_limited(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=3
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_limited(self):
            return self.___bf00._getbits(
                size=1,
                offset=3,
                signed=False
            )

        limited = property(
            __get_limited,
            __set_limited,
            None,
            """Limited-condition flag.  Conditions may exist that prevent
            reaching the setpoint.  (boolean)"""
        )

        def __set_chw_flow(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=4
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_chw_flow(self):
            return self.___bf00._getbits(
                size=1,
                offset=4,
                signed=False
            )

        chw_flow = property(
            __get_chw_flow,
            __set_chw_flow,
            None,
            """boolean"""
        )

        def __set_condw_flow(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=5
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_condw_flow(self):
            return self.___bf00._getbits(
                size=1,
                offset=5,
                signed=False
            )

        condw_flow = property(
            __get_condw_flow,
            __set_condw_flow,
            None,
            """boolean"""
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

    def __init__(self):
        super().__init__(
            key=127,
            scope=0
        )

        self.__chlr_run_mode = chiller_t(
        )
        self._register(('chlr_run_mode', self.__chlr_run_mode))

        self.__chlr_op_mode = hvac_t(
        )
        self._register(('chlr_op_mode', self.__chlr_op_mode))

        self.__chlr_state = SNVT_chlr_status.chlr_stateType(
        )
        self._register(('chlr_state', self.__chlr_state))
        self._definition = standard.add(self)


    def __set_chlr_run_mode(self, v):
        self.__chlr_run_mode._value = v

    chlr_run_mode = property(
        lambda self: self.__chlr_run_mode._value,
        __set_chlr_run_mode,
        None,
        """Chiller run mode.  (chiller run mode names.)."""
    )

    def __set_chlr_op_mode(self, v):
        self.__chlr_op_mode._value = v

    chlr_op_mode = property(
        lambda self: self.__chlr_op_mode._value,
        __set_chlr_op_mode,
        None,
        """Chiller operating mode.  (HVAC mode names.)."""
    )

    def __set_chlr_state(self, v):
        self.__chlr_state._value = v

    chlr_state = property(
        lambda self: self.__chlr_state._value,
        __set_chlr_state,
        None,
        """Chiller state flags.  (alarm, enabled, local, limited, chiller
        water flow, condenser water flow.)."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_chlr_run_mode(v.__chlr_run_mode)
        self.__set_chlr_op_mode(v.__chlr_op_mode)
        self.__set_chlr_state(v.__chlr_state)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 3


if __name__ == '__main__':
    # unit test code.
    item = SNVT_chlr_status()
    pass
