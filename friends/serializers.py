from rest_framework import serializers

from contacts.serializers import ContactSerializer, ContactSerializerPopulated
from friends.models import Friend


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'


class FriendSerializerPopulated(serializers.ModelSerializer):

    first_contact = ContactSerializer()
    second_contact = ContactSerializer()

    class Meta:
        model = Friend
        fields = '__all__'


class FriendSerializerPopulatedContactPopulated(serializers.ModelSerializer):

    first_contact = ContactSerializerPopulated()
    second_contact = ContactSerializerPopulated()

    foo = serializers.SerializerMethodField()

    def get_foo(self, obj):
        return f"Foo id: {obj.pk}"

    class Meta:
        model = Friend
        fields = '__all__'
