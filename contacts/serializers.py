from rest_framework import serializers

from users.serializers import UserSerializer
from contacts.models import Contact, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# class AddressSerializerPopulated(serializers.ModelSerializer):


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializerPopulated(serializers.ModelSerializer):

    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = '__all__'
