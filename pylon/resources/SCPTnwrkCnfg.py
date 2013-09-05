"""
    SCPTnwrkCnfg
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

from pylon.resources.standard import standard

from pylon.resources.config_source_t import config_source_t
from pylon.resources.SNVT_config_src import SNVT_config_src


class SCPTnwrkCnfg(SNVT_config_src):
    """SCPTnwrk standard property type.

    Network configuration source.

    The value of this field determines the source of the node's network
    configuration. The configuration property set the source for network
    configuration for a device. The source may be the device itself, called
    self-installation, or an external network tool. All devices that support
    self-installation must provide this configuration property to allow a
    network tool to take control of the device’s network configuration.
    """

    def __init__(self, default_value=config_source_t.CFG_EXTERNAL):
        super().__init__(
            default_value=default_value
        )
        self._definition = standard.add(self)
        self._property_scope, self._property_key = 0, 25

