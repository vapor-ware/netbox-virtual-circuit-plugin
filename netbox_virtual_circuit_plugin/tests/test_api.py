from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import Token

from rest_framework import status
from rest_framework.test import APIClient

from netbox_virtual_circuit_plugin.models import VirtualCircuit, VLAN, VirtualCircuitVLAN
from netbox_virtual_circuit_plugin.choices import VirtualCircuitStatusChoices


class VirtualCircuitEndpointTestCase(TestCase):
    def setUp(self):
        # Create a superuser and token for API calls.
        self.user = User.objects.create(username='testuser', is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Base URL.
        self.url = '/api/plugins/virtual-circuit/virtual-circuits/'

        # Seed data.
        self.vc1 = VirtualCircuit.objects.create(vcid=1, name='VC 1')
        self.vc2 = VirtualCircuit.objects.create(vcid=2, name='VC 2')

        self.vlan1 = VLAN.objects.create(vid=1, name='VLAN 1')
        self.vlan2 = VLAN.objects.create(vid=2, name='VLAN 2')
        self.vlan3 = VLAN.objects.create(vid=3, name='VLAN 3')
        self.vlan4 = VLAN.objects.create(vid=4, name='VLAN 4')
        self.vlan5 = VLAN.objects.create(vid=5, name='VLAN 5')

        self.vc1_vlan1 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan1)
        self.vc1_vlan2 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan2)

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)

        vc1 = response.data['results'][0]
        self.assertEqual(vc1['vcid'], self.vc1.vcid)
        self.assertEqual(vc1['name'], self.vc1.name)
        self.assertEqual(vc1['status'], self.vc1.status)
        self.assertEqual(vc1['context'], self.vc1.context)
        self.assertEqual(len(vc1['vlans']), 2)

        vlan1 = vc1['vlans'][0]['vlan']
        self.assertEqual(vlan1['id'], self.vlan1.id)
        self.assertEqual(vlan1['vid'], self.vlan1.vid)
        self.assertEqual(vlan1['name'], self.vlan1.name)
        self.assertEqual(vlan1['status'], self.vlan1.status)

        vlan2 = vc1['vlans'][1]['vlan']
        self.assertEqual(vlan2['id'], self.vlan2.id)
        self.assertEqual(vlan2['vid'], self.vlan2.vid)
        self.assertEqual(vlan2['name'], self.vlan2.name)
        self.assertEqual(vlan2['status'], self.vlan2.status)

        vc2 = response.data['results'][1]
        self.assertEqual(vc2['vcid'], self.vc2.vcid)
        self.assertEqual(vc2['name'], self.vc2.name)
        self.assertEqual(vc2['status'], self.vc2.status)
        self.assertEqual(vc2['context'], self.vc2.context)
        self.assertEqual(len(vc2['vlans']), 0)

    def test_get_200(self):
        response = self.client.get(f'{self.url}{self.vc1.vcid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vcid'], self.vc1.vcid)
        self.assertEqual(response.data['name'], self.vc1.name)
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], '')
        self.assertEqual(len(response.data['vlans']), 2)

        vlan1 = response.data['vlans'][0]['vlan']
        self.assertEqual(vlan1['id'], self.vlan1.id)
        self.assertEqual(vlan1['vid'], self.vlan1.vid)
        self.assertEqual(vlan1['name'], self.vlan1.name)
        self.assertEqual(vlan1['status'], self.vlan1.status)

        vlan2 = response.data['vlans'][1]['vlan']
        self.assertEqual(vlan2['id'], self.vlan2.id)
        self.assertEqual(vlan2['vid'], self.vlan2.vid)
        self.assertEqual(vlan2['name'], self.vlan2.name)
        self.assertEqual(vlan2['status'], self.vlan2.status)

    def test_get_404(self):
        response = self.client.get(f'{self.url}{100}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_400_missing_params(self):
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 3)
        self.assertIn('vcid', response.data)
        self.assertIn('name', response.data)
        self.assertIn('vlans', response.data)

    def test_create_400_existed_vc(self):
        data = {'vcid': 1, 'name': 'foo', 'context': 'bar', 'vlans': []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_201_no_vlan(self):
        data = {'vcid': 3, 'name': 'foo', 'context': 'bar', 'vlans': []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 3)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 0)

    def test_create_201_single_vlan(self):
        data = {'vcid': 4, 'name': 'foo', 'context': 'bar', 'vlans': [{'id': self.vlan3.id}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 4)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 1)

        vlan3 = response.data['vlans'][0]['vlan']
        self.assertEqual(vlan3['id'], self.vlan3.id)
        self.assertEqual(vlan3['vid'], self.vlan3.vid)
        self.assertEqual(vlan3['name'], self.vlan3.name)
        self.assertEqual(vlan3['status'], self.vlan3.status)

    def test_create_201_multiple_vlans(self):
        data = {'vcid': 5, 'name': 'foo', 'context': 'bar', 'vlans': [{'id': self.vlan4.id}, {'id': self.vlan5.id}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vcid'], 5)
        self.assertEqual(response.data['name'], 'foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], 'bar')
        self.assertEqual(len(response.data['vlans']), 2)

        vlan4 = response.data['vlans'][0]['vlan']
        self.assertEqual(vlan4['id'], self.vlan4.id)
        self.assertEqual(vlan4['vid'], self.vlan4.vid)
        self.assertEqual(vlan4['name'], self.vlan4.name)
        self.assertEqual(vlan4['status'], self.vlan4.status)

        vlan5 = response.data['vlans'][1]['vlan']
        self.assertEqual(vlan5['id'], self.vlan5.id)
        self.assertEqual(vlan5['vid'], self.vlan5.vid)
        self.assertEqual(vlan5['name'], self.vlan5.name)
        self.assertEqual(vlan5['status'], self.vlan5.status)

    def test_create_400_existed_vlan(self):
        data = {'vcid': 6, 'name': 'foo', 'context': 'bar', 'vlans': [{'id': self.vlan1.id}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_400_non_existent_vlan(self):
        data = {'vcid': 7, 'name': 'foo', 'context': 'bar', 'vlans': [{'id': 400}]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_200_name(self):
        data = {'name': 'patched-foo'}
        response = self.client.patch(f'{self.url}{self.vc1.vcid}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vcid'], 1)
        self.assertEqual(response.data['name'], 'patched-foo')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION)
        self.assertEqual(response.data['context'], '')
        self.assertEqual(len(response.data['vlans']), 2)

        vlan1 = response.data['vlans'][0]['vlan']
        self.assertEqual(vlan1['id'], self.vlan1.id)
        self.assertEqual(vlan1['vid'], self.vlan1.vid)
        self.assertEqual(vlan1['name'], self.vlan1.name)
        self.assertEqual(vlan1['status'], self.vlan1.status)

        vlan2 = response.data['vlans'][1]['vlan']
        self.assertEqual(vlan2['id'], self.vlan2.id)
        self.assertEqual(vlan2['vid'], self.vlan2.vid)
        self.assertEqual(vlan2['name'], self.vlan2.name)
        self.assertEqual(vlan2['status'], self.vlan2.status)

    def test_patch_200_status(self):
        data = {'status': VirtualCircuitStatusChoices.STATUS_CONFIGURED}
        response = self.client.patch(f'{self.url}{self.vc1.vcid}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vcid'], 1)
        self.assertEqual(response.data['name'], 'VC 1')
        self.assertEqual(response.data['status'], VirtualCircuitStatusChoices.STATUS_CONFIGURED)
        self.assertEqual(response.data['context'], '')
        self.assertEqual(len(response.data['vlans']), 2)

        vlan1 = response.data['vlans'][0]['vlan']
        self.assertEqual(vlan1['id'], self.vlan1.id)
        self.assertEqual(vlan1['vid'], self.vlan1.vid)
        self.assertEqual(vlan1['name'], self.vlan1.name)
        self.assertEqual(vlan1['status'], self.vlan1.status)

        vlan2 = response.data['vlans'][1]['vlan']
        self.assertEqual(vlan2['id'], self.vlan2.id)
        self.assertEqual(vlan2['vid'], self.vlan2.vid)
        self.assertEqual(vlan2['name'], self.vlan2.name)
        self.assertEqual(vlan2['status'], self.vlan2.status)

    def test_patch_400_invalid_status(self):
        data = {'status': 'invalid'}
        response = self.client.patch(f'{self.url}{self.vc1.vcid}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_204(self):
        response = self.client.delete(f'{self.url}{self.vc1.vcid}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_404(self):
        response = self.client.delete(f'{self.url}{100}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class VCVLANEndpointTestCase(TestCase):
    def setUp(self):
        # Create a superuser and token for API calls.
        self.user = User.objects.create(username='testuser', is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Base URL.
        self.url = '/api/plugins/virtual-circuit/vlans/'

        # Seed data.
        self.vc1 = VirtualCircuit.objects.create(vcid=1, name='VC 1')
        self.vc2 = VirtualCircuit.objects.create(vcid=2, name='VC 2')

        self.vlan1 = VLAN.objects.create(vid=1, name='VLAN 1')
        self.vlan2 = VLAN.objects.create(vid=2, name='VLAN 2')
        self.vlan3 = VLAN.objects.create(vid=3, name='VLAN 3')

        self.vc1_vlan1 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc1, vlan=self.vlan1)
        self.vc2_vlan2 = VirtualCircuitVLAN.objects.create(virtual_circuit=self.vc2, vlan=self.vlan2)

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

        vc1_vlan1 = response.data['results'][0]
        self.assertEqual(vc1_vlan1['id'], self.vc1_vlan1.id)
        self.assertEqual(vc1_vlan1['virtual_circuit'], self.vc1_vlan1.virtual_circuit.vcid)
        self.assertEqual(vc1_vlan1['vlan'], self.vc1_vlan1.vlan.id)

        vc2_vlan2 = response.data['results'][1]
        self.assertEqual(vc2_vlan2['id'], self.vc2_vlan2.id)
        self.assertEqual(vc2_vlan2['virtual_circuit'], self.vc2_vlan2.virtual_circuit.vcid)
        self.assertEqual(vc2_vlan2['vlan'], self.vc2_vlan2.vlan.id)

    def test_get_200(self):
        response = self.client.get(f'{self.url}{self.vc1_vlan1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['virtual_circuit'], self.vc1.vcid)
        self.assertEqual(response.data['vlan'], self.vlan1.id)

    def test_get_404(self):
        response = self.client.get(f'{self.url}{100}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_201(self):
        data = {'virtual_circuit': self.vc2.vcid, 'vlan': self.vlan3.id}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['virtual_circuit'], self.vc2.vcid)
        self.assertEqual(response.data['vlan'], self.vlan3.id)

    def test_create_400_missing_params(self):
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 2)
        self.assertIn('virtual_circuit', response.data)
        self.assertIn('vlan', response.data)

    def test_create_400_existed_vlan(self):
        data = {'virtual_circuit': self.vc1.vcid, 'vlan': self.vlan1.id}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_200(self):
        data = {'vlan': self.vlan3.id}
        response = self.client.patch(f'{self.url}{self.vc1_vlan1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['virtual_circuit'], self.vc1.vcid)
        self.assertEqual(response.data['vlan'], self.vlan3.id)

    def test_patch_400_existed_vlan(self):
        data = {'vlan': self.vlan2.id}
        response = self.client.patch(f'{self.url}{self.vc1_vlan1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_204(self):
        response = self.client.delete(f'{self.url}{self.vc1_vlan1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_404(self):
        response = self.client.delete(f'{self.url}{100}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
