from rest_framework.viewsets import ModelViewSet
from netbox_virtual_circuit_plugin.models import VirtualCircuit
from .serializers import VirtualCircuitSerializer

class VirtualCircuitViewSet(ModelViewSet):
    queryset = VirtualCircuit.objects.all()
    serializer_class = VirtualCircuitSerializer
