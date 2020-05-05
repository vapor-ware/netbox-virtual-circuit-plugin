from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import VirtualCircuit


class ListVirtualCircuitsView(View):
    """
    List all virtual circuits.
    """
    def get(self, request):
        vcs = VirtualCircuit.objects.all()
        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit_list.html', {
            'virtual_circuits': vcs,
        })

class VirtualCircuitView(View):
    """
    Single virtual circuits view, identified by ID.
    """
    def get(self, request, vcid):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=vcid))
        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
        })
