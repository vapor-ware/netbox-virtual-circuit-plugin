from rest_framework.serializers import ModelSerializer
from netbox_virtual_circuit_plugin.models import VirtualCircuit

class VirtualCircuitSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuit
        fields = '__all__'
