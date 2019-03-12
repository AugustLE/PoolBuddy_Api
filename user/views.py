from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
from .models import CustomUser
from rest_framework import permissions
from raw.models import RegisteredDevice
from .serializers import UserSerializer, SimpleUserSerializer
from raw.models import RegisteredDevice
from client.models import ForecastLongTerm, ForeastShortTerm


# Create your views here.

class UserAuthToken(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            if not token:
                return Response({'token': created.key, 'error': None})

            return Response({'token': token.key, 'error': None})
        return Response({'error': 'wrong username or password'})


class RegisterUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        full_name = request.data.get('full_name')
        pool_size = request.data.get('pool_size')
        device_id = request.data.get('device_id')

        if RegisteredDevice.objects.filter(device_id=device_id).count() > 0:
            return Response({"error": 'Device with this ID already exists'})
        #is_valid = validate_email(email, verify=True, check_mx=True)
        if CustomUser.objects.filter(email=email).count() > 0:
            return Response({"error": 'A user with this email already exists'})

        user = CustomUser(email=email, full_name=full_name, pool_size=pool_size)
        user.set_password(password)
        user.save()

        new_device = RegisteredDevice(user=user, device_id=device_id)
        new_device.save()

        ###### TODO: ONLY FOR DEMO, NOT FOR PRODUCTION
        for obj in ForecastLongTerm.objects.all():
            obj.user = user
        for obj in ForeastShortTerm.objects.all():
            obj.user = user
        ######


        Token.objects.filter(user=user).delete()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "error": None})



class RegisterForPush(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def post(self, request):
        user = request.user
        user.push_device_id = request.data.get('push_token')
        user.save()
        return Response({'STATUS': 'OK'})


class LogOutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        user = request.user
        print('HELLO')
        if user:
            Token.objects.filter(user=user).delete()
            return Response(status=status.HTTP_200_OK)


class UserDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request):
        if request.user.city:
            data = UserSerializer(request.user, many=False).data
        else:
            data = SimpleUserSerializer(request.user, many=False).data

        device = RegisteredDevice.objects.get(user=request.user)
        data['device'] = device.device_id
        return Response(data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        pool_size = request.data.get('pool_size')
        device_id = request.data.get('device_id')
        name = request.data.get('name')

        user = request.user
        device = RegisteredDevice.objects.get(user=user)
        user.pool_size = pool_size
        user.full_name = name
        device.device_id = device_id
        user.save()
        device.save()
        data = UserSerializer(user, many=False).data
        data['device'] = device.device_id
        return Response(data, status=status.HTTP_200_OK)
