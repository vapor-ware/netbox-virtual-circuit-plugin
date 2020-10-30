from ipam.models import VLAN
from extras.plugins import PluginTemplateExtension

from .models import VirtualCircuit, VirtualCircuitVLAN


class TenantVirtualCircuitCount(PluginTemplateExtension):
    model = 'tenancy.tenant'

    def right_page(self):
        # Map Virtual Circuits' IDs to VLANs' IDs.
        m = {}

        # Filter VLANs by tenant.
        vlans = VLAN.objects.filter(tenant=self.context['object'])
        for v in vlans:
            # If a VLAN is presented, map back to its Virtual Circuit to prevent duplicates.
            if VirtualCircuitVLAN.objects.filter(vlan=v).count() == 1:
                vcvlan = VirtualCircuitVLAN.objects.get(vlan=v)
                m[vcvlan.virtual_circuit.vcid] = vcvlan.vlan.id

        return self.render('netbox_virtual_circuit_plugin/virtual_circuit_tenant.html', extra_context={
            'count': len(m),
        })


template_extensions = [TenantVirtualCircuitCount]
