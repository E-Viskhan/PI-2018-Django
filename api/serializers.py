from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


class DualSerializerViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.CharField(source='date_joined')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'created_at']

