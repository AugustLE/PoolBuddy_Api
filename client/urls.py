from django.conf.urls import url, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'client'

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [

    url(r'^client/getshortterm/$', views.ShortTermForecastView.as_view()),
	url(r'^client/getlongterm/$', views.LongTermForecastView.as_view()),
	url(r'^client/getcities/$', views.CityView.as_view()),
	url(r'^client/registercity/$', views.CityView.as_view()),
	url(r'^client/unregcity/$', views.UnregisterCity.as_view()),
	url(r'^client/updateforecast/(?P<f_type>\w+)/$', views.UpdateForecastsView.as_view())

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)