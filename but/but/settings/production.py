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
    'dsn': 'https://db63343960c84fe0851b9167e95b95b3:d1f369f174774676a11363b42976a6e3@app.getsentry.com/72480',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'fastagram.s3storage_fastagram.S3PipelineCachedStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = 'do0qcfch9z2l2.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://do0qcfch9z2l2.cloudfront.net/"
