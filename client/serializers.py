from rest_framework import serializers
from .models import ForeastShortTerm, ForecastLongTerm
from weather_data.models import City

class ForecastShortTermSerializer(serializers.ModelSerializer):

	class Meta:
		model = ForeastShortTerm
		fields = (
			'pk',
			'date',
			'temp_0_to_2',
			'temp_2_to_4',
			'temp_4_to_6',
			'temp_6_to_8',
			'temp_8_to_10',
			'temp_10_to_12',
			'temp_12_to_14',
			'temp_14_to_16',
			'temp_16_to_18',
			'temp_18_to_20',
			'temp_20_to_22',
			'temp_22_to_24'
		)


class ForecastLongTermSerializer(serializers.ModelSerializer):

	class Meta:
		model = ForecastLongTerm
		fields = (
			'pk',
			'date',
			'temp_0_to_6',
			'temp_6_to_12',
			'temp_12_to_18',
			'temp_18_to_24',
		)


class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = (
			'pk',
			'city_name',
			'latitude',
			'longitude'
		)