from django.contrib.auth import logout

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def logout_user(request):

    logout(request)
    return redirect(reverse("home"))
