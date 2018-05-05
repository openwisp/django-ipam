class BaseTestIpAddress(object):
    def test_string_representation(self):
        ipaddress = self.ipaddress_model(ip_address='entry ip_address')
        self.assertEqual(str(ipaddress), ipaddress.ip_address)


class BaseTestSubnet(object):
    def test_string_representation(self):
        subnet = self.subnet_model(name='entry name')
        self.assertEqual(str(subnet), subnet.name)
