from rest_framework import serializers
from .models import RawTempData, RegisteredDevice

class RawDataSerializer(serializers.ModelSerializer):

	device_id = serializers.PrimaryKeyRelatedField(queryset=RegisteredDevice.objects.all(), source='device.device_id')

	class Meta:
		model = RawTempData
		fields = (
			'device_id',
			'timestamp',
			'air_temp_C',
			'air_temp_F',
			'water_temp_C',
			'water_temp_F'
		)