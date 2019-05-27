import os
import dotenv
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOTENV = os.path.join(BASE_DIR, '.env')
if os.path.isfile(DOTENV):
    dotenv.load_dotenv(DOTENV)

SECRET_KEY = 'a%5cb20uhnfwol1ipk6$i$4*-a+#km1(-6#ri_gp9e1zvy6u*+'

DEBUG = True

ALLOWED_HOSTS = [
    'limelight-dance-core.herokuapp.com',
]

INSTALLED_APPS = [
    'api',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

CORS_ORIGIN_WHITELIST = [
    'https://limelight-dance-ui.herokuapp.com',
    'http://limelight-dance-ui.herokuapp.com',
    'http://localhost:8080',
]
