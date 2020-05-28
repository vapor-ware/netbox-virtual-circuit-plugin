from django.test import TestCase
from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN
from netbox_virtual_circuit_plugin.choices import VirtualCircuitStatusChoices


class VirtualCircuitTestCase(TestCase):
    def setUp(self):
        """Initialize several virtual circuits and VLANs."""
        VirtualCircuit.objects.bulk_create((
            VirtualCircuit(vcid=1, name='VC 1'),
            VirtualCircuit(vcid=2, name='VC 2', status=VirtualCircuitStatusChoices.STATUS_CONFIGURED),
            VirtualCircuit(vcid=3, name='VC 3', context='foo'),
        ))

        VLAN.objects.bulk_create((
            VLAN(vid=1, name='VLAN 1'),
            VLAN(vid=2, name='VLAN 2'),
            VLAN(vid=3, name='VLAN 3'),
        ))

    def test_virtual_circuits_metadata(self):
        """Verify virtual circuits' metadata are correctly setup."""
        vc1 = VirtualCircuit.objects.get(vcid=1)
        self.assertEqual(vc1.name, 'VC 1')
        self.assertEqual(vc1.status, VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(vc1.context, '')

        vc2 = VirtualCircuit.objects.get(vcid=2)
        self.assertEqual(vc2.vcid, 2)
        self.assertEqual(vc2.name, 'VC 2')
        self.assertEqual(vc2.status, VirtualCircuitStatusChoices.STATUS_CONFIGURED)
        self.assertEqual(vc2.context, '')

        vc3 = VirtualCircuit.objects.get(vcid=3)
        self.assertEqual(vc3.vcid, 3)
        self.assertEqual(vc3.name, 'VC 3')
        self.assertEqual(vc3.status, VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(vc3.context, 'foo')
