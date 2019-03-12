from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import City, Forecast, RawModelOutput
# Register your models here.


class ForecastAdmin(admin.ModelAdmin):
	list_display = ('temp_from', 'temp_to')
	#ordering = ['-temp_from']


admin.site.register(City)
admin.site.register(Forecast, ForecastAdmin)
admin.site.register(RawModelOutput)