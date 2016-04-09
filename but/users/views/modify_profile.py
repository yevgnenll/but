from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from users.models import User


class UserProfileModifyView(LoginRequiredMixin, View):

    def get(self, request, slug):

        user = User.objects.get(username=slug)
        enter_user = request.user

        if user.username != enter_user.username:
            messages.add_message(
                    request,
                    messages.ERROR,
                    "개인정보는 본인만 수정이 가능합니다"
            )

            return redirect('home')
        context = {
                'user': user
        }

        return render(
                request,
                "users/modify_profile.html",
                context
        )

    def post(self, request, slug):

        profile_image = request.FILES.get('image') or False
        email = request.POST.get('email')
        description = request.POST.get('description')
        phone_number = request.POST.get('phone_number')

        user = User.objects.get(username=slug)

        if profile_image:
            user.profile_image = profile_image

        user.email = email
        user.phone_number = phone_number
        user.description = description
        user.save()

        return redirect(reverse(
            'profile', kwargs={
                'slug': slug,
                }
            )
        )
