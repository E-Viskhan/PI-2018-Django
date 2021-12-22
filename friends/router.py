from rest_framework import routers

from friends.views import FriendViewSet

router = routers.DefaultRouter()
router.register(r'friends', FriendViewSet)
