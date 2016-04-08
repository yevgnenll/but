from django.contrib.auth import logout

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def logout(request):

    logout(request)
    return revrse("home")
