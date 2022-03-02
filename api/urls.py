from django.contrib import admin
from django.urls import path, include

from .router import router as users_router
from contacts.router import router as contacts_router
from friends.router import router as friends_router
from users.router import router as users_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(users_router.urls)),
    path('', include(contacts_router.urls)),
    path('', include(friends_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
