from rest_framework import viewsets
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
