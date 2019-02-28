from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import RawTempData, RegisteredDevice
from .serializers import RawDataSerializer
from datetime import datetime
# Create your views here.


class RawDataView(APIView):
	permission_classes = (permissions.AllowAny,)

	@csrf_exempt
	def post(self, request):

		device_id = request.data.get('device_id')
		timestamp = request.data.get('timestamp')
		air_temp_C = request.data.get('air_temp_C')
		air_temp_F =  request.data.get('air_temp_F')
		water_temp_C =  request.data.get('water_temp_C')
		water_temp_F =  request.data.get('water_temp_F')

		device = RegisteredDevice.objects.get(device_id=device_id)
		new_raw_data = RawTempData(
			device=device,
			timestamp=datetime.fromtimestamp(timestamp),
			air_temp_C=air_temp_C,
			air_temp_F=air_temp_F,
			water_temp_C=water_temp_C,
			water_temp_F=water_temp_F
		)
		new_raw_data.save()

		return Response('Content saved')

	@csrf_exempt
	def get(self, request, device_id):

		device = RegisteredDevice.objects.get(device_id=device_id)
		queryset = RawTempData.objects.filter(device=device)
		data = RawDataSerializer(queryset, many=True).data
		return Response(data, status=status.HTTP_200_OK)






