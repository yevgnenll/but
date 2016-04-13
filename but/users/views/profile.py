from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User


class UserProfileView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = 'username'
    template_name = 'users/profile.html'
