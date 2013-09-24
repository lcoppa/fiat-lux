"""SFPTuniversalFireIndicator standard profile, originally defined in
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
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard
from pylon.resources.SNVT_switch import SNVT_switch
from pylon.resources.SCPTfireIndicate import SCPTfireIndicate
from pylon.resources.SCPTlocation import SCPTlocation
from pylon.resources.SCPTmaxRcvTime import SCPTmaxRcvTime
from pylon.resources.SCPTzoneNum import SCPTzoneNum
from pylon.resources.SCPTfireTxt1 import SCPTfireTxt1
from pylon.resources.SCPTfireTxt2 import SCPTfireTxt2
from pylon.resources.SCPTfireTxt3 import SCPTfireTxt3
from pylon.resources.SCPTinstallDate import SCPTinstallDate
from pylon.resources.SCPTmaintDate import SCPTmaintDate
from pylon.resources.SCPTmanfDate import SCPTmanfDate
from pylon.resources.SCPToemType import SCPToemType


class SFPTuniversalFireIndicator(base.Profile):
    """SFPTuniversalFireIndicator standard profile.  Universal Fire
    Indicator.  Generic indicator of the presence of fire by
    manufacturer-defined means."""

    def __init__(self):
        super().__init__(
            key=11011,
            scope=0,
            principal='nviUFIState'
        )
        self.datapoints['nviUFIState'] = base.Profile.DatapointMember(
            doc="""Universal Fire Indicator State.  The input NV controls the
            indicator device.""",
            name='nviUFIState',
            profile=self,
            number=1,
            datatype=SNVT_switch,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoFireTrouble'] = base.Profile.DatapointMember(
            doc="""Indicator Trouble.  This output NV reflects the
            operational condition of the indicator device.""",
            name='nvoFireTrouble',
            profile=self,
            number=2,
            datatype=SNVT_switch,
            mandatory=False,
            service=base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciIndicator'] = base.Profile.PropertyMember(
            doc="""Fire indicator device type.  Describes the fire indicator
            device.""",
            name='nciIndicator',
            profile=self,
            number=1,
            datatype=SCPTfireIndicate,
            default=b'\x00',
            mandatory=True
        )
        self.properties['nciLocation'] = base.Profile.PropertyMember(
            doc="""Location Provides descriptive physical location
            information related to the object.""",
            name='nciLocation',
            profile=self,
            number=2,
            datatype=SCPTlocation,
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=True
        )
        self.properties['nciMaxReceiveT'] = base.Profile.PropertyMember(
            doc="""Maximum receive time.  The maximum period of time that may
            expire with no updates on the associated input network variables
            before the object goes into heartbeat failure mode.  A zero value
            disables.""",
            name='nciMaxReceiveT',
            profile=self,
            number=3,
            datatype=SCPTmaxRcvTime,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciZoneNumber'] = base.Profile.PropertyMember(
            doc="""Zone number.  The zone number for the device.""",
            name='nciZoneNumber',
            profile=self,
            number=4,
            datatype=SCPTzoneNum,
            default=b'\x00\x00',
            mandatory=True
        )
        self.properties['nciFireText1'] = base.Profile.PropertyMember(
            doc="""Fire text information.  Text information relevant to fire
            conditions.  A '>' at end of string indicates presence of fire
            text 2.""",
            name='nciFireText1',
            profile=self,
            number=5,
            datatype=SCPTfireTxt1,
            flags=base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciFireText2'] = base.Profile.PropertyMember(
            doc="""Fire text information, continuation.  Continuation text
            information relevant to fire conditions.  A '>' at end of string
            indicates presence of fire text 3.""",
            name='nciFireText2',
            profile=self,
            number=6,
            datatype=SCPTfireTxt2,
            flags=base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciFireText3'] = base.Profile.PropertyMember(
            doc="""Fire text information, second continuation.  Second
            continuation text information relevant to fire conditions.""",
            name='nciFireText3',
            profile=self,
            number=7,
            datatype=SCPTfireTxt3,
            flags=base.PropertyFlags.DISABLE,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciInstallDate'] = base.Profile.PropertyMember(
            doc="""Installation date.  The date of installation for the
            device.""",
            name='nciInstallDate',
            profile=self,
            number=8,
            datatype=SCPTinstallDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciMaintDate'] = base.Profile.PropertyMember(
            doc="""Maintenance date.  The date of last maintenance for the
            device.""",
            name='nciMaintDate',
            profile=self,
            number=9,
            datatype=SCPTmaintDate,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciManfDate'] = base.Profile.PropertyMember(
            doc="""Manufacture date.  The date of manufacture for the
            device.""",
            name='nciManfDate',
            profile=self,
            number=10,
            datatype=SCPTmanfDate,
            flags=base.PropertyFlags.MFG |
                base.PropertyFlags.CONST,
            default=b'\x00\x00\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self.properties['nciOEMLable'] = base.Profile.PropertyMember(
            doc="""OEM label.  The label, programmed by the OEM, to identify
            the unit name.""",
            name='nciOEMLable',
            profile=self,
            number=11,
            datatype=SCPToemType,
            flags=base.PropertyFlags.MFG |
                base.PropertyFlags.CONST,
            minimum=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            maximum=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00',
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTuniversalFireIndicator()
    pass
