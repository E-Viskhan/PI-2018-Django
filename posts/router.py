from api.router import router
from posts.views import PostsViewSet

router.register(r'posts', PostsViewSet)
