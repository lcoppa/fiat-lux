"""
    SFPTnodeObject
"""

#
# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pylon.resources import base
from pylon.resources.standard import standard

from pylon.resources.SNVT_obj_request import SNVT_obj_request
from pylon.resources.SNVT_obj_status import SNVT_obj_status
from pylon.resources.SCPTnwrkCnfg import SCPTnwrkCnfg
from pylon.resources.SCPTmaxSndT import SCPTmaxSndT


class SFPTnodeObject(base.Profile):
    """SFPTnodeObject standard profile.

    Node Object.  Allows the function of objects within a node to be monitored.
    Only one may exist on a node.
    """

    def __init__(self):
        super().__init__(
            key=0,
            scope=0,
            principal='nvoStatus',
        )
        self._definition = standard.add(self)
        self.properties['nciNetConfig'] = base.Profile.PropertyMember(
            doc="""
            Network configuration source:
            Indicates whether the node will configure itself, or
            expects a network manager.
            """,
            name='nciNetConfig',
            profile=self,
            number=1,
            datatype=SCPTnwrkCnfg,
            mandatory=False,
            flags=base.PropertyFlags.RESET
        )

        self.datapoints['nviRequest'] = base.Profile.DatapointMember(
            doc="""
            Object request:   Requests a particular mode for a particular
            object in the device.
            """,
            name='nviRequest',
            profile=self,
            number=1,
            datatype=SNVT_obj_request,
            mandatory=True,
            direction=base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoStatus'] = base.Profile.DatapointMember(
            doc="""
            Object status: Reports the status of requested object in the
            device.
            """,
            name='nvoStatus',
            profile=self,
            number=2,
            datatype=SNVT_obj_status,
            mandatory=True,
            direction=base.Profile.DatapointMember.OUTPUT,
            properties={
                'nciMaxStsSendT':
                base.Profile.PropertyMember(
                    doc="""
                    Maximum send time:   Controls the maximum period of time
                    before the object status is transmitted; Zero (0) means
                    disabled.
                    """,
                    name='nciMaxStsSendT',
                    profile=self,
                    number=2,
                    datatype=SCPTmaxSndT,
                    mandatory=False
                )
            }
        )
        self.finalize()

# ### TODO REMINDER: add missing datapoint and property members
