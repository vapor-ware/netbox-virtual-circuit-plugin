from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, ValidationError
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
            try:
              ret = VirtualCircuitVLAN.objects.get(vlan=vlan.get('vlan'))
              if ret:
                  raise ValidationError({'id': f'VLAN {ret.vlan} is already assigned to Virtual Circuit {ret.virtual_circuit}'})
            except VirtualCircuitVLAN.DoesNotExist:
                pass

            VirtualCircuitVLAN.objects.create(virtual_circuit=virtual_circuit, **vlan)
        return virtual_circuit

class VirtualCircuitVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'virtual_circuit', 'vlan']
