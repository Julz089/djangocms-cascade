# Django settings for unit test project.
from __future__ import unicode_literals

import os
import sys

from django.core.urlresolvers import reverse_lazy

from cmsplugin_cascade.extra_fields.config import PluginExtraFieldsConfig
from cmsplugin_cascade.utils import format_lazy

DEBUG = True

BASE_DIR = os.path.dirname(__file__)

# Root directory for this Django project
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir, os.path.pardir))

# Directory where working files, such as media and databases are kept
WORK_DIR = os.path.join(PROJECT_ROOT, 'workdir')

SITE_ID = 1

ROOT_URLCONF = 'bs3demo.urls'

SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WORK_DIR, 'db.sqlite3'),
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'reversion',
    'djangocms_text_ckeditor',
    'django_select2',
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.segmentation',
    'cms',
    'cms_bootstrap3',
    'adminsortable2',
    'menus',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'sass_processor',
    'sekizai',
    'bs3demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

# silence false-positive warning 1_6.W001
# https://docs.djangoproject.com/en/1.8/ref/checks/#backwards-compatibility
#TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(WORK_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(WORK_DIR, 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    ('node_modules', os.path.join(PROJECT_ROOT, 'node_modules')),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
            'bs3demo.context_processors.cascade',
        ),
    },
}]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

#############################################################
# Application specific settings

if sys.argv[1] == 'test':
    CMS_TEMPLATES = (
         ('testing.html', "Default Page"),
    )
else:
    CMS_TEMPLATES = (
         ('main.html', "Main Content"),
         ('wrapped.html', "Wrapped Bootstrap Column"),
    )

CMS_SEO_FIELDS = True

CMS_CACHE_DURATIONS = {
    'content': 3600,
    'menus': 3600,
    'permissions': 86400,
}

CMSPLUGIN_CASCADE_PLUGINS = (
    'cmsplugin_cascade.segmentation',
    'cmsplugin_cascade.generic',
    'cmsplugin_cascade.link',
    'cmsplugin_cascade.bootstrap3',
    'bs3demo',
)

CMSPLUGIN_CASCADE = {
    'alien_plugins': ('TextPlugin', 'TextLinkPlugin',),
    'plugins_with_sharables': {
        'BootstrapImagePlugin': ('image_shapes', 'image_width_responsive', 'image_width_fixed',
                                 'image_height', 'resize_options',),
        'BootstrapPicturePlugin': ('image_shapes', 'responsive_heights', 'image_size', 'resize_options',),
        'BootstrapButtonPlugin': ('button_type', 'button_size', 'button_options', 'icon_font',),
        'TextLinkPlugin': ('link', 'target',),
    },
    'plugins_with_extra_fields': {
        'BootstrapRowPlugin': PluginExtraFieldsConfig(inline_styles={
            'extra_fields:Margins': ['margin-top', 'margin-bottom'],
            'extra_units:Margins': 'px,em'}),
    },
    'bootstrap3': {},
    'allow_plugin_hiding': True,
}
if os.getenv('DJANGO_CLIENT_FRAMEWORK', '').startswith('angular'):
    CMSPLUGIN_CASCADE['bootstrap3']['template_basedir'] = 'angular-ui'

CACSCADE_WORKAREA_GLOSSARY = {
    'breakpoints': ['xs', 'sm', 'md', 'lg'],
    'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
    'fluid': False,
    'media_queries': {
        'xs': ['(max-width: 768px)'],
        'sm': ['(min-width: 768px)', '(max-width: 992px)'],
        'md': ['(min-width: 992px)', '(max-width: 1200px)'],
        'lg': ['(min-width: 1200px)'],
    },
}

CMS_PLACEHOLDER_CONF = {
    # this placeholder is used in templates/main.html, it shows how to
    # scaffold a djangoCMS page starting with an empty placeholder
    'Main Content': {
        'plugins': ['BootstrapContainerPlugin', 'BootstrapJumbotronPlugin'],
        'parent_classes': {'BootstrapContainerPlugin': None, 'BootstrapJumbotronPlugin': None},
        'glossary': CACSCADE_WORKAREA_GLOSSARY,
    },
    # this placeholder is used in templates/wrapped.html, it shows how to
    # add content to an existing Bootstrap column
    'Bootstrap Column': {
        'plugins': ['BootstrapRowPlugin', 'TextPlugin', ],
        'parent_classes': {'BootstrapRowPlugin': None},
        'require_parent': False,
        'glossary': CACSCADE_WORKAREA_GLOSSARY,
    },
}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texticon_wysiwig_config')),
}

SELECT2_CSS = 'node_modules/select2/dist/css/select2.min.css'
SELECT2_JS = 'node_modules/select2/dist/js/select2.min.js'

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/opt/local/bin/optipng {filename}',
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
}

#THUMBNAIL_DEBUG = True

SASS_PROCESSOR_INCLUDE_DIRS = (
    os.path.join(PROJECT_ROOT, 'node_modules'),
)

# to access files such as fonts via staticfiles finders
NODE_MODULES_URL = STATIC_URL + 'node_modules/'
