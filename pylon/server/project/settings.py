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
Pilon IP-C Server projects settings.
"""

__version__ = "$Revision: #12 $"
# $File: //depot/Software/Pylon/Dev/Python/Server/RestApi/project/settings.py $


import os


# determine absolute path to (this) project directory and the root (parent) directory
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gary Bartlett', 'garyb@echelon.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOT_DIR, 'sqlite3.db'),                   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_DIR, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+as%3gym0q*4gn67tnod!!=8$j+15czp91gjub%xg^8a*i2t)@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(ROOT_DIR, "templates"),
)

# NOTE: <https://docs.djangoproject.com/en/1.5/ref/templates/api/#django.template.loaders.app_directories.Loader>
#       The order of INSTALLED_APPS is significant! For example, if you want
#       to customize the Django admin, you might choose to override the
#       standard admin/base_site.html template, from django.contrib.admin,
#       with your own admin/base_site.html in myproject.polls. You must then
#       make sure that your myproject.polls comes before django.contrib.admin
#       in INSTALLED_APPS, otherwise django.contrib.admin‘s will be loaded
#       first and yours will be ignored.
INSTALLED_APPS = (
    # Pilon IP-C Server REST API
    'api',                          # must be listed first (see note above)

    # Django
    # DOC: <https://docs.djangoproject.com/en/1.5/ref/contrib/admin/>
    'django.contrib.admin',         # Django admin application
    'django.contrib.admindocs',     # Django admin documentation
    'django.contrib.auth',          # user authentication system
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',      # anonymous sessions
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # South (database schema migration)
    #'south',

    # Django REST Framework
    'rest_framework',

    # Gunicorn WSGI Server
    'gunicorn',                     # adds 'manage.py run_gunicorn'
)    

# DOC: <http://django-rest-framework.org/api-guide/settings.html>
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',                # (default)
        'rest_framework.renderers.XMLRenderer',
        'rest_framework.renderers.YAMLRenderer',                # requires: pyyaml
        'rest_framework.renderers.BrowsableAPIRenderer'         # (default)
    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',                    # (default)
        'rest_framework.parsers.FormParser',                    # (default)
        'rest_framework.parsers.MultiPartParser',               # (default)
        'rest_framework.parsers.XMLParser',                     # requires: defusedxml
        'rest_framework.parsers.YAMLParser'                     # requires: pyyaml
    ),
                  
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # (default)
        'rest_framework.authentication.BasicAuthentication'     # (default)
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.AllowAny',                 # (default)
        
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
                  
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        # Use hyperlinked styles by default.
        # Only used if the `serializer_class` attribute is not set on a view.
        'rest_framework.serializers.HyperlinkedModelSerializer',
    
    # DOC: <http://django-rest-framework.org/api-guide/content-negotiation.html#setting-the-content-negotiation>
    'DEFAULT_CONTENT_NEGOTIATION_CLASS':
        'api.content_negotiation.ContentNegotiation',
    
    # DOC: <http://django-rest-framework.org/api-guide/filtering.html#generic-filtering>
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    )   
}

# Pilon IP-C Server configuration settings
PILON = {
    # A (named) collection of Pilon IP-C Server Collectors that will
    # be started to collect and update devices and datapoints.
    # Names must be no longer than 30 characters and consist only of
    # letters, numbers, underscores or hyphens.
    'COLLECTORS': {
        # local LonBridge Server
        'lonbridge': {
            'collector': 'collectors.lonbridge.LonBridgeCollector',
            'args': {
                'host': 'localhost',
                'port': 3050
            }
        },
                   
        # localhost collector    
        'localhost': {
            'collector': 'collectors.localhost.LocalhostCollector',
            'args': {
                'poll': 5
            }
        }
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# DOC: <https://docs.djangoproject.com/en/1.5/topics/logging/#configuring-logging>
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
           
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'default': {
            'format': '%(asctime)s %(levelname)-8s %(name)s:%(lineno)d:%(funcName)s  %(message)s'
        },
        'simple': {
            'format': '%(levelname)s|%(message)s'
        },
    },
           
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler'
        },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'default'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, 'django.log'),
            'formatter': 'default'
        }
    },
           
    'loggers': {
        # default logger for this project
        'project': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True
        },
        'pilon': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True
        },
                
        # ignore DEBUG messages from the content_negotiation module
        'pilon.server.api.content_negotiation': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            'propagate': False
        },
                
        # other loggers could include '' (catch-all), 'project.views', 'api', 'api.views', etc.
        
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
    }
}
