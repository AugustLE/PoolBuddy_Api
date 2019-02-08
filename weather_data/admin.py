from django.contrib import admin
from .models import DayData, City, Forecast
# Register your models here.

admin.site.register(DayData)
admin.site.register(City)
admin.site.register(Forecast)