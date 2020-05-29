from django.core.exceptions import ValidationError
from django.test import TestCase

from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN
from netbox_virtual_circuit_plugin.choices import VirtualCircuitStatusChoices


class VirtualCircuitTestCase(TestCase):
    def setUp(self):
        # Virtual Circuits.
        self.vc1 = VirtualCircuit.objects.create(vcid=1, name='VC 1')
        self.vc2 = VirtualCircuit.objects.create(vcid=2, name='VC 2', status=VirtualCircuitStatusChoices.STATUS_CONFIGURED)
        self.vc3 = VirtualCircuit.objects.create(vcid=3, name='VC 3', context='foo')

        # VLANs.
        self.vlan1 = VLAN.objects.create(vid=1, name='VLAN 1')
        self.vlan2 = VLAN.objects.create(vid=2, name='VLAN 2')
        self.vlan3 = VLAN.objects.create(vid=3, name='VLAN 3')

        # Virtual Circuit to VLAN connections.
        self.vc1_vlan1 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan1)
        self.vc1_vlan2 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan2)
        self.vc2_vlan3 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc2, vlan=self.vlan3)

    def test_get_virtual_circuits(self):
        self.assertEqual(self.vc1.vcid, 1)
        self.assertEqual(self.vc1.name, 'VC 1')
        self.assertEqual(self.vc1.status, VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(self.vc1.context, '')

        self.assertEqual(self.vc2.vcid, 2)
        self.assertEqual(self.vc2.name, 'VC 2')
        self.assertEqual(self.vc2.status, VirtualCircuitStatusChoices.STATUS_CONFIGURED)
        self.assertEqual(self.vc2.context, '')

        self.assertEqual(self.vc3.vcid, 3)
        self.assertEqual(self.vc3.name, 'VC 3')
        self.assertEqual(self.vc3.status, VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(self.vc3.context, 'foo')

    def test_get_vlans(self):
        self.assertEqual(self.vlan1.vid, 1)
        self.assertEqual(self.vlan1.name, 'VLAN 1')

        self.assertEqual(self.vlan2.vid, 2)
        self.assertEqual(self.vlan2.name, 'VLAN 2')

        self.assertEqual(self.vlan3.vid, 3)
        self.assertEqual(self.vlan3.name, 'VLAN 3')

    def test_get_virtual_circuits_vlans(self):
        self.assertEqual(self.vc1_vlan1.virtual_circuit, self.vc1)
        self.assertEqual(self.vc1_vlan1.vlan, self.vlan1)

        self.assertEqual(self.vc1_vlan2.virtual_circuit, self.vc1)
        self.assertEqual(self.vc1_vlan2.vlan, self.vlan2)

        self.assertEqual(self.vc2_vlan3.virtual_circuit, self.vc2)
        self.assertEqual(self.vc2_vlan3.vlan, self.vlan3)

    def test_duplicate_virtual_circuits_vlans(self):
        duplicate1 = VirtualCircuitVLAN(virtual_circuit=self.vc1, vlan=self.vlan1)
        duplicate2 = VirtualCircuitVLAN(virtual_circuit=self.vc1, vlan=self.vlan2)
        duplicate3 = VirtualCircuitVLAN(virtual_circuit=self.vc2, vlan=self.vlan3)

        self.assertRaises(ValidationError, duplicate1.full_clean)
        self.assertRaises(ValidationError, duplicate2.full_clean)
        self.assertRaises(ValidationError, duplicate3.full_clean)
