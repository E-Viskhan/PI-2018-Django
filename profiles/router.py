from rest_framework import routers

from profiles.views import ProfilesViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfilesViewSet)
