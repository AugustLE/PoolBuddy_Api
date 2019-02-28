from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import City, Forecast
# Register your models here.

admin.site.register(City)
admin.site.register(Forecast)