"""controller standard profile, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.Note this resource is marked as obsolete.
It should not be used for new development, but continued use in existing
designs is permitted."""


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


class controller(pylon.resources.base.Profile):
    """controller standard profile.  Controller A basic object that is
    designed to interface to multiple sensor and actuator objects.  It has no
    standardized content."""

    def __init__(self):
        super().__init__(
            key=5,
            scope=0,
            principal='nvoValue'
        )
        self.datapoints['nvoValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Value output.  Transmitted data.""",
            name='nvoValue',
            profile=self,
            number=1,
            datatype=pylon.resources.base.xxx,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nviValueFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Value feedback input.  Feedback return input whenever a
            destination object's input NV receives an update.""",
            name='nviValueFb',
            profile=self,
            number=2,
            datatype=pylon.resources.base.xxx,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Value input.  Received data from a data source object.""",
            name='nviValue',
            profile=self,
            number=3,
            datatype=pylon.resources.base.xxx,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoValueFb'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Value feedback output.  Feedback return output for the
            input NV, used for synchronization in multiple relationships.""",
            name='nvoValueFb',
            profile=self,
            number=4,
            datatype=pylon.resources.base.xxx,
            mandatory=False,
            direction=pylon.resources.base.Profile.DatapointMember.OUTPUT
        )
        self._original_name = 'SFPTcontroller'
        self._mark_obsolete()
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = controller()
    pass
