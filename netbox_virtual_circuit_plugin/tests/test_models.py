from django.core.exceptions import ValidationError
from django.test import TestCase

from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN
from netbox_virtual_circuit_plugin.choices import VirtualCircuitStatusChoices


class VirtualCircuitTestCase(TestCase):
    def setUp(self):
        # Seed data.
        self.vc1 = VirtualCircuit.objects.create(vcid=1, name='VC 1')

        self.vlan1 = VLAN.objects.create(vid=1, name='VLAN 1')
        self.vlan2 = VLAN.objects.create(vid=2, name='VLAN 2')

        self.vc1_vlan1 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan1)

    def test_invalid_vcid(self):
        negative = VirtualCircuit(vcid=-1, name='VC -1')
        self.assertRaises(ValidationError, negative.full_clean)

        zero = VirtualCircuit(vcid=0, name='VC 0')
        self.assertRaises(ValidationError, zero.full_clean)

        out_of_range = VirtualCircuit(vcid=4294967296, name='VC 4294967296')
        self.assertRaises(ValidationError, out_of_range.full_clean)

    def test_duplicate_vlan(self):
        duplicate = VirtualCircuitVLAN(virtual_circuit=self.vc1, vlan=self.vlan1)
        self.assertRaises(ValidationError, duplicate.full_clean)

    def test_create_virtual_circuit(self):
        vc1_vlan2 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan2)
        self.assertEqual(vc1_vlan2.virtual_circuit, self.vc1)
        self.assertEqual(vc1_vlan2.vlan, self.vlan2)
