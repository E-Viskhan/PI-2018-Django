from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import DualSerializerViewSet
from contacts.models import Contact

from contacts.serializers import ContactSerializer, ContactSerializerPopulated


class ContactViewSet(DualSerializerViewSet):
    queryset = Contact.objects.all()
    default_serializer_class = ContactSerializerPopulated

    serializer_classes = {
        'create': ContactSerializer,
        'update': ContactSerializer
    }
