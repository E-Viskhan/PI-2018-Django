from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.CharField(source='date_joined')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'created_at']

