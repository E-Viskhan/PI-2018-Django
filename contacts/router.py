from rest_framework import routers

from contacts.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
