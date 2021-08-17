from rest_framework.viewsets import ModelViewSet
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN
from .serializers import VirtualCircuitSerializer, VirtualCircuitVLANSerializer
from netbox_virtual_circuit_plugin.filters import VirtualCircuitFilter


class VirtualCircuitViewSet(ModelViewSet):
    serializer_class = VirtualCircuitSerializer
    queryset = VirtualCircuit.objects.all()
    filterset_class = VirtualCircuitFilter


class VirtualCircuitVLANViewSet(ModelViewSet):
    queryset = VirtualCircuitVLAN.objects.all()
    serializer_class = VirtualCircuitVLANSerializer
