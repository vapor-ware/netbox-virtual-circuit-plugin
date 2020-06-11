from django import forms

from utilities.forms import BootstrapMixin

from .models import VirtualCircuit

class VirtualCircuitForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new Virtual Circuit."""

    class Meta:
        model = VirtualCircuit
        fields = [
            'vcid',
            'name',
            'status',
            'context',
        ]
        help_texts = {
            'vid': 'Configured Virtual Circuit ID',
            'name': 'Configured Virtual Circuit name',
            'status': 'Operational status of this Virtual Circuit',
            'context': 'Context of this Virtual Circuit',
        }
