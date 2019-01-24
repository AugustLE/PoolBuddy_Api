from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DayDataSerializer
from .models import DayData
from rest_framework import status, permissions


class GetDayDataView(APIView):
	#permission_classes = (permissions.IsAuthenticated,)

	@csrf_exempt
	def get(self, request):
		all_days = DayData.objects.all()
		data = DayDataSerializer(all_days, many=True).data
		return Response(data, status=status.HTTP_200_OK)