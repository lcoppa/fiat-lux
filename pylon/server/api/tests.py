#
# Copyright (c) 2013 Echelon Corporation.  All rights reserved.
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

"""
Pilon IP-C Server REST API tests.

This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

__version__ = "$Revision: #5 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/tests.py $


from django.test import TestCase

from api.models.device import Device


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class DeviceTest(TestCase):
    """ `Device` model tests. """
    
    def test_device(self):
        #""" Test `Device` class."""
        device = Device()
        self.assertIsNotNone(device)
        self.assertEqual(str(device), "0:  ()")
        device.clean()
        
        device = Device(name='device1')
        self.assertEqual(str(device), "0: device1 ()")
        device.clean()
                
        device = Device(name='device2', devid='lon.devid2')
        self.assertEqual(str(device), "0: device2 (lon.devid2)")
        device.clean()
