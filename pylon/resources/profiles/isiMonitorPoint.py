"""isiMonitorPoint standard profile, originally defined in resource file set
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


class isiMonitorPoint(pylon.resources.base.Profile):
    """isiMonitorPoint standard profile.  ISI Monitor Point.  Provides a
    monitoring input for use by a controller monitoring an ISI network.  The
    input uses automatic enrollment to provide an easy way for a controller
    and monitored device to work together to support event-driven updates,
    providing a method that minimizes network transactions and provides easy
    set up for devices that support automatic enrollment."""

    def __init__(self):
        super().__init__(
            key=8,
            scope=0,
            principal='nviValue'
        )
        self.datapoints['nviValue'] = pylon.resources.base.Profile.DatapointMember(
            doc="""Input value.  Input value used in automatic connections
            initiated by the controller.""",
            name='nviValue',
            profile=self,
            number=1,
            datatype=pylon.resources.base.xxx,
            mandatory=True,
            direction=pylon.resources.base.Profile.DatapointMember.INPUT
        )
        self._original_name = 'SFPTisiMonitorPoint'
        self._definition = standard.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = isiMonitorPoint()
    pass
