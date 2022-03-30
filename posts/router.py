from rest_framework import routers

from posts.views import PostsViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
