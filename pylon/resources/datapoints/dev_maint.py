"""dev_maint standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  """


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
import pylon.resources.enumerations.device_select_t


class dev_maint(pylon.resources.base.Structure):
    """dev_maint standard datapoint type.  Device maintenance.
    Device-maintenance states."""

    class dev_typeType(pylon.resources.base.Union):

        class pump_ctrlType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.___bf00 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf00', self.___bf00))

                self.___bf01 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))
            def __set_service_required(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_service_required(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            service_required = property(
                __get_service_required,
                __set_service_required,
                None,
                """Service required.  Service/maintenance is required.
                (boolean)"""
            )

            def __set_bearings_change(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_bearings_change(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            bearings_change = property(
                __get_bearings_change,
                __set_bearings_change,
                None,
                """Change bearings.  Bearings need to be replaced.
                (boolean)"""
            )

            def __set_bearings_lubricate(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_bearings_lubricate(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            bearings_lubricate = property(
                __get_bearings_lubricate,
                __set_bearings_lubricate,
                None,
                """Lubricate bearings.  Bearings need to be greased.
                (boolean)"""
            )

            def __set_shaftseal_change(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_shaftseal_change(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            shaftseal_change = property(
                __get_shaftseal_change,
                __set_shaftseal_change,
                None,
                """Change shaft seal.  Seal on the shaft needs to be
                replaced.  (boolean)"""
            )

            def __set_reserved1_4_7(self, v):
                if 0 <= v <= 15:
                    self.___bf00._setbits(
                        value=v,
                        size=4,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..15')

            def __get_reserved1_4_7(self):
                return self.___bf00._getbits(
                    size=4,
                    offset=4,
                    signed=False
                )

            reserved1_4_7 = property(
                __get_reserved1_4_7,
                __set_reserved1_4_7,
                None,
                """Bitfield reserved1_4_7"""
            )

            def __set_reserved2_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf01._setbits(
                        value=v,
                        size=8,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..255')

            def __get_reserved2_0_7(self):
                return self.___bf01._getbits(
                    size=8,
                    offset=0,
                    signed=False
                )

            reserved2_0_7 = property(
                __get_reserved2_0_7,
                __set_reserved2_0_7,
                None,
                """Bitfield reserved2_0_7"""
            )

            def __set_reserved3_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf02._setbits(
                        value=v,
                        size=8,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..255')

            def __get_reserved3_0_7(self):
                return self.___bf02._getbits(
                    size=8,
                    offset=0,
                    signed=False
                )

            reserved3_0_7 = property(
                __get_reserved3_0_7,
                __set_reserved3_0_7,
                None,
                """Bitfield reserved3_0_7"""
            )


            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.___bf02._value = v.___bf02._value
                self.___bf01._value = v.___bf01._value
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class valve_posType(pylon.resources.base.Structure):

            def __init__(self):
                super().__init__(
                    key=-1,
                    scope=-1
                )

                self.___bf00 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf00', self.___bf00))

                self.___bf01 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = pylon.resources.base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))
            def __set_motor_maint(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_motor_maint(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            motor_maint = property(
                __get_motor_maint,
                __set_motor_maint,
                None,
                """Motor Maintenance.  The motor requires servicing."""
            )

            def __set_packing_change(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_packing_change(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            packing_change = property(
                __get_packing_change,
                __set_packing_change,
                None,
                """Packing Change.  The packing needs to be controlled or
                changed."""
            )

            def __set_electronics_check(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_electronics_check(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            electronics_check = property(
                __get_electronics_check,
                __set_electronics_check,
                None,
                """Check Electronics.  The electronics need to be checked
                (temperature too high)"""
            )

            def __set_positioning_check(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_positioning_check(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            positioning_check = property(
                __get_positioning_check,
                __set_positioning_check,
                None,
                """Check Position.  The positioning needs to be checked
                (mechanical or electronic)"""
            )

            def __set_lubrication_check(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=4
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_lubrication_check(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            lubrication_check = property(
                __get_lubrication_check,
                __set_lubrication_check,
                None,
                """Check Lubrication.  The lubrication need to be checked."""
            )

            def __set_return_check(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=5
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_return_check(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            return_check = property(
                __get_return_check,
                __set_return_check,
                None,
                """Check Spring-Return Function.  The spring-return function
                needs to be checked."""
            )

            def __set_battery_check(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=6
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_battery_check(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            battery_check = property(
                __get_battery_check,
                __set_battery_check,
                None,
                """Check battery.  The battery needs to be checked."""
            )

            def __set_reserved1_7(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved1_7(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            reserved1_7 = property(
                __get_reserved1_7,
                __set_reserved1_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_reserved2_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf01._setbits(
                        value=v,
                        size=8,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..255')

            def __get_reserved2_0_7(self):
                return self.___bf01._getbits(
                    size=8,
                    offset=0,
                    signed=False
                )

            reserved2_0_7 = property(
                __get_reserved2_0_7,
                __set_reserved2_0_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_reserved3_0_6(self, v):
                if 0 <= v <= 127:
                    self.___bf02._setbits(
                        value=v,
                        size=7,
                        offset=0
                    )
                else:
                    raise ValueError('Not in range 0..127')

            def __get_reserved3_0_6(self):
                return self.___bf02._getbits(
                    size=7,
                    offset=0,
                    signed=False
                )

            reserved3_0_6 = property(
                __get_reserved3_0_6,
                __set_reserved3_0_6,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_general_maint(self, v):
                if 0 <= v <= 1:
                    self.___bf02._setbits(
                        value=v,
                        size=1,
                        offset=7
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_general_maint(self):
                return self.___bf02._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            general_maint = property(
                __get_general_maint,
                __set_general_maint,
                None,
                """General Maintenance.  General Maintenance needs to be
                performed.  Please consult the documentation or your
                Maintenance Department."""
            )


            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.___bf02._value = v.___bf02._value
                self.___bf01._value = v.___bf01._value
                self.___bf00._value = v.___bf00._value

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__pump_ctrl = dev_maint.dev_typeType.pump_ctrlType(
            )
            self._register(('pump_ctrl', self.__pump_ctrl))

            self.__valve_pos = dev_maint.dev_typeType.valve_posType(
            )
            self._register(('valve_pos', self.__valve_pos))

        def __set_pump_ctrl(self, v):
            self.__pump_ctrl._value = v

        pump_ctrl = property(
            lambda self: self.__pump_ctrl._value,
            __set_pump_ctrl,
            None,
            """Pump controller device maintenance state."""
        )

        def __set_valve_pos(self, v):
            self.__valve_pos._value = v

        valve_pos = property(
            lambda self: self.__valve_pos._value,
            __set_valve_pos,
            None,
            """Valve positioner device maintenance information."""
        )

        def __set(self, v):
            if not isinstance(v, type(self)):
                raise TypeError(
                    'Expected instance of {0}, got {1}'.format(
                        type(self),
                        type(v)
                    )
                )
            self.__set_pump_ctrl(v.__pump_ctrl)
            self.__set_valve_pos(v.__valve_pos)

        _value = property(lambda self: self, __set)

    def __init__(self):
        super().__init__(
            key=175,
            scope=0
        )

        self.__device_select = pylon.resources.enumerations.device_select_t.device_select_t(
        )
        self._register(('device_select', self.__device_select))

        self.__dev_type = dev_maint.dev_typeType(
        )
        self._register(('dev_type', self.__dev_type))
        self._original_name = 'SNVT_dev_maint'
        self._definition = standard.add(self)


    def __set_device_select(self, v):
        self.__device_select._value = v

    device_select = property(
        lambda self: self.__device_select._value,
        __set_device_select,
        None,
        """Device selection.  Determines the interpretation of the
        network-variable content.  (device selection names.)."""
    )

    def __set_dev_type(self, v):
        self.__dev_type._value = v

    dev_type = property(
        lambda self: self.__dev_type._value,
        __set_dev_type,
        None,
        """Union of device maintenance state structures for various
        devices."""
    )

    def __set(self, v):
        if not isinstance(v, type(self)):
            raise TypeError(
                'Expected instance of {0}, got {1}'.format(
                    type(self),
                    type(v)
                )
            )
        self.__set_device_select(v.__device_select)
        self.__set_dev_type(v.__dev_type)

    _value = property(lambda self: self, __set)

    def __len__(self):
        """Return the length of the type, in bytes."""
        return 4


if __name__ == '__main__':
    # unit test code.
    item = dev_maint()
    pass
