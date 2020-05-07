from rest_framework.serializers import ModelSerializer
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN


class VirtualCircuitSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuit
        fields = '__all__'

class VirtualCircuitVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = '__all__'
