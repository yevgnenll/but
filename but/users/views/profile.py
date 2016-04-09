from django.views.generic.detail import DetailView

from users.models import User


class UserProfileView(DetailView):

    model = User
    slug_field = 'username'
    template_name = 'users/profile.html'
