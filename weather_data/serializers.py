from rest_framework import serializers
from .models import DayData

class DayDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayData
		fields = (
			'day',
			'is_active'
		)