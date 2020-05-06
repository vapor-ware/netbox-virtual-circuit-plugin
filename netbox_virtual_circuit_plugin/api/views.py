from rest_framework.viewsets import ModelViewSet
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN
from .serializers import VirtualCircuitSerializer, VirtualCircuitVLANSerializer


class VirtualCircuitViewSet(ModelViewSet):
    queryset = VirtualCircuit.objects.all()
    serializer_class = VirtualCircuitSerializer

class VirtualCircuitVLANViewSet(ModelViewSet):
    queryset = VirtualCircuitVLAN.objects.all()
    serializer_class = VirtualCircuitVLANSerializer
