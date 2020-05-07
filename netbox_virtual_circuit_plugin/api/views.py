from rest_framework.viewsets import ModelViewSet
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN
from .serializers import VirtualCircuitSerializer, VirtualCircuitVLANSerializer


class VirtualCircuitViewSet(ModelViewSet):
    serializer_class = VirtualCircuitSerializer

    def get_queryset(self):
        context = self.request.query_params.get('context', None)
        if context is None:
            queryset = VirtualCircuit.objects.all().order_by('vcid')
        else:
            queryset = VirtualCircuit.objects.filter(context=context)
        return queryset

class VirtualCircuitVLANViewSet(ModelViewSet):
    queryset = VirtualCircuitVLAN.objects.all()
    serializer_class = VirtualCircuitVLANSerializer
