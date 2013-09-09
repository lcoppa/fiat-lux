"""SNVT_dev_status standard datapoint type, originally defined in resource
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
from pylon.resources.device_select_t import device_select_t


class SNVT_dev_status(base.Structure):
    """SNVT_dev_status standard datapoint type.  Device status.  Status of
    the device."""

    class dev_typeType(base.Union):

        class pump_ctrlType(base.Structure):

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

                self.___bf01 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))
            def __set_device_fault(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_device_fault(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            device_fault = property(
                __get_device_fault,
                __set_device_fault,
                None,
                """Pump controller fault.  See SNVT_pump_fault network
                variable declaration on device.  (boolean)"""
            )

            def __set_supply_fault(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_supply_fault(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            supply_fault = property(
                __get_supply_fault,
                __set_supply_fault,
                None,
                """Supply fault.  No electrical power, no fluid in pump,
                etc.  See SNVT_pump_fault network variable declaration on
                device.  (boolean)"""
            )

            def __set_reserved1_2(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved1_2(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            reserved1_2 = property(
                __get_reserved1_2,
                __set_reserved1_2,
                None,
                """Bitfield reserved1_2"""
            )

            def __set_speed_low(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_speed_low(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            speed_low = property(
                __get_speed_low,
                __set_speed_low,
                None,
                """Low-speed limit of pump.  Pump is running at the lowest
                possible speed, therefore the requested performance is not
                possible.  (boolean)"""
            )

            def __set_speed_high(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_speed_high(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            speed_high = property(
                __get_speed_high,
                __set_speed_high,
                None,
                """High-speed limit of pump.  Pump is running at the highest
                possible speed, therefore the requested performance is not
                possible.  (boolean)"""
            )

            def __set_reserved1_5(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=5,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved1_5(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            reserved1_5 = property(
                __get_reserved1_5,
                __set_reserved1_5,
                None,
                """Bitfield reserved1_5"""
            )

            def __set_setpt_out_of_range(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=6,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_setpt_out_of_range(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            setpt_out_of_range = property(
                __get_setpt_out_of_range,
                __set_setpt_out_of_range,
                None,
                """Setpoint out of range.  Chosen override setpoint value is
                lower than the manufacturer-defined low-setpoint limit or
                higher than the manufacturer-defined high-setpoint limit.
                (boolean)"""
            )

            def __set_reserved1_7(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=7,
                        signed=False
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
                """Bitfield reserved1_7"""
            )

            def __set_local_control(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_local_control(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            local_control = property(
                __get_local_control,
                __set_local_control,
                None,
                """Locally controlled pump.  Pump is locally operated
                (hardware override) (boolean)"""
            )

            def __set_reserved2_1(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved2_1(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            reserved2_1 = property(
                __get_reserved2_1,
                __set_reserved2_1,
                None,
                """Bitfield reserved2_1"""
            )

            def __set_running(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=2,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_running(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            running = property(
                __get_running,
                __set_running,
                None,
                """Running pump.  Pump is presently running.  (boolean)"""
            )

            def __set_reserved2_3(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=3,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved2_3(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            reserved2_3 = property(
                __get_reserved2_3,
                __set_reserved2_3,
                None,
                """Bitfield reserved2_3"""
            )

            def __set_remote_press(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_remote_press(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            remote_press = property(
                __get_remote_press,
                __set_remote_press,
                None,
                """Remote pressure sensor.  Pump controller is using a remote
                pressure sensor.  (boolean)"""
            )

            def __set_remote_flow(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=5,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_remote_flow(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            remote_flow = property(
                __get_remote_flow,
                __set_remote_flow,
                None,
                """Remote flow sensor.  Pump controller is using a remote
                flow sensor.  (boolean)"""
            )

            def __set_remote_temp(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=6,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_remote_temp(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=6,
                    signed=False
                )

            remote_temp = property(
                __get_remote_temp,
                __set_remote_temp,
                None,
                """Remote temperature sensor.  Pump controller is using a
                remote temperature sensor.  (boolean)"""
            )

            def __set_reserved2_7(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=7,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved2_7(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=7,
                    signed=False
                )

            reserved2_7 = property(
                __get_reserved2_7,
                __set_reserved2_7,
                None,
                """Bitfield reserved2_7"""
            )

            def __set_reserved3_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf02._setbits(
                        value=v,
                        size=8,
                        offset=0,
                        signed=False
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
                self.___bf02(v.___bf02)
                self.___bf01(v.___bf01)
                self.___bf00(v.___bf00)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        class valve_posType(base.Structure):

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

                self.___bf01 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf01', self.___bf01))

                self.___bf02 = base.Scaled(
                    size=1,
                    signed=False
                )
                self._register(('___bf02', self.___bf02))
            def __set_running(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_running(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            running = property(
                __get_running,
                __set_running,
                None,
                """Valve Running.  Valve is presently being positioned."""
            )

            def __set_adapting(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_adapting(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            adapting = property(
                __get_adapting,
                __set_adapting,
                None,
                """Adapting Valve is presently adapting."""
            )

            def __set_initializing(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=2,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_initializing(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=2,
                    signed=False
                )

            initializing = property(
                __get_initializing,
                __set_initializing,
                None,
                """Initializing Valve is presently initializing."""
            )

            def __set_local_control(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=3,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_local_control(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=3,
                    signed=False
                )

            local_control = property(
                __get_local_control,
                __set_local_control,
                None,
                """Local Control.  The valve operation is being locally
                controlled."""
            )

            def __set_setpt_out_of_range(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=4,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_setpt_out_of_range(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=4,
                    signed=False
                )

            setpt_out_of_range = property(
                __get_setpt_out_of_range,
                __set_setpt_out_of_range,
                None,
                """Setpoint out of range.  Chosen override setpoint value is
                lower than the manufacturer-defined low-setpoint limit or
                higher than the manufacturer-defined high-setpoint limit."""
            )

            def __set_remote_ctrl_signal(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=1,
                        offset=5,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_remote_ctrl_signal(self):
                return self.___bf00._getbits(
                    size=1,
                    offset=5,
                    signed=False
                )

            remote_ctrl_signal = property(
                __get_remote_ctrl_signal,
                __set_remote_ctrl_signal,
                None,
                """Remote Control Signal.  The remote-control signal is
                active."""
            )

            def __set_reserved1_6_7(self, v):
                if 0 <= v <= 1:
                    self.___bf00._setbits(
                        value=v,
                        size=2,
                        offset=6,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved1_6_7(self):
                return self.___bf00._getbits(
                    size=2,
                    offset=6,
                    signed=False
                )

            reserved1_6_7 = property(
                __get_reserved1_6_7,
                __set_reserved1_6_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_hw_emergency(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=0,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_hw_emergency(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=0,
                    signed=False
                )

            hw_emergency = property(
                __get_hw_emergency,
                __set_hw_emergency,
                None,
                """Hardware Emergency.  The hardware-emergency state is
                active."""
            )

            def __set_sw_emergency(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=1,
                        offset=1,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_sw_emergency(self):
                return self.___bf01._getbits(
                    size=1,
                    offset=1,
                    signed=False
                )

            sw_emergency = property(
                __get_sw_emergency,
                __set_sw_emergency,
                None,
                """Software Emergency.  The software-emergency state is
                active."""
            )

            def __set_reserved2_2_7(self, v):
                if 0 <= v <= 1:
                    self.___bf01._setbits(
                        value=v,
                        size=6,
                        offset=2,
                        signed=False
                    )
                else:
                    raise ValueError('Not in range 0..1')

            def __get_reserved2_2_7(self):
                return self.___bf01._getbits(
                    size=6,
                    offset=2,
                    signed=False
                )

            reserved2_2_7 = property(
                __get_reserved2_2_7,
                __set_reserved2_2_7,
                None,
                """This field is reserved.  This field is reserved."""
            )

            def __set_reserved3_0_7(self, v):
                if 0 <= v <= 255:
                    self.___bf02._setbits(
                        value=v,
                        size=8,
                        offset=0,
                        signed=False
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
                """This field is reserved.  This field is reserved."""
            )


            def __set(self, v):
                if not isinstance(v, type(self)):
                    raise TypeError(
                        'Expected instance of {0}, got {1}'.format(
                            type(self),
                            type(v)
                        )
                    )
                self.___bf02(v.___bf02)
                self.___bf01(v.___bf01)
                self.___bf00(v.___bf00)

            _value = property(lambda self: self, __set)

            def __len__(self):
                """Return the length of the type, in bytes."""
                return 3

        def __init__(self):
            super().__init__(
                key=-1,
                scope=-1
            )

            self.__pump_ctrl = SNVT_dev_status.dev_typeType.pump_ctrlType(
            )
            self._register(('pump_ctrl', self.__pump_ctrl))

            self.__valve_pos = SNVT_dev_status.dev_typeType.valve_posType(
            )
            self._register(('valve_pos', self.__valve_pos))

        def __set_pump_ctrl(self, v):
            self.__pump_ctrl._value = v

        pump_ctrl = property(
            lambda self: self.__pump_ctrl._value,
            __set_pump_ctrl,
            None,
            """Pump controller device status."""
        )

        def __set_valve_pos(self, v):
            self.__valve_pos._value = v

        valve_pos = property(
            lambda self: self.__valve_pos._value,
            __set_valve_pos,
            None,
            """Valve positioner device status."""
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
            key=173,
            scope=0
        )

        self.__device_select = device_select_t(
        )
        self._register(('device_select', self.__device_select))

        self.__dev_type = SNVT_dev_status.dev_typeType(
        )
        self._register(('dev_type', self.__dev_type))
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
        """Union of device status for various devices."""
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
    item = SNVT_dev_status()
    pass
