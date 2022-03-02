from rest_framework import serializers
from users.models import CustomUser, Photos


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(source='date_joined')
    name = serializers.CharField(source='first_name')
    photos = PhotosSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'status', 'photos', 'first_name', 'last_name', 'created_at']

