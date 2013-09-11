"""SFPTchiller standard profile, originally defined in resource file set
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
# Generated at 05-Sep-2013 10:50.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SNVT_hvac_mode import SNVT_hvac_mode
from pylon.resources.SNVT_str_asc import SNVT_str_asc
from pylon.resources.SNVT_chlr_status import SNVT_chlr_status
from pylon.resources.SCPTpwrUpState import SCPTpwrUpState
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTlimitChlrCap import SCPTlimitChlrCap
from pylon.resources.SCPTcoolSetpt import SCPTcoolSetpt
from pylon.resources.SCPTheatSetpt import SCPTheatSetpt
from pylon.resources.SCPThvacMode import SCPThvacMode
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTdefltBehave import SCPTdefltBehave
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTpwrUpDelay import SCPTpwrUpDelay


class SFPTchiller(base.Profile):
    """SFPTchiller standard profile.  Chiller Controller.  For use with
    centrifugal, absorption, reciprocating, and other models of chillers."""

    def __init__(self):
        super().__init__(
            key=8040,
            scope=0
        )
        self.datapoints['nviChillerEnable'] = base.Profile.DatapointMember(
            doc="""Chiller enable.  Request start/stop chiller.""",
            name='nviChillerEnable',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCoolSetpt'] = base.Profile.DatapointMember(
            doc="""Cool setpoint.  Desired temperature of leaving chilled
            water.""",
            name='nviCoolSetpt',
            profile=self,
            number=2,
            datatype=SNVT_temp_p,
            mandatory=True,
            minimum=b'\xfb\x3c',
            maximum=b'\x13\x10',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoOnOff'] = base.Profile.DatapointMember(
            doc="""On or off state.  Chiller on/off run state.""",
            name='nvoOnOff',
            profile=self,
            number=3,
            datatype=SNVT_switch,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoActiveSetpt'] = base.Profile.DatapointMember(
            doc="""Active setpoint output.  Active cool or heat setpoint.""",
            name='nvoActiveSetpt',
            profile=self,
            number=4,
            datatype=SNVT_temp_p,
            mandatory=True,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x24\x54',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviCapacityLim'] = base.Profile.DatapointMember(
            doc="""Capacity limit input.  Capacity limit of chiller.""",
            name='nviCapacityLim',
            profile=self,
            number=5,
            datatype=SNVT_lev_percent,
            mandatory=False,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviEntChWTemp'] = base.Profile.DatapointMember(
            doc="""Entering chilled-water temperature input.  Accommodates
            remote temperature-sensor input.""",
            name='nviEntChWTemp',
            profile=self,
            number=6,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\xfb\x3c',
            maximum=b'\x13\x1a',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviMode'] = base.Profile.DatapointMember(
            doc="""Chiller mode.  Chiller modes.""",
            name='nviMode',
            profile=self,
            number=7,
            datatype=SNVT_hvac_mode,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHeatSetpt'] = base.Profile.DatapointMember(
            doc="""Heating setpoint.  Heating setpoint.""",
            name='nviHeatSetpt',
            profile=self,
            number=8,
            datatype=SNVT_temp_p,
            mandatory=False,
            minimum=b'\x03\xe8',
            maximum=b'\x24\x54',
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoActCapacity'] = base.Profile.DatapointMember(
            doc="""Actual capacity level.  Actual running capacity of
            unit.""",
            name='nvoActCapacity',
            profile=self,
            number=9,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoCapacityLim'] = base.Profile.DatapointMember(
            doc="""Capacity limit.  Present capacity limit setting of
            chiller.""",
            name='nvoCapacityLim',
            profile=self,
            number=10,
            datatype=SNVT_lev_percent,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\x00\x00',
            maximum=b'\x7d\x00',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLvgChWTemp'] = base.Profile.DatapointMember(
            doc="""Leaving chilled-water temperature.  Leaving chilled-water
            temperature.""",
            name='nvoLvgChWTemp',
            profile=self,
            number=11,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEntChWTemp'] = base.Profile.DatapointMember(
            doc="""Entering chilled-water temperature.  Entering
            chilled-water temperature.""",
            name='nvoEntChWTemp',
            profile=self,
            number=12,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEntCndWTemp'] = base.Profile.DatapointMember(
            doc="""Entering condenser-water temperature.  Entering
            condenser-water temperature.""",
            name='nvoEntCndWTemp',
            profile=self,
            number=13,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoLvgCndWTemp'] = base.Profile.DatapointMember(
            doc="""Leaving condenser-water temperature.  Leaving
            condenser-water temperature.""",
            name='nvoLvgCndWTemp',
            profile=self,
            number=14,
            datatype=SNVT_temp_p,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            minimum=b'\xf0\x60',
            maximum=b'\x2e\x18',
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoAlarmDescr'] = base.Profile.DatapointMember(
            doc="""Alarm annunciation text.  Character string (30 characters
            max)""",
            name='nvoAlarmDescr',
            profile=self,
            number=15,
            datatype=SNVT_str_asc,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoChillerStat'] = base.Profile.DatapointMember(
            doc="""Chiller status.  Chiller states or modes.""",
            name='nvoChillerStat',
            profile=self,
            number=16,
            datatype=SNVT_chlr_status,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciChillerEnable'] = base.Profile.PropertyMember(
            doc="""Chiller enable.  The default power-up and restart modes of
            the device when the default behavior selector is set to zero.""",
            name='nciChillerEnable',
            profile=self,
            number=1,
            datatype=SCPTpwrUpState,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=2,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=3,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciCapacityLim'] = base.Profile.PropertyMember(
            doc="""Chiller capacity limit.  The default value for the
            capacity limit of the chiller when the default behavior selector
            is set to zero.""",
            name='nciCapacityLim',
            profile=self,
            number=4,
            datatype=SCPTlimitChlrCap,
            default=b'\x4e\x20',
            mandatory=False
        )
        self.properties['nciCoolSetpt'] = base.Profile.PropertyMember(
            doc="""Cooling setpoint.  The default setpoint for the leaving
            chilled water temperature in cooling mode when the default
            behavior selector is set to zero.""",
            name='nciCoolSetpt',
            profile=self,
            number=5,
            datatype=SCPTcoolSetpt,
            default=b'\x02\xd0',
            mandatory=True
        )
        self.properties['nciHeatSetpt'] = base.Profile.PropertyMember(
            doc="""Heating setpoint.  The default setpoint for the leaving
            water temperature in heating mode when the default behavior
            selector is set to zero.""",
            name='nciHeatSetpt',
            profile=self,
            number=6,
            datatype=SCPTheatSetpt,
            default=b'\x0d\xac',
            mandatory=False
        )
        self.properties['nciMode'] = base.Profile.PropertyMember(
            doc="""HVAC mode.  The default operating mode of the device when
            the default behavior selector is set to zero.""",
            name='nciMode',
            profile=self,
            number=7,
            datatype=SCPThvacMode,
            default=b'\x03',
            mandatory=False
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=8,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciDefaults'] = base.Profile.PropertyMember(
            doc="""Default behavior.  Selects which set of values will be
            used on power-up and communication failure, between the stated
            default values (0), or manufacturer-specified values (1)""",
            name='nciDefaults',
            profile=self,
            number=9,
            datatype=SCPTdefltBehave,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciRCvHrtBt'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciRCvHrtBt',
            profile=self,
            number=10,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciPwrup'] = base.Profile.PropertyMember(
            doc="""Power-up delay.  The minimum period of time after power-up
            or re-establishment of communications before a control action
            takes place.""",
            name='nciPwrup',
            profile=self,
            number=11,
            datatype=SCPTpwrUpDelay,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTchiller()
    pass
