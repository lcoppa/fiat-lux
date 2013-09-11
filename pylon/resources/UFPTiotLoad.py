"""UFPTiotLoad userdefined profile, originally defined in resource file set
iot 90:00:00:05:00:00:00:00-1.Note this resource is marked as obsolete.  It
should not be used for new development, but continued use in existing designs
is permitted."""


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
from pylon.resources.userdefined import userdefined
from pylon.resources.UNVT_iot_load_control import UNVT_iot_load_control


class UFPTiotLoad(base.Profile):
    """UFPTiotLoad userdefined profile.  IoT Load.  IoT load actuator for a
    lighting, sunblind, fan, motor, or other load ."""

    def __init__(self):
        super().__init__(
            key=20003,
            scope=1
        )
        self.datapoints['nviLoadControl'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Load control input value.""",
            name='nviLoadControl',
            profile=self,
            number=1,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoLoadStatus'] = base.Profile.DatapointMember(
            doc="""IoT load control.  Load control status output.""",
            name='nvoLoadStatus',
            profile=self,
            number=2,
            datatype=UNVT_iot_load_control,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT
        )
        self._mark_obsolete()
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = UFPTiotLoad()
    pass
