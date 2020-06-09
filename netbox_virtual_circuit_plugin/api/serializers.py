from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN


class VCVLANSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=VLAN.objects.all(), source='vlan', write_only=True)

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'vlan']
        depth = 1

class VirtualCircuitSerializer(ModelSerializer):
    vlans = VCVLANSerializer(many=True)

    class Meta:
        model = VirtualCircuit
        fields = ['vcid', 'name', 'status', 'context', 'vlans']

    def create(self, validated_data):
        vlans = validated_data.pop('vlans')
        virtual_circuit = VirtualCircuit.objects.create(**validated_data)
        for vlan in vlans:
            VirtualCircuitVLAN.objects.create(virtual_circuit=virtual_circuit, **vlan)
        return virtual_circuit

class VirtualCircuitVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'virtual_circuit', 'vlan']
