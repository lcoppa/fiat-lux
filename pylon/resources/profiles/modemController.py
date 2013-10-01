"""modemController standard profile, originally defined in resource file set
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
import pylon.resources.datapoints.str_asc
import pylon.resources.datapoints.switch
import pylon.resources.datapoints.telcom
import pylon.resources.properties.autoAnswer


class modemController(pylon.resources.base.Profile):
    """modemController standard profile.  Modem Controller.  A Modem
    Controller is used to control the functions of a data modem (POTS, ISDN,
    etc.)."""

    def __init__(self):
        super().__init__(
            key=5091,
            scope=0
        )
        self.datapoints['nviDialStr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Dial String Input.  Character string (30 characters
            max)""",
            name='nviDialStr',
            profile=self,
            number=1,
            datatype=pylon.resources.datapoints.str_asc.str_asc,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviCallCancel'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Call Cancel Input.  """,
            name='nviCallCancel',
            profile=self,
            number=2,
            datatype=pylon.resources.datapoints.switch.switch,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoConnectStat'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Connect Status Output.  """,
            name='nvoConnectStat',
            profile=self,
            number=3,
            datatype=pylon.resources.datapoints.telcom.telcom,
            mandatory=True,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoConnectStr'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Connect String Output.  Character string (30 characters
            max)""",
            name='nvoConnectStr',
            profile=self,
            number=4,
            datatype=pylon.resources.datapoints.str_asc.str_asc,
            mandatory=False,
            service=pylon.resources.base.Profile.DatapointMember.ACKNOWLEDGED,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['nciAutoAnswer'] = pylon.resources.base.Profile.PropertyMember(
            doc="""Auto answer.  Enable the automatic call answer function of
            a device.""",
            name='nciAutoAnswer',
            profile=self,
            number=1,
            datatype=pylon.resources.properties.autoAnswer.autoAnswer,
            default=b'\x00',
            mandatory=False
        )
        self._original_name = 'SFPTmodemController'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = modemController()
    pass
