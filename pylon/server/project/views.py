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
Pilon IP-C Server project-level views.
"""

__version__ = "$Revision: #5 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/project/views.py $


import datetime

from django.http import Http404, HttpResponse


def home(request):
    """
    The home page view.
    """
    content = """
    <h1>Gary's IP-C Server Home Page</h1>
    What's here:
    <ul>
        <li><a href="/">This home page.</a></li>
        <li><a href="/hello/">Hello World!</a></li>
        <li><a href="/time/">The current time.</a></li>
        <li><a href="/time/+3/">The time in <b>3</b> hours.</a></li>
        <li><a href="/admin/">The Django administration interface.</a></li>
        <li>The Django REST Framework authentication interface:</li>
        <ul>
            <li><a href="/auth/login/">Log in.</a></li>
            <li><a href="/auth/logout/">Log out.</a></li>
        </ul>
        <li><a href="/api/"><b>The IP-C Server REST API.</b></a></li>
    </ul>
    """
    return HttpResponse(content)


def hello(request):
    """
    The Hello World view.
    """
    return HttpResponse("Hello World!")


def time(request):
    """
    The current time view.
    """
    return HttpResponse("The current time is: <b>%s</b>" % datetime.datetime.now())


def time_plus(request, plus):
    """
    The current time view.
    """
    try:
        hours = int(plus)
    except ValueError:
        raise Http404()
    time = datetime.datetime.now() + datetime.timedelta(hours=hours)
    return HttpResponse("The time in %d hours is: <b>%s</b>" % (hours, time))
