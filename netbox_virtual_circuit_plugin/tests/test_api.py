from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import Token

from rest_framework import status
from rest_framework.test import APIClient

from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN
from netbox_virtual_circuit_plugin.choices import VirtualCircuitStatusChoices


class VirtualCircuitsEndpointTestCase(TestCase):
    def setUp(self):
        # Create a superuser and token for API calls.
        self.user = User.objects.create(username='testuser', is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Base URL.
        self.url = '/api/plugins/virtual-circuit/virtual-circuits/'

        # Seed virtual circuits and VLANs.
        self.vc1 = VirtualCircuit.objects.create(vcid=1, name='VC 1')
        self.vc2 = VirtualCircuit.objects.create(vcid=2, name='VC 2')

        self.vlan1 = VLAN.objects.create(vid=1, name='VLAN 1')
        self.vlan2 = VLAN.objects.create(vid=2, name='VLAN 2')
        self.vlan3 = VLAN.objects.create(vid=3, name='VLAN 3')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_get_200(self):
        response = self.client.get(f'{self.url}{self.vc1.vcid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vcid'], self.vc1.vcid)
        self.assertEqual(response.data['name'], self.vc1.name)
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], '')
        self.assertEqual(len(response.data['vlans']), 0)

    def test_get_404(self):
        response = self.client.get(f'{self.url}{100}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_201(self):
        data = {'vcid': 3, 'name': 'foo', 'context': 'bar', 'vlans': []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 3)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 0)

    def test_create_201_single_vlan(self):
        data = {'vcid': 4, 'name': 'foo', 'context': 'bar', 'vlans': [{'vlan': self.vlan1.id}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 4)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 1)
        self.assertEqual(response.data['vlans'][0]['vlan'], self.vlan1.id)

    def test_create_201_multiple_vlans(self):
        data = {'vcid': 5, 'name': 'foo', 'context': 'bar', 'vlans': [{'vlan': self.vlan2.id}, {'vlan': self.vlan3.id}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 5)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 2)
        self.assertEqual(response.data['vlans'][0]['vlan'], self.vlan2.id)
        self.assertEqual(response.data['vlans'][1]['vlan'], self.vlan3.id)

    def test_create_xxx_no_vlan(self):
        pass

    def test_create_xxx_non_unique_vlan(self):
        pass

    def test_create_xxx_non_unique_vc(self):
        pass

    def test_create_400_missing_params(self):
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('vcid', response.data)
        self.assertIn('name', response.data)
        self.assertIn('vlans', response.data)
        self.assertEqual(len(response.data), 3)
