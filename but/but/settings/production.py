from .partial import *

import raven

import os


DEBUG = False

ALLOWED_HOSTS = [
    "*",
]

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': 'https://e5f71612f02944c1918e54e156ac3976:8041940a51d34500accba3cfd92a06c7@app.getsentry.com/73401',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'fastagram.s3storage_fastagram.S3PipelineCachedStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = 'do0qcfch9z2l2.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://do0qcfch9z2l2.cloudfront.net/"
