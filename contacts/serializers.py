from rest_framework import serializers

from api.serializers import UserSerializer
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializerPopulated(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Contact
        fields = '__all__'

