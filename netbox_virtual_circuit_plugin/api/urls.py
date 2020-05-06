from rest_framework import routers
from .views import VirtualCircuitViewSet, VCVLANViewSet

router = routers.DefaultRouter()
router.register('virtual-circuits', VirtualCircuitViewSet)
router.register('vlans', VCVLANViewSet)
urlpatterns = router.urls
