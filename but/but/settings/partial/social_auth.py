from .base import INSTALLED_APPS

import os


INSTALLED_APPS += [
    'social.apps.django_app.default',
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

AUTHENTICATION_BACKENDS = (
    'social.backends.kakao.KakaoOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    # default setting
    'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_USER_MODEL = 'users.User'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/login/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/"
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = "/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/"
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"
