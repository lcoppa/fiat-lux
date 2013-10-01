"""variableSpeedMotorDrive standard profile, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.lev_percent
import pylon.resources.properties.defScale
import pylon.resources.datapoints.amp
import pylon.resources.datapoints.volt
import pylon.resources.datapoints.power_kilo
import pylon.resources.datapoints.time_hour
import pylon.resources.properties.maxSetpoint
import pylon.resources.properties.minSetpoint
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.nomRPM
import pylon.resources.properties.nomFreq
import pylon.resources.properties.rampUpTm
import pylon.resources.properties.rampDownTm
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.location


class variableSpeedMotorDrive(pylon.resources.base.Profile):
    """variableSpeedMotorDrive standard profile.  Variable-Speed Motor
    Drive.  Variable-Speed/Frequency Drive for Motors."""

    def __init__(self):
        super().__init__(
            key=6010,
            scope=0,
            principal='nviDrvSpeedStpt'
        )
        self.datapoints['nviDrvSpeedStpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive speed setpoint.  Provides start/stop control and a
            low-resolution speed setpoint.""",
            name='nviDrvSpeedStpt',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDrvSpeedScale'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive speed setpoint scaling.  Negative values indicate a
            motor direction in reverse.""",
            name='nviDrvSpeedScale',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT,
            properties={
                'nciDrvSpeedScale':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Drive speed scaling default value.  Default value
                    for drive speed setpoint scaling.""",
                    name='nciDrvSpeedScale',
                    profile=self,
                    number=11,
                    datatype=pylon.resources.properties.defScale.defScale,
                    mandatory=False
                )
            }
        )
        self.datapoints['nvoDrvCurnt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive current output.  Drive current (Amperes) output.""",
            name='nvoDrvCurnt',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.amp.amp,
            mandatory=False,
            minimum=b'\x00\x00',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDrvSpeed'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive speed output.  Drive speed as a percentage of
            nominal speed.""",
            name='nvoDrvSpeed',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDrvVolt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive voltage output.  The typical range is 0 to 700
            volts.""",
            name='nvoDrvVolt',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.volt.volt,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDrvPwr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive power output.  Drive power (kW) output.""",
            name='nvoDrvPwr',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.power_kilo.power_kilo,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoDrvRunHours'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Drive total running hours.  The number of hours the drive
            has been actively running.""",
            name='nvoDrvRunHours',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.time_hour.time_hour,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciMaxSpeed'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum motor speed.  The value is entered as a percent of
            nominal speed in RPM, as defined by the nominal speed
            configuration value.""",
            name='nciMaxSpeed',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.maxSetpoint.maxSetpoint,
            default=b'\x4e\x20',
            mandatory=True
        )
        self.properties['nciMinSpeed'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum motor speed.  The value is entered as a percent of
            nominal speed in RPM, as defined by the nominal speed
            configuration value.""",
            name='nciMinSpeed',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.minSetpoint.minSetpoint,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciSndHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  Controls the maximum period of time
            before the output values are transmitted.""",
            name='nciSndHrtBt',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            mandatory=True
        )
        self.properties['nciNmlSpeed'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal motor speed in RPM.  This value is necessary to
            determine the minimum and maximum speed for the motor.""",
            name='nciNmlSpeed',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.nomRPM.nomRPM,
            default=b'\x07\x08',
            mandatory=True
        )
        self.properties['nciNmlFreq'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal motor frequency.  Typical default values include
            50Hz and 60Hz.""",
            name='nciNmlFreq',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.nomFreq.nomFreq,
            mandatory=True
        )
        self.properties['nciRampUpTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum ramp-up time.  Minimum time of acceleration.""",
            name='nciRampUpTm',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.rampUpTm.rampUpTm,
            mandatory=True
        )
        self.properties['nciRampDownTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum ramp-down time.  Minimum time of deceleration.""",
            name='nciRampDownTm',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.rampDownTm.rampDownTm,
            mandatory=True
        )
        self.properties['nciRcvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  Maximum time that elapses after the
            last update to the input NV before actuator adopts the default
            output.""",
            name='nciRcvHrtBt',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            mandatory=False
        )
        self.properties['nciMinOutTm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  Controls the minimum period of time
            between output value transmissions.""",
            name='nciMinOutTm',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location label.  Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.location.location,
            mandatory=False
        )
        self._original_name = 'SFPTvariableSpeedMotorDrive'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = variableSpeedMotorDrive()
    pass
