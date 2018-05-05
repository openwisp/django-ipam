import os
from unittest import skipUnless

import swapper
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

IPAddress = swapper.load_model("django_ipam", "IPAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django_ipam models')
class TestIpAddress(TestCase):
    def test_string_representation(self):
        ipaddress = IPAddress(ip_address='entry ip_address')
        self.assertEqual(str(ipaddress), ipaddress.ip_address)


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django_ipam models')
class TestSubnet(TestCase):
    def test_string_representation(self):
        subnet = Subnet(name='entry name')
        self.assertEqual(str(subnet), subnet.name)


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django_ipam models')
class TestAdmin(TestCase):
        def setUp(self):
            self._superuser_login()

        def _superuser_login(self):
            user = User.objects.create_superuser(username="admin",
                                                 password="admin",
                                                 email="test@test.org")

            self.client.login(user)

        def test_subnet_change(self):
            obj = Subnet.objects.create(name="Sample Subnet",
                                        description="testing subnet")
            response = self.client.get(reverse('admin:sample_ipam_subnet_change', args=[obj.pk]),
                                       follow=True)
            self.assertContains(response, 'ok')

        def test_ipaddress_change(self):
            obj = IPAddress.objects.create(ip_address="196.168.1.1",
                                           description="test address")
            response = self.client.get(reverse('admin:sample_ipam_ipaddress_change', args=[obj.pk]),
                                       follow=True)
            self.assertContains(response, 'ok')
