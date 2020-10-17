from rest_framework import serializers 
from users.serializers import UserSerializer
from .models import Room



class ReadRoomSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Room 
        exclude = ()


class WriteRoomSerializer(serializers.ModelSerializer):


    class Meta:
        model = Room 
        exclude = ()

