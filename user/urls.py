from django.conf.urls import url, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_framework_views

app_name = 'user'

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [

    url(r'^user/details/$', views.UserDetail.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token),
    url(r'^user/login/$', views.UserAuthToken.as_view()),
    url(r'^user/logout/$', views.LogOutView.as_view()),
	url(r'^user/register/$', views.RegisterUserView.as_view()),
    url(r'^user/registerpush/$', views.RegisterForPush.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)