from ipaddress import IPv4Network, IPv6Network

from django.core.exceptions import ValidationError


class BaseTestModel(object):
    def test_ip_address_string_representation(self):
        ipaddress = self.ipaddress_model(ip_address='entry ip_address')
        self.assertEqual(str(ipaddress), ipaddress.ip_address)

    def test_invalid_ipaddress_subnet(self):
        failed = True
        self.create_subnet(dict(subnet='192.168.2.0/24'))
        try:
            self.create_ipaddress(dict(ip_address='10.0.0.2',
                                       subnet=self.subnet_model.objects.first()))
        except ValidationError as e:
            self.assertTrue(e.message_dict['ip_address'] == ['IP address does not belong to the subnet'])
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_valid_ipaddress_subnet(self):
        failed = False
        self.create_subnet(dict(subnet='192.168.2.0/24'))
        try:
            self.create_ipaddress(dict(ip_address='192.168.2.1',
                                       subnet=self.subnet_model.objects.first()))
        except ValidationError:
            failed = True
        if failed:
            self.fail('ValidationError raised')

    def test_used_ipaddress(self):
        failed = True
        self.create_subnet(dict(subnet='10.0.0.0/24'))
        self.create_ipaddress(dict(ip_address='10.0.0.1',
                                   subnet=self.subnet_model.objects.first()))
        try:
            self.create_ipaddress(dict(ip_address='10.0.0.1',
                                       subnet=self.subnet_model.objects.first()))
        except ValidationError as e:
            self.assertTrue(e.message_dict['ip_address'] == ["IP address already used."])
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_subnet_string_representation(self):
        subnet = self.subnet_model(subnet='entry subnet')
        self.assertEqual(str(subnet), str(subnet.subnet))

    def test_valid_cidr_field(self):
        failed = False
        try:
            self.create_subnet(dict(subnet='22.0.0.0/24'))
        except ValidationError:
            failed = True
        if failed:
            self.fail('ValidationError raised')

    def test_invalid_cidr_field(self):
        failed = True
        error_message = ["'192.192.192.192.192' does not appear to be an IPv4 or IPv6 network"]
        try:
            self.create_subnet(dict(subnet='192.192.192.192.192'))
        except ValidationError as e:
            self.assertTrue(e.message_dict['subnet'] == error_message)
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_overlapping_subnet(self):
        failed = True
        self.create_subnet(dict(subnet='192.168.2.0/24'))
        try:
            self.create_subnet(dict(subnet='192.168.2.0/25'))
        except ValidationError as e:
            self.assertTrue(e.message_dict['subnet'] == ['Subnet overlaps with 192.168.2.0/24'])
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_save_none_subnet_fails(self):
        failed = True
        try:
            self.create_subnet(dict(subnet=None))
        except ValidationError:
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_save_blank_subnet_fails(self):
        failed = True
        try:
            self.create_subnet(dict(subnet=""))
        except ValidationError:
            failed = False
        if failed:
            self.fail('ValidationError not raised')

    def test_retrieves_ipv4_ipnetwork_type(self):
        instance = self.create_subnet(dict(subnet='10.1.2.0/24'))
        instance = self.subnet_model.objects.get(pk=instance.pk)
        self.assertIsInstance(instance.subnet, IPv4Network)

    def test_retrieves_ipv6_ipnetwork_type(self):
        instance = self.create_subnet(dict(subnet='2001:db8::0/32'))
        instance = self.subnet_model.objects.get(pk=instance.pk)
        self.assertIsInstance(instance.subnet, IPv6Network)
