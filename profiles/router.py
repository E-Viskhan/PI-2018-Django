from api.router import router
from profiles.views import ProfilesViewSet, ProfileStatusViewSet

router.register(r'profile', ProfilesViewSet)
router.register(r'profile/status', ProfileStatusViewSet)
