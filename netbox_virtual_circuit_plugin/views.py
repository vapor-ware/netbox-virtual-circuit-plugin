from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import View
from .models import VirtualCircuit, VirtualCircuitVLAN, VLAN


class ListVirtualCircuitsView(View):
    """List all virtual circuits."""

    def get(self, request):
        vcs = VirtualCircuit.objects.all()
        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit_list.html', {
            'virtual_circuits': vcs,
        })

class VirtualCircuitView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, vcid):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=vcid))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })
