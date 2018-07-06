import json

from django.urls import reverse

from .base import CreateModelsMixin


class BaseTestApi(CreateModelsMixin):
    def test_ipv4_get_avaialble_api(self):
        subnet = self._create_subnet(dict(subnet="10.0.0.0/24"))
        self._create_ipaddress(dict(ip_address="10.0.0.1", subnet=subnet))
        response = self.client.get(reverse('ipam:get_first_available_ip', args=(subnet.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '10.0.0.2')

    def test_ipv6_get_avaialble_api(self):
        subnet = self._create_subnet(dict(subnet="fdb6:21b:a477::9f7/64"))
        self._create_ipaddress(dict(ip_address="fdb6:21b:a477::1", subnet=subnet))
        response = self.client.get(reverse('ipam:get_first_available_ip', args=(subnet.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'fdb6:21b:a477::2')

    def test_unavailable_ip(self):
        subnet = self._create_subnet(dict(subnet="10.0.0.0/32", description="Sample Subnet"))
        response = self.client.get(reverse('ipam:get_first_available_ip', args=(subnet.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, None)

    def test_ipv4_request_api(self):
        subnet = self._create_subnet(dict(subnet="10.0.0.0/24"))
        self._create_ipaddress(dict(ip_address="10.0.0.1", subnet=subnet))
        data = {
            'subnet': str(subnet.id),
            'description': 'Test ip address'
        }
        response = self.client.post(reverse('ipam:request_ip', args=(subnet.id,)),
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["ip_address"], '10.0.0.2')

    def test_ipv6_request_api(self):
        subnet = self._create_subnet(dict(subnet="fdb6:21b:a477::9f7/64"))
        self._create_ipaddress(dict(ip_address="fdb6:21b:a477::1", subnet=subnet))
        data = {
            'subnet': str(subnet.id),
            'description': 'Test ip address',
        }
        response = self.client.post(reverse('ipam:request_ip', args=(subnet.id,)),
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["ip_address"], 'fdb6:21b:a477::2')

    def test_unvailable_request_api(self):
        subnet = self._create_subnet(dict(subnet="10.0.0.0/32"))
        data = {
            'subnet': str(subnet.id),
            'description': 'Test ip address'
        }
        response = self.client.post(reverse('ipam:request_ip', args=(subnet.id,)),
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, None)
