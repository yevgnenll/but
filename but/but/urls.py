from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

from social.utils import setting_name
from social.apps.django_app import views

from but.views import HomeView
from users.views import SignupView, logout_user, UserLoginView, UserProfileView, UserProfileModifyView
from trades.views import SellCreateView


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', UserLoginView.as_view(), name="login"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'^register/goods/$', SellCreateView.as_view(), name="register_goods"),

    # url(r'^logout/facebook/$', , name="facebook"),
    # url(r'^logout/kakao/$', , name="kakao"),
    url(r'^user/(?P<slug>\w+)/modify/$', UserProfileModifyView.as_view(), name="profile_modify"),
    url(r'^user/(?P<slug>\w+)/$', UserProfileView.as_view(), name="profile"),

    url('', include('social.apps.django_app.urls', namespace='social')),

]
