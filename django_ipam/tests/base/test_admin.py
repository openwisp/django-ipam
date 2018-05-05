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
        obj = self.subnet_model.objects.create(name="Sample Subnet",
                                               description="testing subnet")
        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[obj.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')

    def test_ipaddress_change(self):
        obj = self.ipaddress_model.objects.create(ip_address="196.168.1.1",
                                                  description="test address")
        response = self.client.get(reverse('admin:{0}_ipaddress_change'.format(self.app_name), args=[obj.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
