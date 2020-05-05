from rest_framework import routers
from .views import VirtualCircuitViewSet

router = routers.DefaultRouter()
router.register('virtual-circuits', VirtualCircuitViewSet)
urlpatterns = router.urls
