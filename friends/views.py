from rest_framework import viewsets
from friends.models import Friend

from friends.serializers import FriendSerializer


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
