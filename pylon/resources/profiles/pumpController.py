"""pumpController standard profile, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.standard import standard
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.dev_c_mode
import pylon.resources.datapoints.press
import pylon.resources.datapoints.flow_p
import pylon.resources.properties.minRemotePressureSetpoint
import pylon.resources.properties.maxRemotePressureSetpoint
import pylon.resources.properties.minRemoteFlowSetpoint
import pylon.resources.properties.maxRemoteFlowSetpoint
import pylon.resources.datapoints.temp_p
import pylon.resources.properties.minRemoteTempSetpoint
import pylon.resources.properties.maxRemoteTempSetpoint
import pylon.resources.datapoints.dev_status
import pylon.resources.datapoints.rpm
import pylon.resources.datapoints.time_hour
import pylon.resources.datapoints.dev_fault
import pylon.resources.datapoints.dev_maint
import pylon.resources.datapoints.power
import pylon.resources.datapoints.power_kilo
import pylon.resources.datapoints.elec_kwh
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.pumpCharacteristic
import pylon.resources.properties.location
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.minPressureSetpoint
import pylon.resources.properties.maxPressureSetpoint
import pylon.resources.properties.minFlowSetpoint
import pylon.resources.properties.maxFlowSetpoint
import pylon.resources.properties.deviceControlMode
import pylon.resources.properties.objMajVer
import pylon.resources.properties.objMinVer


class pumpController(pylon.resources.base.Profile):
    """pumpController standard profile.  Pump Controller for HVAC
    Applications.  Provides the primary force to distribute and circulate hot
    and chilled water in a variety of space-temperature and air-conditioning
    systems."""

    def __init__(self):
        super().__init__(
            key=8120,
            scope=0
        )
        self.datapoints['nviPumpSetpoint'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump setpoint for normal operation.  """,
            name='nviPumpSetpoint',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviPumpOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Requested pump operating mode.  """,
            name='nviPumpOpMode',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoPumpCapacity'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump capacity in percent.  """,
            name='nvoPumpCapacity',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEffOpMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective operating mode.  """,
            name='nvoEffOpMode',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoControlMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Effective device control mode.  """,
            name='nvoControlMode',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.dev_c_mode.dev_c_mode,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviPumpOvdStop'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump override stop command.  """,
            name='nviPumpOvdStop',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override speed in percent.  """,
            name='nviOvdSpeed',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdPress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override setpoint for pressure.  """,
            name='nviOvdPress',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOvdFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Override setpoint for flow.  """,
            name='nviOvdFlow',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.flow_p.flow_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRemotePress'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Remote differential pressure sensor.  """,
            name='nviRemotePress',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinPress':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote pressure-sensor minimum value.  """,
                    name='nciRemMinPress',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.minRemotePressureSetpoint.minRemotePressureSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxPress':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote pressure-sensor maximum value.  """,
                    name='nciRemMaxPress',
                    profile=self,
                    number=12,
                    datatype=pylon.resources.properties.maxRemotePressureSetpoint.maxRemotePressureSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviRemoteFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Remote flow sensor.  """,
            name='nviRemoteFlow',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.flow_p.flow_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinFlow':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote flow-sensor minimum value.  """,
                    name='nciRemMinFlow',
                    profile=self,
                    number=13,
                    datatype=pylon.resources.properties.minRemoteFlowSetpoint.minRemoteFlowSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxFlow':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote flow-sensor maximum value.  """,
                    name='nciRemMaxFlow',
                    profile=self,
                    number=14,
                    datatype=pylon.resources.properties.maxRemoteFlowSetpoint.maxRemoteFlowSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviRemoteTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Remote temperature sensor.  """,
            name='nviRemoteTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciRemMinTemp':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote temperature-sensor minimum value.  """,
                    name='nciRemMinTemp',
                    profile=self,
                    number=15,
                    datatype=pylon.resources.properties.minRemoteTempSetpoint.minRemoteTempSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                ),
                'nciRemMaxTemp':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Remote temperature-sensor maximum value.  """,
                    name='nciRemMaxTemp',
                    profile=self,
                    number=16,
                    datatype=pylon.resources.properties.maxRemoteTempSetpoint.maxRemoteTempSetpoint,
                    default=b'\x7f\xff',
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoPumpStatus'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device status.  Current status of the device.""",
            name='nvoPumpStatus',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.dev_status.dev_status,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPressure'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump pressure.  """,
            name='nvoPressure',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.press.press,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFlow'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump flow.  """,
            name='nvoFlow',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.flow_p.flow_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump speed.  """,
            name='nvoSpeed',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.rpm.rpm,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPumpOverride'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Pump override active.  """,
            name='nvoPumpOverride',
            profile=self,
            number=17,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoRuntime'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Runtime Total running time for the pump in hours.  After
            65535 hours, the counter starts again at zero.""",
            name='nvoRuntime',
            profile=self,
            number=18,
            datatype=pylon.resources.datapoints.time_hour.time_hour,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPumpFault'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device fault states.  Fault information for the
            device.""",
            name='nvoPumpFault',
            profile=self,
            number=19,
            datatype=pylon.resources.datapoints.dev_fault.dev_fault,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoMaintenance'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device maintenance.  Device-maintenance states.""",
            name='nvoMaintenance',
            profile=self,
            number=20,
            datatype=pylon.resources.datapoints.dev_maint.dev_maint,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoFluidTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fluid temperature.  """,
            name='nvoFluidTemp',
            profile=self,
            number=21,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPower'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Electrical power consumption in Watts.  """,
            name='nvoPower',
            profile=self,
            number=22,
            datatype=pylon.resources.datapoints.power.power,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoPowerkilo'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Electrical power consumption in kiloWatts.  """,
            name='nvoPowerkilo',
            profile=self,
            number=23,
            datatype=pylon.resources.datapoints.power_kilo.power_kilo,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnergyConsum'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Total energy consumption of the pump.  """,
            name='nvoEnergyConsum',
            profile=self,
            number=24,
            datatype=pylon.resources.datapoints.elec_kwh.elec_kwh,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Send heartbeat time.  """,
            name='nciSndHrtBt',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            mandatory=True
        )
        self.properties['nroPumpChar'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Pump characteristics.  """,
            name='nroPumpChar',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.pumpCharacteristic.pumpCharacteristic,
            flags=pylon.resources.base.PropertyFlags.MFG,
            mandatory=True
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  """,
            name='nciLocation',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  """,
            name='nciRcvHrtBt',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  """,
            name='nciMinOutTm',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            mandatory=False
        )
        self.properties['nciPressLowLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""User-defined operational-pressure low limit.  """,
            name='nciPressLowLim',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.minPressureSetpoint.minPressureSetpoint,
            mandatory=False
        )
        self.properties['nciPressHighLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""User-defined operational-pressure high limit.  """,
            name='nciPressHighLim',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.maxPressureSetpoint.maxPressureSetpoint,
            mandatory=False
        )
        self.properties['nciFlowLowLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""User-defined operational-flow low limit.  """,
            name='nciFlowLowLim',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.minFlowSetpoint.minFlowSetpoint,
            mandatory=False
        )
        self.properties['nciFlowHighLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""User-defined operational-flow high limit.  """,
            name='nciFlowHighLim',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.maxFlowSetpoint.maxFlowSetpoint,
            mandatory=False
        )
        self.properties['nciControlMode'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Control mode for normal operation.  """,
            name='nciControlMode',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.deviceControlMode.deviceControlMode,
            mandatory=False
        )
        self.properties['nciObjMajVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object major version number.  The major version number for
            the object.""",
            name='nciObjMajVer',
            profile=self,
            number=17,
            datatype=pylon.resources.properties.objMajVer.objMajVer,
            flags=pylon.resources.base.PropertyFlags.CONST,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciObjMinVer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Object minor version number.  The minor version number for
            the object.""",
            name='nciObjMinVer',
            profile=self,
            number=18,
            datatype=pylon.resources.properties.objMinVer.objMinVer,
            flags=pylon.resources.base.PropertyFlags.DEVICE_SPECIFIC |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self._original_name = 'SFPTpumpController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = pumpController()
    pass
