from rest_framework.serializers import ModelSerializer, SerializerMethodField
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VirtualCircuitVLAN


class VLANSerializer(ModelSerializer):
    id = SerializerMethodField('get_id')
    vid = SerializerMethodField('get_vid')

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'vid']

    def get_id(self, obj):
        return obj.vlan.id

    def get_vid(self, obj):
        return obj.vlan.vid

class VirtualCircuitSerializer(ModelSerializer):
    vlans = VLANSerializer(many=True, read_only=True)

    class Meta:
        model = VirtualCircuit
        fields = ['vcid', 'name', 'status', 'context', 'vlans']

class VirtualCircuitVLANSerializer(ModelSerializer):

    class Meta:
        model = VirtualCircuitVLAN
        fields = ['id', 'virtual_circuit', 'vlan']
