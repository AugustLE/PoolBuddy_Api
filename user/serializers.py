from rest_framework import serializers
from pbApi import settings
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('pk', 'image', 'full_name', 'email')


