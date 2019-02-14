from rest_framework import serializers
from pbApi import settings
from user.models import CustomUser
from weather_data.models import City

class UserSerializer(serializers.ModelSerializer):

    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), source='city.name')

    class Meta:
        model = CustomUser
        fields = ('pk', 'full_name', 'email', 'pool_size', 'city')


