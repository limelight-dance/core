import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'a%5cb20uhnfwol1ipk6$i$4*-a+#km1(-6#ri_gp9e1zvy6u*+'

DEBUG = True

ALLOWED_HOSTS = ['limelight-dance-core.herokuapp.com']

INSTALLED_APPS = [
    'api',
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
