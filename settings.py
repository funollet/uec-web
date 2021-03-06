# Django settings for uec-web project.
# -*- coding:utf-8 -*-
import os.path
import sys

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

from settings_local import *

ROOT_URLCONF = 'urls'

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media-admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

APPEND_SLASH = True

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates', ''),
    os.path.join(PROJECT_ROOT, 'templates-global', ''),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'tagging',
    'links',
    'events',
    'txts',
    'filebrowser',
    'feedme', 'feedme-photos',
)

ABSOLUTE_URL_OVERRIDES = {
    'events.event': lambda o: u'/events/%s/%s/' % (o.startdate.strftime('%Y/%m/%d').lower(), o.id) ,
    'txts.txt': lambda o: u'/%s/%s/' % (o.section.easyname, o.easyname),
}

# Tags application.
STYLE_URL = os.path.join(MEDIA_URL, 'tags', '')

FEEDME_CACHE_BACKEND = 'file://%s' % os.path.join(PROJECT_ROOT, 'cache', 'feedme')
