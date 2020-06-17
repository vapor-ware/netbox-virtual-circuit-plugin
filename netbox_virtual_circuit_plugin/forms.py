from django import forms

from utilities.forms import BootstrapMixin

from .models import VirtualCircuit, VirtualCircuitVLAN, VirtualCircuitStatusChoices

BLANK_CHOICE = (("", "---------"),)


class VirtualCircuitForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = VirtualCircuit
        fields = [
            'vcid',
            'name',
            'status',
            'context',
        ]

class VirtualCircuitFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )
    status = forms.ChoiceField(
        choices=BLANK_CHOICE + VirtualCircuitStatusChoices.CHOICES,
        required=False
    )

    class Meta:
        model = VirtualCircuit
        fields = [
            'q',
            'status',
            'context',
        ]

class VirtualCircuitVLANForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = VirtualCircuitVLAN
        fields = [
            'virtual_circuit',
            'vlan',
        ]
