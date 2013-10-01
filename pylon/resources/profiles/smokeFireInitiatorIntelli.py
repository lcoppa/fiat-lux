"""smokeFireInitiatorIntelli standard profile, originally defined in resource
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
import pylon.resources.properties.maxSendTime
import pylon.resources.datapoints.fire_test
import pylon.resources.datapoints.lev_cont
import pylon.resources.datapoints.hvac_emerg
import pylon.resources.properties.location
import pylon.resources.properties.oemType
import pylon.resources.properties.smokeNomSens
import pylon.resources.properties.smokeDayAlrmLim
import pylon.resources.properties.smokeNightAlrmLim
import pylon.resources.properties.smokeDayPreAlrmLim
import pylon.resources.properties.smokeNightPreAlrmLim
import pylon.resources.properties.zoneNum
import pylon.resources.properties.installDate
import pylon.resources.properties.maintDate
import pylon.resources.properties.manfDate
import pylon.resources.properties.fireTxt1
import pylon.resources.properties.fireTxt2
import pylon.resources.properties.fireTxt3


class smokeFireInitiatorIntelli(pylon.resources.base.Profile):
    """smokeFireInitiatorIntelli standard profile.  Smoke (Intelligent) Fire
    Initiator.  Intelligent (addressable) Smoke Fire Initiator object for
    fire-alarm notification and response functions."""

    def __init__(self):
        super().__init__(
            key=11002,
            scope=0
        )
        self.datapoints['nvoFireAlm'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fire alarm.  Fire information for use by simple
            indicators.""",
            name='nvoFireAlm',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxSendTime':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Maximum send time.  The maximum period of time
                    between consecutive transmissions of the current
                    value.""",
                    name='nciMaxSendTime',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.maxSendTime.maxSendTime,
                    mandatory=True
                )
            }
        )
        self.datapoints['nvoFireTrouble'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Fire trouble.  Initiator trouble information for use by
            simple indicators.""",
            name='nvoFireTrouble',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviDeviceRequest'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Device request.  Receives requests intended to perform
            smoke detector operations, initiated from operator.""",
            name='nviDeviceRequest',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.fire_test.fire_test,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoDayNightMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Day (0%;  0) and Night (100%;  1) mode.  Present value for
            Day/Night mode.  The DayNightMode variable is used by
            applications that use day/night -sensitive limits depending upon
            time of day.""",
            name='nvoDayNightMode',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=False,
            polled=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEnvComp'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Environmental compensation.  For use by operator-interface
            devices requiring system, environmental-compensation
            reporting.""",
            name='nvoEnvComp',
            profile=self,
            number=5,
            datatype=pylon.resources.datapoints.lev_cont.lev_cont,
            mandatory=False,
            polled=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoEmergMode'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Emergency mode:  EMERG_NORMAL or EMERG_FIRE.  Controls the
            (actuator) position for smoke-control devices.""",
            name='nvoEmergMode',
            profile=self,
            number=6,
            datatype=pylon.resources.datapoints.hvac_emerg.hvac_emerg,
            mandatory=False,
            minimum=b'\x00',
            maximum=b'\x05',
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciNodeLocation'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciNodeLocation',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.location.location,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciOEMLabel'] = pylon.resources.base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOEMLabel',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.oemType.oemType,
            flags=pylon.resources.base.PropertyFlags.MFG |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciNomSens'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nominal sensitivity.  The nominal sensitivity value for
            the fire initiator in percentage obscuration by smoke.""",
            name='nciNomSens',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.smokeNomSens.smokeNomSens,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciDayAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Daytime alarm limit.  The daytime alarm limit sensitivity
            value for the fire initiator in percentage obscuration by
            smoke.""",
            name='nciDayAlarm',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.smokeDayAlrmLim.smokeDayAlrmLim,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciNightAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nighttime alarm limit.  The nighttime alarm limit
            sensitivity value for the fire initiator in percentage
            obscuration by smoke.""",
            name='nciNightAlarm',
            profile=self,
            number=6,
            datatype=pylon.resources.properties.smokeNightAlrmLim.smokeNightAlrmLim,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciDayPreAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Daytime pre-alarm limit.  The daytime pre-alarm limit
            sensitivity value for the fire initiator in percentage
            obscuration by smoke.""",
            name='nciDayPreAlarm',
            profile=self,
            number=7,
            datatype=pylon.resources.properties.smokeDayPreAlrmLim.smokeDayPreAlrmLim,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciNightPreAlarm'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Nighttime pre-alarm limit.  The nighttime pre-alarm limit
            sensitivity value for the fire initiator in percentage
            obscuration by smoke.""",
            name='nciNightPreAlarm',
            profile=self,
            number=8,
            datatype=pylon.resources.properties.smokeNightPreAlrmLim.smokeNightPreAlrmLim,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=True
        )
        self.properties['nciZoneNum'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Zone number.  The zone number for the device.""",
            name='nciZoneNum',
            profile=self,
            number=9,
            datatype=pylon.resources.properties.zoneNum.zoneNum,
            mandatory=True
        )
        self.properties['nciInstallDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=10,
            datatype=pylon.resources.properties.installDate.installDate,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['nciMaintDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Maintenance date.  The date of last maintenance for the
            device.""",
            name='nciMaintDate',
            profile=self,
            number=11,
            datatype=pylon.resources.properties.maintDate.maintDate,
            mandatory=False
        )
        self.properties['nciManufDate'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciManufDate',
            profile=self,
            number=12,
            datatype=pylon.resources.properties.manfDate.manfDate,
            flags=pylon.resources.base.PropertyFlags.MFG |
                pylon.resources.base.PropertyFlags.CONST,
            mandatory=False
        )
        self.properties['nciFireText1'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information.  Text information relevant to fire
            conditions.  A '>' at end of string indicates presence of fire
            text 2.""",
            name='nciFireText1',
            profile=self,
            number=13,
            datatype=pylon.resources.properties.fireTxt1.fireTxt1,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['nciFireText2'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information, continuation.  Continuation text
            information relevant to fire conditions.  A '>' at end of string
            indicates presence of fire text 3.""",
            name='nciFireText2',
            profile=self,
            number=14,
            datatype=pylon.resources.properties.fireTxt2.fireTxt2,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self.properties['nciFireText3'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Fire text information, second continuation.  Second
            continuation text information relevant to fire conditions.""",
            name='nciFireText3',
            profile=self,
            number=15,
            datatype=pylon.resources.properties.fireTxt3.fireTxt3,
            flags=pylon.resources.base.PropertyFlags.DISABLE,
            mandatory=False
        )
        self._original_name = 'SFPTsmokeFireInitiatorIntelli'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = smokeFireInitiatorIntelli()
    pass
