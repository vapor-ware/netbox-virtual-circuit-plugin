from rest_framework import routers
from .views import VirtualCircuitViewSet, VirtualCircuitVLANViewSet


router = routers.DefaultRouter()
router.register(r'virtual-circuits', VirtualCircuitViewSet, 'vcid')
router.register(r'vlans', VirtualCircuitVLANViewSet)
urlpatterns = router.urls
