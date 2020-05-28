from rest_framework.serializers import ModelSerializer, SerializerMethodField
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN


class VLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['vlan']

class VirtualCircuitSerializer(ModelSerializer):
    vlans = VLANSerializer(many=True)

    class Meta:
        model = VirtualCircuit
        fields = ['vcid', 'name', 'status', 'context', 'vlans']

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
