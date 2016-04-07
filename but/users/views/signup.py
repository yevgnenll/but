from users.models import User

from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login


class SignupView(View):

    def get(self, request):

        return render(
                request,
                "users/signup.html",
                {}
        )

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        User.objects.create_user(
                username=username,
                password=password,
                email=email,
        )
        user = authenticate(
                username=username,
                password=password,
        )

        login(request, user)

        return redirect("home")
