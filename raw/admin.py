from django.contrib import admin
from .models import RegisteredDevice, RawTempData
# Register your models here.
admin.site.register(RegisteredDevice)
admin.site.register(RawTempData)