from rest_framework import routers

from profiles.views import ProfilesViewSet, ProfileStatusViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfilesViewSet)
router.register(r'profile/status', ProfileStatusViewSet)
