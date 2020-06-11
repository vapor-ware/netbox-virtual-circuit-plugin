from django import forms

from utilities.forms import BootstrapMixin

from .models import VirtualCircuit, VirtualCircuitVLAN

class VirtualCircuitForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = VirtualCircuit
        fields = [
            'vcid',
            'name',
            'status',
            'context',
        ]
        help_texts = {
            'vcid': 'Configured Virtual Circuit ID',
            'name': 'Configured Virtual Circuit name',
            'status': 'Operational status of this Virtual Circuit',
            'context': 'Context of this Virtual Circuit',
        }

class VirtualCircuitVLANForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = VirtualCircuitVLAN
        labels = {
            'virtual_circuit': 'Virtual Circuit',
            'vlan': 'VLAN',
        }
        fields = [
            'virtual_circuit',
            'vlan',
        ]
        help_texts = {
            'virtual_circuit': 'Any Virtual Circuit',
            'vlan': 'Any unassigned VLAN',
        }
