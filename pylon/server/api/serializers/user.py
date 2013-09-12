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
Pilon IP-C Server REST API User serializer.
"""

__version__ = "$Revision: #6 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/api/serializers/user.py $


from django.contrib.auth.models import User

from rest_framework             import serializers

__all__ = ['UserSerializer']


# DOC: <http://django-rest-framework.org/api-guide/serializers.html#hyperlinkedmodelserializer>
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    'ModelSerializer' for the 'User' model.
    """
    #api = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model  = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')
        #exclude = ()