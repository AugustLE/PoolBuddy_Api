from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import datetime
from .models import ForeastShortTerm, ForecastLongTerm
from weather_data.models import City
from .serializers import ForecastShortTermSerializer, ForecastLongTermSerializer, CitySerializer
from user.serializers import SimpleUserSerializer, UserSerializer
from raw.models import RegisteredDevice
from weather_data.models import Forecast, RawModelOutput


class ShortTermForecastView(APIView):

	@csrf_exempt
	def get(self, request):

		time_now = datetime.datetime.now() - datetime.timedelta(hours=8)
		time_end = time_now + datetime.timedelta(days=3)
		queryset = ForeastShortTerm.objects.filter(date__range=[time_now, time_end], user=request.user)
		data = ForecastShortTermSerializer(queryset, many=True).data
		return Response(data, status=status.HTTP_200_OK)


class LongTermForecastView(APIView):

	@csrf_exempt
	def get(self, request):

		time_now = datetime.datetime.now() - datetime.timedelta(hours=8)
		time_end = time_now + datetime.timedelta(days=10)
		queryset = ForecastLongTerm.objects.filter(date__range=[time_now, time_end], user=request.user)
		data = ForecastLongTermSerializer(queryset, many=True).data
		return Response(data, status=status.HTTP_200_OK)


class CityView(APIView):

	@csrf_exempt
	def get(self, request):
		search_word = request.GET.get('city_search')
		queryset = City.objects.filter(city_name__icontains=search_word)
		data = CitySerializer(queryset, many=True).data
		return Response(data, status=status.HTTP_200_OK)


	@csrf_exempt
	def post(self, request):

		city_pk = request.data.get('city_pk')
		city = City.objects.get(pk=city_pk)
		user = request.user
		user.city = city
		user.save()
		serialized_user = UserSerializer(user, many=False).data
		device = RegisteredDevice.objects.get(user=user)
		serialized_user['device'] = device.device_id
		return Response(serialized_user, status=status.HTTP_200_OK)

class UnregisterCity(APIView):

	@csrf_exempt
	def post(self, request):
		user = request.user
		user.city = None
		user.save()
		data = SimpleUserSerializer(user, many=False).data
		return Response(data, status=status.HTTP_200_OK)

def end_day(time_now):
	return time_now.replace(hour=23, minute=59)



def convert_to_forecast(model, request, f_type):

	time_now = datetime.datetime.now() - datetime.timedelta(hours=8)

	if f_type == 'short_term':
		ForeastShortTerm.objects.filter(user=request.user).delete()
		time_end = time_now + datetime.timedelta(days=3)
		raw_data = model.objects.filter(temp_from__range=[time_now, time_end])

		data_raw = []
		time_shift = time_now
		for n in range(4):
			day_n_data = raw_data.filter(temp_from__range=[time_shift, end_day(time_shift)])
			data_raw.append((day_n_data, time_shift))
			time_shift = time_shift.replace(day=time_shift.day + 1, hour=0, minute=0, second=0, microsecond=0)


		for day_data in data_raw:
			temps = {}
			#for obj in day_data:
			for i in range(len(day_data[0])):
				obj = day_data[0][i]
				hour = obj.temp_from.hour
				if hour % 2 == 0:
					average = (float(obj.temperature) + float(day_data[0][i + 1].temperature)) / 2
					temps[str(hour)] = round(average, 2)
			forecast = ForeastShortTerm(
				user=request.user,
				date=day_data[1],
				temp_0_to_2=temps.get('0', None),
				temp_2_to_4=temps.get('2', None),
				temp_4_to_6=temps.get('4', None),
				temp_6_to_8=temps.get('6', None),
				temp_8_to_10=temps.get('8', None),
				temp_10_to_12=temps.get('10', None),
				temp_12_to_14=temps.get('12', None),
				temp_14_to_16=temps.get('14', None),
				temp_16_to_18=temps.get('16', None),
				temp_18_to_20=temps.get('18', None),
				temp_20_to_22=temps.get('20', None),
				temp_22_to_24=temps.get('22', None),
			)
			forecast.save()

	elif f_type == 'long_term':
		ForecastLongTerm.objects.filter(user=request.user).delete()
		time_end = time_now + datetime.timedelta(days=10)
		raw_data = model.objects.filter(temp_from__range=[time_now, time_end])

		data_raw = []
		time_shift = time_now + datetime.timedelta(days=3)
		for n in range(11):
			day_n_data = raw_data.filter(temp_from__range=[time_shift, end_day(time_shift)])
			data_raw.append((day_n_data, time_shift))
			time_shift = time_shift.replace(day=time_shift.day + 1, hour=0, minute=0, second=0, microsecond=0)

		for day_data in data_raw:
			length = len(day_data[0])
			#print(day_data[0][0].temperature)
			all_null = True
			for d_temp in day_data[0]:
				if d_temp.temperature:
					all_null = False

			if all_null:
				break
			forecast_longterm = ForecastLongTerm(user=request.user, date=day_data[1])
			if length == 1:
				forecast_longterm.temp_18_to_24 = day_data[0][0].temperature

			elif length == 2:
				forecast_longterm.temp_12_to_18 = day_data[0][0].temperature
				forecast_longterm.temp_18_to_24 = day_data[0][1].temperature

			elif length == 3:
				forecast_longterm.temp_6_to_12 = day_data[0][0].temperature
				forecast_longterm.temp_12_to_18 = day_data[0][1].temperature
				forecast_longterm.temp_18_to_24 = day_data[0][2].temperature
			elif length == 4:
				forecast_longterm.temp_0_to_6 = day_data[0][0].temperature
				forecast_longterm.temp_6_to_12 = day_data[0][1].temperature
				forecast_longterm.temp_12_to_18 = day_data[0][2].temperature
				forecast_longterm.temp_18_to_24 = day_data[0][3].temperature

			forecast_longterm.save()



class UpdateForecastsView(APIView):
	#permission_classes = (permissions.AllowAny,)

	@csrf_exempt
	def post(self, request, f_type):
		#
		# query = forecast data
		#prediction =  anders implimenterer prediksjon(query)

		# TODO: I stedet for å putte inn Forecast som model argument, putt in RawModelOutput
		convert_to_forecast(model=Forecast, request=request, f_type=f_type)
		return Response('OK', status=status.HTTP_200_OK)


