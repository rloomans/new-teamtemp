import os

import dj_database_url

from teamtemp.settings.base import *

DEBUG = os.environ.get('DJANGO_DEBUG', True)
SECRET_KEY = os.environ.get(
    'TEAMTEMP_SECRET_KEY',
    'rp47vufz8lrr1cxki7lmc9w221ajgauk5ctv6xi')

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(PROJECT_DIR, 'teamtemp.sqlite'),
        conn_max_age=600
    )
}
