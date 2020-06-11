from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from utilities.views import ObjectEditView, ObjectListView

from .forms import VirtualCircuitForm, VirtualCircuitVLANForm
from .models import VirtualCircuit, VirtualCircuitVLAN, VLAN
from .tables import VirtualCircuitTable


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

class VirtualCircuitListView(ObjectListView):
    permission_required = 'netbox_virtual_circuit_plugin.view_virtualcircuit'
    queryset = VirtualCircuit.objects.all()
    # filterset = VirtualCircuitFilter
    # filterset_form = VirtualCircuitFilterForm
    table = VirtualCircuitTable
    template_name = 'netbox_virtual_circuit_plugin/virtual_circuit_list.html'

class VirtualCircuitCreateView(ObjectEditView):
    permission_required = 'netbox_virtual_circuit_plugin.add_virtualcircuit'
    model = VirtualCircuit
    queryset = VirtualCircuit.objects.all()
    model_form =  VirtualCircuitForm
    template_name = 'netbox_virtual_circuit_plugin/virtual_circuit_edit.html'
    default_return_url = 'plugins:netbox_virtual_circuit_plugin:virtual_circuit_list'

class VirtualCircuitVLANCreateView(ObjectEditView):
    permission_required = 'netbox_virtual_circuit_plugin.add_virtualcircuitvlan'
    model = VirtualCircuitVLAN
    queryset = VirtualCircuitVLAN.objects.all()
    model_form =  VirtualCircuitVLANForm
    template_name = 'netbox_virtual_circuit_plugin/virtual_circuit_vlan_edit.html'
    default_return_url = 'plugins:netbox_virtual_circuit_plugin:virtual_circuit_list'
