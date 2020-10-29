from ipam.models import VLAN
from extras.plugins import PluginTemplateExtension

from .models import VirtualCircuit, VirtualCircuitVLAN


class TenantVirtualCircuitCount(PluginTemplateExtension):
    model = 'tenancy.tenant'

    def right_page(self):
        m = {}
        vlans = VLAN.objects.filter(tenant=self.context['object'])
        for v in vlans:
            if VirtualCircuitVLAN.objects.filter(vlan=v).count() == 1:
                vcvlan = VirtualCircuitVLAN.objects.get(vlan=v)
                m[vcvlan.virtual_circuit.vcid] = vcvlan.vlan.id

        return self.render('netbox_virtual_circuit_plugin/virtual_circuit_tenant.html', extra_context={
            'count': len(m),
            'vlan_count': vlans.count(),
        })


template_extensions = [TenantVirtualCircuitCount]
