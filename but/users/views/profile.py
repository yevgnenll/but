from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from users.models import User


class UserProfileView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = 'username'
    template_name = 'users/profile.html'

    def dispatch(self, request, *args, **kwargs):

        page_slug = kwargs.get('slug')
        page_user = User.objects.get(
                username=page_slug,
        )

        if page_user == request.user:
            messages.add_message(
                    request,
                    messages.INFO,
                    "나의 프로필에 들어왔습니다",
            )
        else:
            messages.add_message(
                    request,
                    messages.INFO,
                    "{{page_user}}님의 프로필에 들어왔습니다".foramt(
                        page_user=page_user.username,
                        )
                    )
        return super(UserProfileView, self).dispatch(request, args, kwargs)
