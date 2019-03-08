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


