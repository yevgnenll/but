import dj_database_url
import os

from .base import BASE_DIR


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default':  dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
    )
}
