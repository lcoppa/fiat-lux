"""SNVT_clothes_w_c standard datapoint type, originally defined in resource
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
from pylon.resources.appl_cwc_t import appl_cwc_t
from pylon.resources.appl_cws_t import appl_cws_t
from pylon.resources.appl_cwp_t import appl_cwp_t
from pylon.resources.discrete_levels_t import discrete_levels_t
from pylon.resources.boolean_t import boolean_t
from pylon.resources.appl_rin_t import appl_rin_t
from pylon.resources.SNVT_rpm import SNVT_rpm
from pylon.resources.SNVT_time_min import SNVT_time_min


class SNVT_clothes_w_c(base.Structure):
    """SNVT_clothes_w_c standard datapoint type.  Clothes Washer Command.
    Used to program and start a clothes washer."""

    class actionType(base.Structure):

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
        def __set_power_on(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=0,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_power_on(self):
            return self.___bf00._getbits(
                size=1,
                offset=0,
                signed=False
            )

        power_on = property(
            __get_power_on,
            __set_power_on,
            None,
            """Bitfield power_on"""
        )

        def __set_run_mode(self, v):
            if 0 <= v <= 1:
                self.___bf00._setbits(
                    value=v,
                    size=1,
                    offset=1,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..1')

        def __get_run_mode(self):
            return self.___bf00._getbits(
                size=1,
                offset=1,
                signed=False
            )

        run_mode = property(
            __get_run_mode,
            __set_run_mode,
            None,
            """Bitfield run_mode"""
        )

        def __set_rsrvd2_7(self, v):
            if 0 <= v <= 63:
                self.___bf00._setbits(
                    value=v,
                    size=6,
                    offset=2,
                    signed=False
                )
            else:
                raise ValueError('Not in range 0..63')

        def __get_rsrvd2_7(self):
            return self.___bf00._getbits(
                size=6,
                offset=2,
                signed=False
            )

        rsrvd2_7 = property(
            __get_rsrvd2_7,
            __set_rsrvd2_7,
            None,
            """Bitfield rsrvd2_7"""
        )


        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_power_on(v.__power_on)
            self.__set_run_mode(v.__run_mode)
            self.__set_rsrvd2_7(v.__rsrvd2_7)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 1

    class functionType(base.Structure):

        class washType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__load_level = discrete_levels_t(
                )
                self._register(('load_level', self.__load_level))

                self.__temp = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('temp', self.__temp))

                self.__time = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('time', self.__time))

                self.__prewash = boolean_t(
                )
                self._register(('prewash', self.__prewash))

            def __set_load_level(self, v):
                self.__load_level._value = v

            load_level = property(
                lambda self: self.__load_level._value,
                __set_load_level,
                None,
                """."""
            )

            def __set_temp(self, v):
                self.__temp._value = v

            temp = property(
                lambda self: self.__temp._value,
                __set_temp,
                None,
                """."""
            )

            def __set_time(self, v):
                self.__time._value = v

            time = property(
                lambda self: self.__time._value,
                __set_time,
                None,
                """."""
            )

            def __set_prewash(self, v):
                self.__prewash._value = v

            prewash = property(
                lambda self: self.__prewash._value,
                __set_prewash,
                None,
                """."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_load_level(v.__load_level)
                self.__set_temp(v.__temp)
                self.__set_time(v.__time)
                self.__set_prewash(v.__prewash)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 4

        class rinseType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__temp = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('temp', self.__temp))

                self.__repeat = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=9
                )
                self._register(('repeat', self.__repeat))

                self.__option = appl_rin_t(
                )
                self._register(('option', self.__option))

            def __set_temp(self, v):
                self.__temp._value = v

            temp = property(
                lambda self: self.__temp._value,
                __set_temp,
                None,
                """."""
            )

            def __set_repeat(self, v):
                self.__repeat._value = v

            repeat = property(
                lambda self: self.__repeat._value,
                __set_repeat,
                None,
                """."""
            )

            def __set_option(self, v):
                self.__option._value = v

            option = property(
                lambda self: self.__option._value,
                __set_option,
                None,
                """."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_temp(v.__temp)
                self.__set_repeat(v.__repeat)
                self.__set_option(v.__option)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class spinType(base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__speed = SNVT_rpm(
                )
                self._register(('speed', self.__speed))

                self.__time = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=255
                )
                self._register(('time', self.__time))

                self.__hold = boolean_t(
                )
                self._register(('hold', self.__hold))

            def __set_speed(self, v):
                self.__speed._value = v

            speed = property(
                lambda self: self.__speed._value,
                __set_speed,
                None,
                """."""
            )

            def __set_time(self, v):
                self.__time._value = v

            time = property(
                lambda self: self.__time._value,
                __set_time,
                None,
                """."""
            )

            def __set_hold(self, v):
                self.__hold._value = v

            hold = property(
                lambda self: self.__hold._value,
                __set_hold,
                None,
                """."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_speed(v.__speed)
                self.__set_time(v.__time)
                self.__set_hold(v.__hold)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 4

        class dryType(base.Structure):

            class durationType(base.Structure):

                def __init__(self):
                    super().__init__(
                        key=-1,
                        scope=-1
                    )

                    self.__time = base.Scaled(
                        size=1,
                        signed=False,
                        minimum=0,
                        maximum=255
                    )
                    self._register(('time', self.__time))

                    self.__dryness = discrete_levels_t(
                    )
                    self._register(('dryness', self.__dryness))

                def __set_time(self, v):
                    self.__time._value = v

                time = property(
                    lambda self: self.__time._value,
                    __set_time,
                    None,
                    """."""
                )

                def __set_dryness(self, v):
                    self.__dryness._value = v

                dryness = property(
                    lambda self: self.__dryness._value,
                    __set_dryness,
                    None,
                    """."""
                )

                def __set(self, v):
                    if not isinstance(v, type(self)):
                        raise TypeError(
                            'Expected instance of {0}, got {1}'.format(
                                type(self),
                                type(v)
                            )
                        )
                    self.__set_time(v.__time)
                    self.__set_dryness(v.__dryness)

                _value = property(lambda self: self, __set)

                def __len__(self):
                    """Return the length of the type, in bytes."""
                    return 2

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.__temp = base.Scaled(
                    size=1,
                    signed=False,
                    minimum=0,
                    maximum=1
                )
                self._register(('temp', self.__temp))

                self.__duration = SNVT_clothes_w_c.functionType.dryType.durationType(
                )
                self._register(('duration', self.__duration))

            def __set_temp(self, v):
                self.__temp._value = v

            temp = property(
                lambda self: self.__temp._value,
                __set_temp,
                None,
                """."""
            )

            def __set_duration(self, v):
                self.__duration._value = v

            duration = property(
                lambda self: self.__duration._value,
                __set_duration,
                None,
                """."""
            )

            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.__set_temp(v.__temp)
                self.__set_duration(v.__duration)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__program = appl_cwp_t(
            )
            self._register(('program', self.__program))

            self.__wash = SNVT_clothes_w_c.functionType.washType(
            )
            self._register(('wash', self.__wash))

            self.__rinse = SNVT_clothes_w_c.functionType.rinseType(
            )
            self._register(('rinse', self.__rinse))

            self.__spin = SNVT_clothes_w_c.functionType.spinType(
            )
            self._register(('spin', self.__spin))

            self.__dry = SNVT_clothes_w_c.functionType.dryType(
            )
            self._register(('dry', self.__dry))

        def __set_program(self, v):
            self.__program._value = v

        program = property(
            lambda self: self.__program._value,
            __set_program,
            None,
            """."""
        )

        def __set_wash(self, v):
            self.__wash._value = v

        wash = property(
            lambda self: self.__wash._value,
            __set_wash,
            None,
            """."""
        )

        def __set_rinse(self, v):
            self.__rinse._value = v

        rinse = property(
            lambda self: self.__rinse._value,
            __set_rinse,
            None,
            """."""
        )

        def __set_spin(self, v):
            self.__spin._value = v

        spin = property(
            lambda self: self.__spin._value,
            __set_spin,
            None,
            """."""
        )

        def __set_dry(self, v):
            self.__dry._value = v

        dry = property(
            lambda self: self.__dry._value,
            __set_dry,
            None,
            """."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_program(v.__program)
            self.__set_wash(v.__wash)
            self.__set_rinse(v.__rinse)
            self.__set_spin(v.__spin)
            self.__set_dry(v.__dry)

        _value = property(lambda self: self, __set)

        def __len__(self):
            """Return the length of the type, in bytes."""
            return 15

    def __init__(self):
        super().__init__(
            key=184,
            scope=0
        )

        self.__cycle = appl_cwc_t(
        )
        self._register(('cycle', self.__cycle))

        self.__subcycle = appl_cws_t(
        )
        self._register(('subcycle', self.__subcycle))

        self.__rervd = base.Scaled(
            size=1,
            signed=False,
            minimum=0,
            maximum=255
        )
        self._register(('rervd', self.__rervd))

        self.__action = SNVT_clothes_w_c.actionType(
        )
        self._register(('action', self.__action))

        self.__function = SNVT_clothes_w_c.functionType(
        )
        self._register(('function', self.__function))

        self.__time_remaining = SNVT_time_min(
        )
        self._register(('time_remaining', self.__time_remaining))
        self._definition = standard.add(self)


    def __set_cycle(self, v):
        self.__cycle._value = v

    cycle = property(
        lambda self: self.__cycle._value,
        __set_cycle,
        None,
        """."""
    )

    def __set_subcycle(self, v):
        self.__subcycle._value = v

    subcycle = property(
        lambda self: self.__subcycle._value,
        __set_subcycle,
        None,
        """."""
    )

    def __set_rervd(self, v):
        self.__rervd._value = v

    rervd = property(
        lambda self: self.__rervd._value,
        __set_rervd,
        None,
        """."""
    )

    def __set_action(self, v):
        self.__action._value = v

    action = property(
        lambda self: self.__action._value,
        __set_action,
        None,
        """."""
    )

    def __set_function(self, v):
        self.__function._value = v

    function = property(
        lambda self: self.__function._value,
        __set_function,
        None,
        """."""
    )

    def __set_time_remaining(self, v):
        self.__time_remaining._value = v

    time_remaining = property(
        lambda self: self.__time_remaining._value,
        __set_time_remaining,
        None,
        """."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_cycle(v.__cycle)
        self.__set_subcycle(v.__subcycle)
        self.__set_rervd(v.__rervd)
        self.__set_action(v.__action)
        self.__set_function(v.__function)
        self.__set_time_remaining(v.__time_remaining)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 21


if __name__ == '__main__':
    # unit test code.
    item = SNVT_clothes_w_c()
    pass
