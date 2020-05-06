from rest_framework.serializers import ModelSerializer
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VCVLAN

class VirtualCircuitSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuit
        fields = '__all__'

class VCVLANSerializer(ModelSerializer):

    class Meta:
        model = VCVLAN
        fields = '__all__'
