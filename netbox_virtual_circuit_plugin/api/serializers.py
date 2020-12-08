from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, ValidationError
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN


class NestedVCVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'vlan']

class VirtualCircuitSerializer(ModelSerializer):
    vlans = NestedVCVLANSerializer(many=True)

    class Meta:
        model = VirtualCircuit
        fields = ['vcid', 'name', 'status', 'context', 'description', 'vlans', 'created', 'last_updated']

    def create(self, validated_data):
        vlans_data = validated_data.pop('vlans')
        virtual_circuit = VirtualCircuit.objects.create(**validated_data)
        for vlan in vlans_data:
            VirtualCircuitVLAN.objects.create(virtual_circuit=virtual_circuit, **vlan)
        return virtual_circuit

class VirtualCircuitVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'virtual_circuit', 'vlan']
