"""SFPTrefrigDisplayCaseControllerDefrost standard profile, originally
defined in resource file set standard 00:00:00:00:00:00:00:00-0."""


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
from pylon.resources.SNVT_lev_disc import SNVT_lev_disc
from pylon.resources.SNVT_defr_state import SNVT_defr_state
from pylon.resources.SNVT_temp_p import SNVT_temp_p
from pylon.resources.SNVT_lev_percent import SNVT_lev_percent
from pylon.resources.SCPTmaxSendTime import SCPTmaxSendTime
from pylon.resources.SCPTminSendTime import SCPTminSendTime
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTdefrostMode import SCPTdefrostMode
from pylon.resources.SCPTstrtupDelay import SCPTstrtupDelay
from pylon.resources.SCPTtermTimeTemp import SCPTtermTimeTemp
from pylon.resources.SCPTmaxDefrstTemp import SCPTmaxDefrstTemp
from pylon.resources.SCPTmaxDefrstTime import SCPTmaxDefrstTime
from pylon.resources.SCPTpumpDownDelay import SCPTpumpDownDelay
from pylon.resources.SCPTdrainDelay import SCPTdrainDelay
from pylon.resources.SCPTinjDelay import SCPTinjDelay


class SFPTrefrigDisplayCaseControllerDefrost(base.Profile):
    """SFPTrefrigDisplayCaseControllerDefrost standard profile.  Refrigerated
    Display-Case Defrost Controller.  Used to control the defrost functions
    of a refigerated display case."""

    def __init__(self):
        super().__init__(
            key=10010,
            scope=0
        )
        self.datapoints['nviDefrostEnable'] = base.Profile.DatapointMember(
            doc="""Defrost Enable.  Begin defrost switch.""",
            name='nviDefrostEnable',
            profile=self,
            number=1,
            datatype=SNVT_lev_disc,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDefrostState'] = base.Profile.DatapointMember(
            doc="""Defrost state.  The nvoDefrostState indicates the current
            state of the defrost object.""",
            name='nvoDefrostState',
            profile=self,
            number=2,
            datatype=SNVT_defr_state,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviTemperature1'] = base.Profile.DatapointMember(
            doc="""Temperture 1.  nviTemperature1 is to be assigned to inlet
            or outlet of the evaporator as required.  An error on the sensor
            is indicated with a value outside the valid range.""",
            name='nviTemperature1',
            profile=self,
            number=3,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoTemperature1'] = base.Profile.DatapointMember(
            doc="""Temperature Processed temperature 1.""",
            name='nvoTemperature1',
            profile=self,
            number=4,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviTemperture2'] = base.Profile.DatapointMember(
            doc="""Temperatur 2.  The nviTemperature2 is to be assigned to
            inlet or outlet of the evaporator as required.  An error on the
            sensor is indicated with a value outside the valid range.""",
            name='nviTemperture2',
            profile=self,
            number=5,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoTemperture2'] = base.Profile.DatapointMember(
            doc="""Temperature Processed temperature 2.""",
            name='nvoTemperture2',
            profile=self,
            number=6,
            datatype=SNVT_temp_p,
            mandatory=False,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviStartUp'] = base.Profile.DatapointMember(
            doc="""Start Up.  If synchronised defrost is selected as the
            control strategy, this network variable indicates that the
            defrost object can begin the after defrost sequence.""",
            name='nviStartUp',
            profile=self,
            number=7,
            datatype=SNVT_lev_disc,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviDefTerminate'] = base.Profile.DatapointMember(
            doc="""Defrost Terminate.  nviDefrostTerminate can be used as an
            input from some external sensor e.g.  ice sensor to indicate the
            level of defrosting.""",
            name='nviDefTerminate',
            profile=self,
            number=8,
            datatype=SNVT_lev_disc,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviHumidity'] = base.Profile.DatapointMember(
            doc="""Humidity The nviHumidity can be used to provide humidity
            information for the defrost algorithm.""",
            name='nviHumidity',
            profile=self,
            number=9,
            datatype=SNVT_lev_percent,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['nciMaxSendTime'] = base.Profile.PropertyMember(
            doc="""Maximum send time.  The maximum period of time between
            consecutive transmissions of the current value.""",
            name='nciMaxSendTime',
            profile=self,
            number=1,
            datatype=SCPTmaxSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciMinSendTime'] = base.Profile.PropertyMember(
            doc="""Minimum send time.  The minimum period of time between
            consecutive transmissions of the current value.""",
            name='nciMinSendTime',
            profile=self,
            number=2,
            datatype=SCPTminSendTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciLocationLabel'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocationLabel',
            profile=self,
            number=3,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciDefrostMode'] = base.Profile.PropertyMember(
            doc="""Defrost mode.  The type of defrost to perform.""",
            name='nciDefrostMode',
            profile=self,
            number=4,
            datatype=SCPTdefrostMode,
            default=b'\x01',
            mandatory=False
        )
        self.properties['nciStartUpDelay'] = base.Profile.PropertyMember(
            doc="""Startup delay.  The time to delay after power-up, defrost,
            or pack fail.""",
            name='nciStartUpDelay',
            profile=self,
            number=5,
            datatype=SCPTstrtupDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciTerminateTimeTemp'] = base.Profile.PropertyMember(
            doc="""Defrost termination setting.  The defrost termination
            condition.""",
            name='nciTerminateTimeTemp',
            profile=self,
            number=6,
            datatype=SCPTtermTimeTemp,
            default=b'\x00',
            mandatory=False
        )
        self.properties['nciDefrostStopTemp'] = base.Profile.PropertyMember(
            doc="""Defrost stop temperature.  The temperature at which to
            terminate defrost for objects set to terminate on
            temperature.""",
            name='nciDefrostStopTemp',
            profile=self,
            number=7,
            datatype=SCPTmaxDefrstTemp,
            minimum=b'\xd8\xf0',
            maximum=b'\x3a\x98',
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciMaxDefrostTime'] = base.Profile.PropertyMember(
            doc="""Maximum defrost time.  The maximum defrost time for
            defrost objects set to terminate on temperature.""",
            name='nciMaxDefrostTime',
            profile=self,
            number=8,
            datatype=SCPTmaxDefrstTime,
            default=b'\x8c\xa0',
            mandatory=False
        )
        self.properties['nciPumpDownDelay'] = base.Profile.PropertyMember(
            doc="""Pump down delay.  The delay to use before starting the
            defrost.""",
            name='nciPumpDownDelay',
            profile=self,
            number=9,
            datatype=SCPTpumpDownDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciDrainDelay'] = base.Profile.PropertyMember(
            doc="""Drain delay.  The delay to use after the defrost has
            terminated.""",
            name='nciDrainDelay',
            profile=self,
            number=10,
            datatype=SCPTdrainDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self.properties['nciInjectionDelay'] = base.Profile.PropertyMember(
            doc="""Injection delay.  The delay to use after the defrost has
            terminated.""",
            name='nciInjectionDelay',
            profile=self,
            number=11,
            datatype=SCPTinjDelay,
            default=b'\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTrefrigDisplayCaseControllerDefrost()
    pass
