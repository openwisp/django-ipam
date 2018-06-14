from django.contrib.auth.models import User
from django.urls import reverse


class BaseTestAdmin(object):
    def setUp(self):
        User.objects.create_superuser(username='admin',
                                      password='tester',
                                      email='admin@admin.com')
        self.client.login(username='admin', password='tester')

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
        self.assertEqual(self.ipaddress_model.objects.get(pk=obj.pk).ip_address, '10.0.0.1')

    def test_ipv4_subnet_change(self):
        subnet = self.subnet_model(subnet="10.0.0.0/24", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        ipaddr = self.ipaddress_model(ip_address="10.0.0.1", subnet=subnet)
        ipaddr.full_clean()
        ipaddr.save()

        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[subnet.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, '<h3>Subnet Visual Display</h3>')

    def test_ipv6_subnet_change(self):
        subnet = self.subnet_model(subnet="fdb6:21b:a477::9f7/64", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        ipaddr = self.ipaddress_model(ip_address="fdb6:21b:a477::9f7", subnet=subnet)
        ipaddr.full_clean()
        ipaddr.save()

        response = self.client.get(reverse('admin:{0}_subnet_change'.format(self.app_name), args=[subnet.pk]),
                                   follow=True)
        self.assertContains(response, 'ok')
        self.assertContains(response, '<h3>Used IP address</h3>')

    def test_subnet_popup_response(self):
        subnet = self.subnet_model(subnet="fdb6:21b:a477::9f7/64", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        ipaddr = self.ipaddress_model(ip_address="fdb6:21b:a477::9f7", subnet=subnet)
        ipaddr.full_clean()
        ipaddr.save()

        response = self.client.get('/admin/django_ipam/subnet/{0}/change/?_popup=1'.format(subnet.id),
                                   follow=True)
        self.assertContains(response, 'ok')

    def test_ipaddress_response(self):
        subnet = self.subnet_model(subnet="10.0.0.0/24", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        post_data = {
            'ip_address': "10.0.0.1",
            'subnet': subnet.id,
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
        }
        response = self.client.post("/admin/django_ipam/ipaddress/add/",
                                    post_data, follow=True)
        self.assertContains(response, 'ok')

    def test_ipaddress_popup_response(self):
        subnet = self.subnet_model(subnet="10.0.0.0/24", description="Sample Subnet")
        subnet.full_clean()
        subnet.save()

        post_data = {
            'ip_address': "10.0.0.1",
            'subnet': subnet.id,
            'created_0': '2017-08-08',
            'created_1': '15:16:10',
            'modified_0': '2017-08-08',
            'modified_1': '15:16:10',
            '_popup': '1',
        }
        response = self.client.post("/admin/django_ipam/ipaddress/add/",
                                    post_data)
        self.assertContains(response, 'opener.dismissAddAnotherPopup(window);')
