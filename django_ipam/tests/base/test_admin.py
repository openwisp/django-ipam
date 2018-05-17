from ipaddress import ip_network

from django.contrib.auth.models import User
from django.urls import reverse


class BaseTestAdmin(object):
    def setUp(self):
        self._superuser_login()

    def _superuser_login(self):
        user = User.objects.create_superuser(username="admin",
                                             password="admin",
                                             email="test@test.org")

        self.client.login(user)

    def test_subnet_change(self):
        obj = self.subnet_model(subnet="10.0.0.0/24", description="Sample Subnet")
        obj.full_clean()
        obj.save()
        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[obj.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertEqual(self.subnet_model.objects.get(pk=obj.pk).subnet, ip_network('10.0.0.0/24'))

    def test_ipaddress_change(self):
        subnet = self.subnet_model(subnet="10.0.0.0/24", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        obj = self.ipaddress_model(ip_address="10.0.0.1", subnet=subnet)
        obj.full_clean()
        obj.save()
        response = self.client.get(reverse('admin:{0}_ipaddress_change'.format(self.app_name), args=[obj.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
