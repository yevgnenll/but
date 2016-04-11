from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static

from social.utils import setting_name
from social.apps.django_app import views

from but.views import HomeView
from users.views import SignupView, logout_user,\
        UserLoginView, UserProfileView, UserProfileModifyView
from trades.views import SellCreateView, GoodsListView,\
    GoodsDetailView, SellUpdateView, OrderPageView, OrderCheckView,\
    OrderCompleteView


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', UserLoginView.as_view(), name="login"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'^register/goods/$', SellCreateView.as_view(), name="register_goods"),
    url(r'^sell/list/$', GoodsListView.as_view(), name="goods_list"),
    url(r'^sell/(?P<slug>\w+)/modify/$', SellUpdateView.as_view(), name="goods_modify"),
    url(r'^sell/(?P<slug>\w+)/$', GoodsDetailView.as_view(), name="goods_detail"),

    url(r'^buy/check/(?P<slug>\w+)/$', OrderCheckView.as_view(), name="buy_check"),
    url(r'^buy/(?P<slug>\w+)/complete/$', OrderCompleteView.as_view(), name="buy_complete"),
    url(r'^buy/(?P<slug>\w+)/$', OrderPageView.as_view(), name="buy_page"),

    url(r'^user/(?P<slug>\w+)/modify/$', UserProfileModifyView.as_view(), name="profile_modify"),
    url(r'^user/(?P<slug>\w+)/$', UserProfileView.as_view(), name="profile"),

    url('', include('social.apps.django_app.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
