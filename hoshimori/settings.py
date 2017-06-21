from django.conf import settings as django_settings
from hoshimori import models
from web.default_settings import DEFAULT_ENABLED_PAGES, DEFAULT_NAVBAR_ORDERING

SITE_NAME = 'Sample Website'
SITE_URL = 'http://sample.com/'
SITE_IMAGE = 'hoshimori.png'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.sample.com/'
GAME_NAME = 'Sample Game'
DISQUS_SHORTNAME = 'sample'
ACCOUNT_MODEL = models.Account
COLOR = '#4a86e8'

SITE_NAV_LOGO = 'logo.png'

NAVBAR_ORDERING = ['student_list', 'card_list', 'weapon_list', 'material_list'] + DEFAULT_NAVBAR_ORDERING