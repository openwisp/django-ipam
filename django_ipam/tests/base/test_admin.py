from django.contrib.auth.models import User
from django.urls import reverse

from .base import CreateModelsMixin


class BaseTestAdmin(CreateModelsMixin):
    def setUp(self):
        User.objects.create_superuser(username='admin',
                                      password='tester',
                                      email='admin@admin.com')
        self.client.login(username='admin', password='tester')

    def test_ipaddress_invalid_entry(self):
        subnet = self._create_subnet(subnet="10.0.0.0/24", description="Sample Subnet")
        post_data = {
            'ip_address': "12344",
            'subnet': subnet.id,
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
        }
        response = self.client.post(reverse('admin:{0}_ipaddress_add'.format(self.app_name)),
                                    post_data, follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, 'Enter a valid IPv4 or IPv6 address.')

    def test_ipaddress_change(self):
        subnet = self._create_subnet(subnet="10.0.0.0/24", description="Sample Subnet")
        obj = self._create_ipaddress(ip_address="10.0.0.1", subnet=subnet)

        response = self.client.get(reverse('admin:{0}_ipaddress_change'.format(self.app_name), args=[obj.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertEqual(self.ipaddress_model.objects.get(pk=obj.pk).ip_address, '10.0.0.1')

    def test_ipv4_subnet_change(self):
        subnet = self._create_subnet(subnet="10.0.0.0/24", description="Sample Subnet")
        self._create_ipaddress(ip_address="10.0.0.1", subnet=subnet)

        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[subnet.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, '<h3>Subnet Visual Display</h3>')

    def test_ipv6_subnet_change(self):
        subnet = self._create_subnet(subnet="fdb6:21b:a477::9f7/64", description="Sample Subnet")
        self._create_ipaddress(ip_address="fdb6:21b:a477::9f7", subnet=subnet)

        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[subnet.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, '<h3>Used IP address</h3>')

    def test_subnet_invalid_entry(self):

        post_data = {
            'subnet': "12344",
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
        }

        response = self.client.post(reverse('admin:{0}_subnet_add'.format(self.app_name)),
                                    post_data, follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, 'Enter a valid CIDR address.')

    def test_subnet_popup_response(self):
        subnet = self._create_subnet(subnet="fdb6:21b:a477::9f7/64", description="Sample Subnet")
        self._create_ipaddress(ip_address="fdb6:21b:a477::9f7", subnet=subnet)

        response = self.client.get('/admin/django_ipam/subnet/{0}/change/?_popup=1'.format(subnet.id),
                                   follow=True)
        self.assertContains(response, 'ok')

    def test_ipaddress_response(self):
        subnet = self._create_subnet(subnet="10.0.0.0/24", description="Sample Subnet")
        post_data = {
            'ip_address': "10.0.0.1",
            'subnet': subnet.id,
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
        }
        response = self.client.post(reverse('admin:{0}_ipaddress_add'.format(self.app_name)),
                                    post_data, follow=True)
        self.assertContains(response, 'ok')

    def test_ipaddress_popup_response(self):
        subnet = self._create_subnet(subnet="10.0.0.0/24", description="Sample Subnet")
        post_data = {
            'ip_address': "10.0.0.1",
            'subnet': subnet.id,
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
            '_popup': '1',
        }
        response = self.client.post(reverse('admin:{0}_ipaddress_add'.format(self.app_name)),
                                    post_data)
        self.assertContains(response, 'opener.dismissAddAnotherPopup(window);')
