from django.conf.urls import url, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_framework_views

app_name = 'user'

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [

    #url(r'^users/current/$', views.UserDetail.as_view()),
    #url(r'^login/$', views.UserAuth.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    #url(r'^user/login/$', views.UserAuthToken.as_view(), name='login'),
    #url(r'^user/logout/$', views.LogOutView.as_view(), name='logout'),
	#url(r'^user/create/$', views.CreateUserView.as_view(), name='createuser'),
    #url(r'^user/registerPush/$', views.RegisterForPush.as_view(), name='registerPush'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)