"""
    SCPTdefOutput
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


class SCPTdefOutput(base.Inheriting):
    """SCPTdefOutput standard property type.

    For a sensor functional block, this configuration property determines the
    position or level that the primary output network variable for the
    functional block should adopt, when no updates are received from the
    hardware within the maximum receive time, at power-on or reset, and when
    an override request is received for the functional block.
    For an actuator functional block, this configuration property determines
    the position or level that the actuator should adopt, when no updates are
    received by primary input network variable within the maximum receive time,
    at power-on or reset, and when an override request is received for the
    functional block.

    The override behavior is defined by the SCPTovrBehave and SCPTovrValue
    configuration properties.
    """

    def __init__(self):
        super().__init__()
        self._property_scope, self._property_key = 0, 7
        self._definition = standard.add(self)

