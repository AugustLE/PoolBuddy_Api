from django.db import models
# Create your models here.

class DayData(models.Model):
    day = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.day

# MET API MODELS
class City(models.Model):
    city_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)

    
    def __str__(self):
        return self.city_name
    
class Forecast(models.Model):        
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temp_from = models.CharField(max_length=200)
    temp_to = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    windDirection = models.CharField(max_length=200)
    windSpeed = models.CharField(max_length=200)
    windGust = models.CharField(max_length=200)
    areaMaxWindSpeed = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
    pressure = models.CharField(max_length=200)
    cloudiness = models.CharField(max_length=200)
    fog = models.CharField(max_length=200)
    lowClouds = models.CharField(max_length=200)
    mediumClouds = models.CharField(max_length=200)
    highClouds = models.CharField(max_length=200)
    dewpointTemperature = models.CharField(max_length=200)

    def __str__(self):
        return self.temp_from[-12:-10] + " " +  self.temp_from[-9:-1] + "-" + self.temp_to[-9:-1]







