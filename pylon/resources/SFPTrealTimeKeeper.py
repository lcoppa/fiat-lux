"""SFPTrealTimeKeeper standard profile, originally defined in resource file
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
from pylon.resources.SNVT_time_stamp import SNVT_time_stamp
from pylon.resources.SCPTupdateRate import SCPTupdateRate
from pylon.resources.SCPTmasterSlave import SCPTmasterSlave
from pylon.resources.SCPTsummerTime import SCPTsummerTime
from pylon.resources.SCPTwinterTime import SCPTwinterTime
from pylon.resources.SCPTmanualAllowed import SCPTmanualAllowed


class SFPTrealTimeKeeper(base.Profile):
    """SFPTrealTimeKeeper standard profile.  Real Time Keeper.  Provides the
    real time on the network to "time-stamp" events and synchronize
    schedulers."""

    def __init__(self):
        super().__init__(
            key=3300,
            scope=0,
            principal='nvoTimeDate'
        )
        self.datapoints['nvoTimeDate'] = base.Profile.DatapointMember(
            doc="""Real time output to the network.  Actual real time and
            date on the network for all linked objects.""",
            name='nvoTimeDate',
            profile=self,
            number=1,
            datatype=SNVT_time_stamp,
            mandatory=True,
            service=base.Profile.DatapointMember.REPEATED,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciUpdateRate':
                base.Profile.PropertyMember(
                    doc="""Time broadcast.  Update rate of the output should
                    be kept at 1 minute, 1 hour, or 1 day.""",
                    name='nciUpdateRate',
                    profile=self,
                    number=2,
                    datatype=SCPTupdateRate,
                    minimum=b'\x02\x58',
                    maximum=b'\x8c\xa0',
                    mandatory=False
                )
            }
        )
        self.datapoints['nviTimeSet'] = base.Profile.DatapointMember(
            doc="""Time input from a synchronizing source.  To set the
            initial/seed time of the clock (for a clock that does not set
            it's own initial time)""",
            name='nviTimeSet',
            profile=self,
            number=2,
            datatype=SNVT_time_stamp,
            mandatory=False,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.properties['nciMasterSlave'] = base.Profile.PropertyMember(
            doc="""Master or slave clock.  "1" means "Master Clock Mode".
            "0" means "Slave Clock Mode".""",
            name='nciMasterSlave',
            profile=self,
            number=1,
            datatype=SCPTmasterSlave,
            mandatory=False
        )
        self.properties['nciSummerTime'] = base.Profile.PropertyMember(
            doc="""Summer date and time.  When not used entry shall be all
            "0" values.  Year, minutes, and seconds are always "0".""",
            name='nciSummerTime',
            profile=self,
            number=3,
            datatype=SCPTsummerTime,
            mandatory=False
        )
        self.properties['nciWinterTime'] = base.Profile.PropertyMember(
            doc="""Winter date and time.  When not used entry shall be all
            "0" values.  Year, minutes, and seconds are always "0".""",
            name='nciWinterTime',
            profile=self,
            number=4,
            datatype=SCPTwinterTime,
            mandatory=False
        )
        self.properties['nciManualAllowed'] = base.Profile.PropertyMember(
            doc="""Manual time updating allowed.  "1" means "Allowed".  "0"
            means "Disallowed".""",
            name='nciManualAllowed',
            profile=self,
            number=5,
            datatype=SCPTmanualAllowed,
            mandatory=False
        )
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = SFPTrealTimeKeeper()
    pass
