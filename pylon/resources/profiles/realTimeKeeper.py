"""realTimeKeeper standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.time_stamp
import pylon.resources.properties.updateRate
import pylon.resources.properties.masterSlave
import pylon.resources.properties.summerTime
import pylon.resources.properties.winterTime
import pylon.resources.properties.manualAllowed


class realTimeKeeper(pylon.resources.base.Profile):
    """realTimeKeeper standard profile.  Real Time Keeper.  Provides the real
    time on the network to "time-stamp" events and synchronize schedulers."""

    def __init__(self):
        super().__init__(
            key=3300,
            scope=0,
            principal='nvoTimeDate'
        )
        self.datapoints['nvoTimeDate'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Real time output to the network.  Actual real time and
            date on the network for all linked objects.""",
            name='nvoTimeDate',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.REPEATED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciUpdateRate':
                pylon.resources.base.Profile.PropertyMember(
                    doc="""Time broadcast.  Update rate of the output should
                    be kept at 1 minute, 1 hour, or 1 day.""",
                    name='nciUpdateRate',
                    profile=self,
                    number=2,
                    datatype=pylon.resources.properties.updateRate.updateRate,
                    minimum=b'\x02\x58',
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviTimeSet'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Time input from a synchronizing source.  To set the
            initial/seed time of the clock (for a clock that does not set
            it's own initial time)""",
            name='nviTimeSet',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.time_stamp.time_stamp,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.properties['nciMasterSlave'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Master or slave clock.  "1" means "Master Clock Mode".
            "0" means "Slave Clock Mode".""",
            name='nciMasterSlave',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.masterSlave.masterSlave,
            mandatory=False
        )
        self.properties['nciSummerTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Summer date and time.  When not used entry shall be all
            "0" values.  Year, minutes, and seconds are always "0".""",
            name='nciSummerTime',
            profile=self,
            number=3,
            datatype=pylon.resources.properties.summerTime.summerTime,
            mandatory=False
        )
        self.properties['nciWinterTime'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Winter date and time.  When not used entry shall be all
            "0" values.  Year, minutes, and seconds are always "0".""",
            name='nciWinterTime',
            profile=self,
            number=4,
            datatype=pylon.resources.properties.winterTime.winterTime,
            mandatory=False
        )
        self.properties['nciManualAllowed'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Manual time updating allowed.  "1" means "Allowed".  "0"
            means "Disallowed".""",
            name='nciManualAllowed',
            profile=self,
            number=5,
            datatype=pylon.resources.properties.manualAllowed.manualAllowed,
            mandatory=False
        )
        self._original_name = 'SFPTrealTimeKeeper'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = realTimeKeeper()
    pass
