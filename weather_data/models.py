from django.db import models

# Create your models here.

class DayData(models.Model):
	day = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.day
