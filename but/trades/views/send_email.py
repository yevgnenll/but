from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from trades.models import Contact
from users.models import User


def send_email(request):

    title = request.POST.get('title')
    content = request.POST.get('content')
    accept = request.POST.get('user_id')

    contact = Contact.objects.create(
        send=request.user,
        message_text=content,
        message_title=title,
        accept=User.objects.get(id=accept),
    )

    return redirect(request.META.get('HTTP_REFERER'))
