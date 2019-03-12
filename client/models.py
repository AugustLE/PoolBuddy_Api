from django.db import models
from user.models import CustomUser

#temperatures in celcius

class ForeastShortTerm(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	date = models.DateField()
	temp_0_to_2 = models.FloatField(null=True, blank=True)
	temp_2_to_4 = models.FloatField(null=True, blank=True)
	temp_4_to_6 = models.FloatField(null=True, blank=True)
	temp_6_to_8 = models.FloatField(null=True, blank=True)
	temp_8_to_10 = models.FloatField(null=True, blank=True)
	temp_10_to_12 = models.FloatField(null=True, blank=True)
	temp_12_to_14 = models.FloatField(null=True, blank=True)
	temp_14_to_16 = models.FloatField(null=True, blank=True)
	temp_16_to_18 = models.FloatField(null=True, blank=True)
	temp_18_to_20 = models.FloatField(null=True, blank=True)
	temp_20_to_22 = models.FloatField(null=True, blank=True)
	temp_22_to_24 = models.FloatField(null=True, blank=True)

	def __str__(self):
		return str(self.date)


#temperatures in celcius
class ForecastLongTerm(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	date = models.DateField()
	temp_0_to_6 = models.FloatField(null=True, blank=True)
	temp_6_to_12 = models.FloatField(null=True, blank=True)
	temp_12_to_18 = models.FloatField(null=True, blank=True)
	temp_18_to_24 = models.FloatField(null=True, blank=True)

	def __str__(self):
		return str(self.date)
