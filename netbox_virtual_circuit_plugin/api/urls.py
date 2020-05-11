from rest_framework import routers
from .views import VirtualCircuitViewSet, VirtualCircuitVLANViewSet


router = routers.DefaultRouter()
router.register('virtual-circuits', VirtualCircuitViewSet, 'vcid')
router.register('vlans', VirtualCircuitVLANViewSet)
urlpatterns = router.urls
