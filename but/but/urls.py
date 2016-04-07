from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

from social.utils import setting_name
from social.apps.django_app import views

from but.views import HomeView


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),

    url('', include('social.apps.django_app.urls', namespace='social')),

]
