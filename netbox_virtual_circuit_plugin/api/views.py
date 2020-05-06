from rest_framework.viewsets import ModelViewSet
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VCVLAN
from .serializers import VirtualCircuitSerializer, VCVLANSerializer

class VirtualCircuitViewSet(ModelViewSet):
    queryset = VirtualCircuit.objects.all()
    serializer_class = VirtualCircuitSerializer

class VCVLANViewSet(ModelViewSet):
    queryset = VCVLAN.objects.all()
    serializer_class = VCVLANSerializer
