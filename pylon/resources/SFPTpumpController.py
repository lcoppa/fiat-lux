"""SFPTpumpController standard profile, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_dev_c_mode import SNVT_dev_c_mode
from pylon.resources.SNVT_press import SNVT_press
from pylon.resources.SNVT_flow_p import SNVT_flow_p
from pylon.resources.SCPTminRemotePressureSetpoint import SCPTminRemotePressureSetpoint
from pylon.resources.SCPTmaxRemotePressureSetpoint import SCPTmaxRemotePressureSetpoint
from pylon.resources.SCPTminRemoteFlowSetpoint import SCPTminRemoteFlowSetpoint
from pylon.resources.SCPTmaxRemoteFlowSetpoint import SCPTmaxRemoteFlowSetpoint
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SCPTminRemoteTempSetpoint import SCPTminRemoteTempSetpoint
from pylon.resources.SCPTmaxRemoteTempSetpoint import SCPTmaxRemoteTempSetpoint
from pylon.resources.SNVT_dev_status import SNVT_dev_status
from pylon.resources.SNVT_rpm import SNVT_rpm
from pylon.resources.SNVT_time_hour import SNVT_time_hour
from pylon.resources.SNVT_dev_fault import SNVT_dev_fault
from pylon.resources.SNVT_dev_maint import SNVT_dev_maint
from pylon.resources.SNVT_power import SNVT_power
from pylon.resources.SNVT_power_kilo import SNVT_power_kilo
from pylon.resources.SNVT_elec_kwh import SNVT_elec_kwh
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTpumpCharacteristic import SCPTpumpCharacteristic
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTminPressureSetpoint import SCPTminPressureSetpoint
from pylon.resources.SCPTmaxPressureSetpoint import SCPTmaxPressureSetpoint
from pylon.resources.SCPTminFlowSetpoint import SCPTminFlowSetpoint
from pylon.resources.SCPTmaxFlowSetpoint import SCPTmaxFlowSetpoint
from pylon.resources.SCPTdeviceControlMode import SCPTdeviceControlMode
from pylon.resources.SCPTobjMajVer import SCPTobjMajVer
from pylon.resources.SCPTobjMinVer import SCPTobjMinVer


class SFPTpumpController(base.Profile):
    """SFPTpumpController standard profile.  Pump Controller for HVAC
    Applications.  Provides the primary force to distribute and circulate hot
    and chilled water in a variety of space-temperature and air-conditioning
    systems."""

    def __init__(self):
        super().__init__(
            key=8120,
            scope=0
        )
        self.datapoints['nviPumpSetpoint'] = base.Profile.DatapointMember(
            doc="""Pump setpoint for normal operation.  """,
            name='nviPumpSetpoint',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPumpOpMode'] = base.Profile.DatapointMember(
            doc="""Requested pump operating mode.  """,
            name='nviPumpOpMode',
            profile=self,
            number=2,
            datatype=SNVT_hvac_mode,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoPumpCapacity'] = base.Profile.DatapointMember(
            doc="""Pump capacity in percent.  """,
            name='nvoPumpCapacity',
            profile=self,
            number=3,
            datatype=SNVT_lev_percent,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffOpMode'] = base.Profile.DatapointMember(
            doc="""Effective operating mode.  """,
            name='nvoEffOpMode',
            profile=self,
            number=4,
            datatype=SNVT_hvac_mode,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoControlMode'] = base.Profile.DatapointMember(
            doc="""Effective device control mode.  """,
            name='nvoControlMode',
            profile=self,
            number=5,
            datatype=SNVT_dev_c_mode,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviPumpOvdStop'] = base.Profile.DatapointMember(
            doc="""Pump override stop command.  """,
            name='nviPumpOvdStop',
            profile=self,
            number=6,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdSpeed'] = base.Profile.DatapointMember(
            doc="""Override speed in percent.  """,
            name='nviOvdSpeed',
            profile=self,
            number=7,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdPress'] = base.Profile.DatapointMember(
            doc="""Override setpoint for pressure.  """,
            name='nviOvdPress',
            profile=self,
            number=8,
            datatype=SNVT_press,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdFlow'] = base.Profile.DatapointMember(
            doc="""Override setpoint for flow.  """,
            name='nviOvdFlow',
            profile=self,
            number=9,
            datatype=SNVT_flow_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRemotePress'] = base.Profile.DatapointMember(
            doc="""Remote differential pressure sensor.  """,
            name='nviRemotePress',
            profile=self,
            number=10,
            datatype=SNVT_press,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinPress':
                base.Profile.PropertyMember(
                    doc="""Remote pressure-sensor minimum value.  """,
                    name='nciRemMinPress',
                    profile=self,
                    number=11,
                    datatype=SCPTminRemotePressureSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxPress':
                base.Profile.PropertyMember(
                    doc="""Remote pressure-sensor maximum value.  """,
                    name='nciRemMaxPress',
                    profile=self,
                    number=12,
                    datatype=SCPTmaxRemotePressureSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviRemoteFlow'] = base.Profile.DatapointMember(
            doc="""Remote flow sensor.  """,
            name='nviRemoteFlow',
            profile=self,
            number=11,
            datatype=SNVT_flow_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinFlow':
                base.Profile.PropertyMember(
                    doc="""Remote flow-sensor minimum value.  """,
                    name='nciRemMinFlow',
                    profile=self,
                    number=13,
                    datatype=SCPTminRemoteFlowSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxFlow':
                base.Profile.PropertyMember(
                    doc="""Remote flow-sensor maximum value.  """,
                    name='nciRemMaxFlow',
                    profile=self,
                    number=14,
                    datatype=SCPTmaxRemoteFlowSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviRemoteTemp'] = base.Profile.DatapointMember(
            doc="""Remote temperature sensor.  """,
            name='nviRemoteTemp',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinTemp':
                base.Profile.PropertyMember(
                    doc="""Remote temperature-sensor minimum value.  """,
                    name='nciRemMinTemp',
                    profile=self,
                    number=15,
                    datatype=SCPTminRemoteTempSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxTemp':
                base.Profile.PropertyMember(
                    doc="""Remote temperature-sensor maximum value.  """,
                    name='nciRemMaxTemp',
                    profile=self,
                    number=16,
                    datatype=SCPTmaxRemoteTempSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPumpStatus'] = base.Profile.DatapointMember(
            doc="""Device status.  Current status of the device.""",
            name='nvoPumpStatus',
            profile=self,
            number=13,
            datatype=SNVT_dev_status,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPressure'] = base.Profile.DatapointMember(
            doc="""Pump pressure.  """,
            name='nvoPressure',
            profile=self,
            number=14,
            datatype=SNVT_press,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFlow'] = base.Profile.DatapointMember(
            doc="""Pump flow.  """,
            name='nvoFlow',
            profile=self,
            number=15,
            datatype=SNVT_flow_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpeed'] = base.Profile.DatapointMember(
            doc="""Pump speed.  """,
            name='nvoSpeed',
            profile=self,
            number=16,
            datatype=SNVT_rpm,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPumpOverride'] = base.Profile.DatapointMember(
            doc="""Pump override active.  """,
            name='nvoPumpOverride',
            profile=self,
            number=17,
            datatype=SNVT_switch,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRuntime'] = base.Profile.DatapointMember(
            doc="""Runtime Total running time for the pump in hours.  After
            65535 hours, the counter starts again at zero.""",
            name='nvoRuntime',
            profile=self,
            number=18,
            datatype=SNVT_time_hour,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPumpFault'] = base.Profile.DatapointMember(
            doc="""Device fault states.  Fault information for the
            device.""",
            name='nvoPumpFault',
            profile=self,
            number=19,
            datatype=SNVT_dev_fault,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaintenance'] = base.Profile.DatapointMember(
            doc="""Device maintenance.  Device-maintenance states.""",
            name='nvoMaintenance',
            profile=self,
            number=20,
            datatype=SNVT_dev_maint,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFluidTemp'] = base.Profile.DatapointMember(
            doc="""Fluid temperature.  """,
            name='nvoFluidTemp',
            profile=self,
            number=21,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPower'] = base.Profile.DatapointMember(
            doc="""Electrical power consumption in Watts.  """,
            name='nvoPower',
            profile=self,
            number=22,
            datatype=SNVT_power,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPowerkilo'] = base.Profile.DatapointMember(
            doc="""Electrical power consumption in kiloWatts.  """,
            name='nvoPowerkilo',
            profile=self,
            number=23,
            datatype=SNVT_power_kilo,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyConsum'] = base.Profile.DatapointMember(
            doc="""Total energy consumption of the pump.  """,
            name='nvoEnergyConsum',
            profile=self,
            number=24,
            datatype=SNVT_elec_kwh,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = base.Profile.PropertyMember(
            doc="""Send heartbeat time.  """,
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            mandatory=True
        )
        self.properties['nroPumpChar'] = base.Profile.PropertyMember(
            doc="""Pump characteristics.  """,
            name='nroPumpChar',
            profile=self,
            number=2,
            datatype=SCPTpumpCharacteristic,
            flags=base.PropertyFlags.MFG,
            mandatory=True
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location label.  """,
            name='nciLocation',
            profile=self,
            number=3,
            datatype=SCPTlocation,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  """,
            name='nciRcvHrtBt',
            profile=self,
            number=4,
            datatype=SCPTmaxRcvTime,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  """,
            name='nciMinOutTm',
            profile=self,
            number=5,
            datatype=SCPTminSendTime,
            mandatory=False
        )
        self.properties['nciPressLowLim'] = base.Profile.PropertyMember(
            doc="""User-defined operational-pressure low limit.  """,
            name='nciPressLowLim',
            profile=self,
            number=6,
            datatype=SCPTminPressureSetpoint,
            mandatory=False
        )
        self.properties['nciPressHighLim'] = base.Profile.PropertyMember(
            doc="""User-defined operational-pressure high limit.  """,
            name='nciPressHighLim',
            profile=self,
            number=7,
            datatype=SCPTmaxPressureSetpoint,
            mandatory=False
        )
        self.properties['nciFlowLowLim'] = base.Profile.PropertyMember(
            doc="""User-defined operational-flow low limit.  """,
            name='nciFlowLowLim',
            profile=self,
            number=8,
            datatype=SCPTminFlowSetpoint,
            mandatory=False
        )
        self.properties['nciFlowHighLim'] = base.Profile.PropertyMember(
            doc="""User-defined operational-flow high limit.  """,
            name='nciFlowHighLim',
            profile=self,
            number=9,
            datatype=SCPTmaxFlowSetpoint,
            mandatory=False
        )
        self.properties['nciControlMode'] = base.Profile.PropertyMember(
            doc="""Control mode for normal operation.  """,
            name='nciControlMode',
            profile=self,
            number=10,
            datatype=SCPTdeviceControlMode,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=17,
            datatype=SCPTobjMajVer,
            flags=base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=18,
            datatype=SCPTobjMinVer,
            flags=base.PropertyFlags.DEVICE_SPECIFIC |
                base.PropertyFlags.CONST,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTpumpController()
    pass
