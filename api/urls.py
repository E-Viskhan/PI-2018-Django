from django.contrib import admin
from django.urls import path, include

from .router import router as users_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(users_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
