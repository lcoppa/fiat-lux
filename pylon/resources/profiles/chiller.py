"""chiller standard profile, originally defined in resource file set standard
00:00:00:00:00:00:00:00-0."""


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
import pylon.resources.datapoints.temp_p
import pylon.resources.datapoints.lev_percent
import pylon.resources.datapoints.hvac_mode
import pylon.resources.datapoints.str_asc
import pylon.resources.datapoints.chlr_status
import pylon.resources.properties.pwrUpState
import pylon.resources.properties.maxSendTime
import pylon.resources.properties.minSendTime
import pylon.resources.properties.limitChlrCap
import pylon.resources.properties.coolSetpt
import pylon.resources.properties.heatSetpt
import pylon.resources.properties.hvacMode
import pylon.resources.properties.location
import pylon.resources.properties.defltBehave
import pylon.resources.properties.maxRcvTime
import pylon.resources.properties.pwrUpDelay


class chiller(pylon.resources.base.Profile):
    """chiller standard profile.  Chiller Controller.  For use with
    centrifugal, absorption, reciprocating, and other models of chillers."""

    def __init__(self):
        super().__init__(
            key=8040,
            scope=0
        )
        self.datapoints['nviChillerEnable'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Chiller enable.  Request start/stop chiller.""",
            name='nviChillerEnable',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCoolSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Cool setpoint.  Desired temperature of leaving chilled
            water.""",
            name='nviCoolSetpt',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            minimum=b'\xfb\x3c',
            maximum=b'\x13\x10',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOnOff'] = pylon.resources.base.Profile.DatapointMember(
            doc="""On or off state.  Chiller on/off run state.""",
            name='nvoOnOff',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActiveSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Active setpoint output.  Active cool or heat setpoint.""",
            name='nvoActiveSetpt',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x24\x54',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviCapacityLim'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Capacity limit input.  Capacity limit of chiller.""",
            name='nviCapacityLim',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEntChWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entering chilled-water temperature input.  Accommodates
            remote temperature-sensor input.""",
            name='nviEntChWTemp',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\xfb\x3c',
            maximum=b'\x13\x1a',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Chiller mode.  Chiller modes.""",
            name='nviMode',
            profile=self,
            number=7,
            datatype=pylon.resources.datapoints.hvac_mode.hvac_mode,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHeatSetpt'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Heating setpoint.  Heating setpoint.""",
            name='nviHeatSetpt',
            profile=self,
            number=8,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            minimum=b'\x03\xe8',
            maximum=b'\x24\x54',
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActCapacity'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Actual capacity level.  Actual running capacity of
            unit.""",
            name='nvoActCapacity',
            profile=self,
            number=9,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCapacityLim'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Capacity limit.  Present capacity limit setting of
            chiller.""",
            name='nvoCapacityLim',
            profile=self,
            number=10,
            datatype=pylon.resources.datapoints.lev_percent.lev_percent,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLvgChWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Leaving chilled-water temperature.  Leaving chilled-water
            temperature.""",
            name='nvoLvgChWTemp',
            profile=self,
            number=11,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEntChWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entering chilled-water temperature.  Entering
            chilled-water temperature.""",
            name='nvoEntChWTemp',
            profile=self,
            number=12,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEntCndWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Entering condenser-water temperature.  Entering
            condenser-water temperature.""",
            name='nvoEntCndWTemp',
            profile=self,
            number=13,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLvgCndWTemp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Leaving condenser-water temperature.  Leaving
            condenser-water temperature.""",
            name='nvoLvgCndWTemp',
            profile=self,
            number=14,
            datatype=pylon.resources.datapoints.temp_p.temp_p,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAlarmDescr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Alarm annunciation text.  Character string (30 characters
            max)""",
            name='nvoAlarmDescr',
            profile=self,
            number=15,
            datatype=pylon.resources.datapoints.str_asc.str_asc,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoChillerStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Chiller status.  Chiller states or modes.""",
            name='nvoChillerStat',
            profile=self,
            number=16,
            datatype=pylon.resources.datapoints.chlr_status.chlr_status,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciChillerEnable'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Chiller enable.  The default power-up and restart modes of
            the device when the default behavior selector is set to zero.""",
            name='nciChillerEnable',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.pwrUpState.pwrUpState,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=pylon.resources.properties.maxSendTime.maxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.minSendTime.minSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciCapacityLim'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Chiller capacity limit.  The default value for the
            capacity limit of the chiller when the default behavior selector
            is set to zero.""",
            name='nciCapacityLim',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.limitChlrCap.limitChlrCap,
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciCoolSetpt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Cooling setpoint.  The default setpoint for the leaving
            chilled water temperature in cooling mode when the default
            behavior selector is set to zero.""",
            name='nciCoolSetpt',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.coolSetpt.coolSetpt,
            default=b'\x02\xd0',
            mandatory=True
        )
        self.properties['nciHeatSetpt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Heating setpoint.  The default setpoint for the leaving
            water temperature in heating mode when the default behavior
            selector is set to zero.""",
            name='nciHeatSetpt',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.heatSetpt.heatSetpt,
            default=b'\x0d\xac',
            mandatory=False
        )
        self.properties['nciMode'] = pylon.resources.base.Profile.PropertyMember(
            doc="""HVAC mode.  The default operating mode of the device when
            the default behavior selector is set to zero.""",
            name='nciMode',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.hvacMode.hvacMode,
            default=b'\x03',
            mandatory=False
        )
        self.properties['nciLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.location.location,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciDefaults'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Default behavior.  Selects which set of values will be
            used on power-up and communication failure, between the stated
            default values (0), or manufacturer-specified values (1)""",
            name='nciDefaults',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.defltBehave.defltBehave,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRCvHrtBt'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRCvHrtBt',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.maxRcvTime.maxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciPwrup'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Power-up delay.  The minimum period of time after power-up
            or re-establishment of communications before a control action
            takes place.""",
            name='nciPwrup',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.pwrUpDelay.pwrUpDelay,
            mandatory=False
        )
        self._original_name = 'SFPTchiller'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = chiller()
    pass
