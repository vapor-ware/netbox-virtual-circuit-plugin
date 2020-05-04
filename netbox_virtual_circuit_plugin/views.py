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
