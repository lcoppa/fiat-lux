"""SFPToutdoorLuminairController standard profile, originally defined in
resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_time_hour_p import SNVT_time_hour_p
from pylon.resources.SNVT_elec_kwh_l import SNVT_elec_kwh_l
from pylon.resources.SNVT_lamp_status import SNVT_lamp_status
from pylon.resources.SCPTenableStatusMsg import SCPTenableStatusMsg
from pylon.resources.SCPTOLCLimits import SCPTOLCLimits
from pylon.resources.SNVT_environment import SNVT_environment
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTbkupSchedule import SCPTbkupSchedule
from pylon.resources.SCPTlampPower import SCPTlampPower
from pylon.resources.SCPTdeviceOutSelection import SCPTdeviceOutSelection
from pylon.resources.SCPTminSetpoint import SCPTminSetpoint
from pylon.resources.SCPTrampUpTm import SCPTrampUpTm
from pylon.resources.SCPTmaxLevelVolt import SCPTmaxLevelVolt
from pylon.resources.SCPTpwrUpState import SCPTpwrUpState


class SFPToutdoorLuminairController(base.Profile):
    """SFPToutdoorLuminairController standard profile.  Outdoor Luminair
    Controller.  """

    def __init__(self):
        super().__init__(
            key=3512,
            scope=0
        )
        self.datapoints['nviLampValue'] = base.Profile.DatapointMember(
            doc="""Lamp Value Input.  The desired state (on/off) and value
            (%) of the lamp bulb.""",
            name='nviLampValue',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviRunHours'] = base.Profile.DatapointMember(
            doc="""Run-Hours Change.  The method used to reset or initialize
            the run-hours count.""",
            name='nviRunHours',
            profile=self,
            number=2,
            datatype=SNVT_time_hour_p,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEnergy'] = base.Profile.DatapointMember(
            doc="""Electricity-Used Change.  The method used to reset or
            initialize the electricity-consumption total.""",
            name='nviEnergy',
            profile=self,
            number=3,
            datatype=SNVT_elec_kwh_l,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLampValueFb'] = base.Profile.DatapointMember(
            doc="""Lamp Value Output.  The actual state (on/off) and value
            (%) of the lamp bulb.""",
            name='nvoLampValueFb',
            profile=self,
            number=4,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoOLCStatus'] = base.Profile.DatapointMember(
            doc="""Lamp-Controller Status Output.  The data related to the
            internal status conditions of the lamp controller.""",
            name='nvoOLCStatus',
            profile=self,
            number=5,
            datatype=SNVT_lamp_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'cpEnableStatusMsg':
                base.Profile.PropertyMember(
                    doc="""Enable-Status Mask.  Determines which status
                    information will be available and valid for the alarm
                    fields of nvoOLCStatus.""",
                    name='cpEnableStatusMsg',
                    profile=self,
                    number=5,
                    datatype=SCPTenableStatusMsg,
                    default=b'\x00\x00\x00\x00\x00',
                    mandatory=True
                ),
                'cpOLCLimits':
                base.Profile.PropertyMember(
                    doc="""OLC Limits Setpoints.  This configuration property
                    sets the limits for nvoOLCStatus.""",
                    name='cpOLCLimits',
                    profile=self,
                    number=10,
                    datatype=SCPTOLCLimits,
                    default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoEnvironment'] = base.Profile.DatapointMember(
            doc="""OLC Environment Output.  The measured values from in and
            around the environment of the fixture, including mains/lamp
            voltages, mains/lamp currents, lamp temperature, consumed power,
            and power factor.""",
            name='nvoEnvironment',
            profile=self,
            number=6,
            datatype=SNVT_environment,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='cpMinSendTime',
            profile=self,
            number=1,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='cpMaxSendTime',
            profile=self,
            number=2,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpBkupSchedule'] = base.Profile.PropertyMember(
            doc="""Backup Schedule.  The On/Off schedule to be used as a
            default.""",
            name='cpBkupSchedule',
            profile=self,
            number=3,
            datatype=SCPTbkupSchedule,
            default=b'\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['cpLampPower'] = base.Profile.PropertyMember(
            doc="""Lamp Power.  The maximum wattage of the installed
            bulbs.""",
            name='cpLampPower',
            profile=self,
            number=4,
            datatype=SCPTlampPower,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpDeviceOutSelection'] = base.Profile.PropertyMember(
            doc="""Device Output Selection.  The type of hardware output.""",
            name='cpDeviceOutSelection',
            profile=self,
            number=6,
            datatype=SCPTdeviceOutSelection,
            default=b'\x00',
            mandatory=True
        )
        self.properties['cpDimLowLevelLight'] = base.Profile.PropertyMember(
            doc="""Dimmable Minimum.  The minimum percentage value for a
            dimmable lamp to remain illuminated.""",
            name='cpDimLowLevelLight',
            profile=self,
            number=7,
            datatype=SCPTminSetpoint,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpWarmUpTime'] = base.Profile.PropertyMember(
            doc="""Minimum warm-up time.  The time it takes the lamp to
            warm-up to the full operating temperature.""",
            name='cpWarmUpTime',
            profile=self,
            number=8,
            datatype=SCPTrampUpTm,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpMaxLevelVolt'] = base.Profile.PropertyMember(
            doc="""Preceivable-Maximum Control.  The maximum voltage (of the
            1-10V output) needed to achieve 100% lamp-light output.  In many
            cases, 100% is reached before the 10V-limit is reached.""",
            name='cpMaxLevelVolt',
            profile=self,
            number=9,
            datatype=SCPTmaxLevelVolt,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['cpPwrUpState'] = base.Profile.PropertyMember(
            doc="""OLC Powerup state.  This configuration property is be used
            to define the default output value on power up.""",
            name='cpPwrUpState',
            profile=self,
            number=11,
            datatype=SCPTpwrUpState,
            default=b'\xc8\x01',
            mandatory=True
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPToutdoorLuminairController()
    pass
