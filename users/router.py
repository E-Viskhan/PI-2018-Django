from api.router import router
from users.views import UserViewSet

router.register(r'users', UserViewSet)
