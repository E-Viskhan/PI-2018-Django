from api.router import router
from follows.views import FollowViewSet

router.register(r'follows', FollowViewSet)
