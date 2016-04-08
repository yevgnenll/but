from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from users.models import User


class UserLoginView(View):

    def get(self, request):

        return render(
                request,
                "users/login.html",
                {}
         )

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next_page") or reverse("home")

        is_user = authenticate(
                username=username,
                password=password,
        )

        if is_user:
            login(request, is_user)
            return redirect(next_page)
        else:
            messages.add_message(request, messages.ERROR, "ID나 비밀번호가 틀렸습니다")
            return render(
                    request,
                    "users/login.html",
                    {}
            )
