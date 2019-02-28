from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views as rest_framework_views

app_name = 'weather_data'

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [

    #url(r'^data/days/all/$', views.GetDayDataView.as_view()),
    # ex: /met/hive
    url(r'^met/(?P<city>\w+)/$', views.met),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)