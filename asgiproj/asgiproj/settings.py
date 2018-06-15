import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "secret-key"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = ["asgiapp"]

MIDDLEWARE = []

ROOT_URLCONF = "asgiproj.urls"

ASGI_APPLICATION = "asgiproj.asgi.application"
