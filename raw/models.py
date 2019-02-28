from django.db import models
from user.models import CustomUser
# Create your models here.
class RegisteredDevice(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    device_id = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.device_id

class RawTempData(models.Model):

    device = models.ForeignKey(RegisteredDevice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    air_temp_C = models.FloatField()
    air_temp_F = models.FloatField()
    water_temp_C = models.FloatField()
    water_temp_F = models.FloatField()

    def __str__(self):
        return self.device.device_id
