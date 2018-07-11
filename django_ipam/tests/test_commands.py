import swapper
from django.test import TestCase

from .base.test_commands import BaseTestCommands


class TestCommands(BaseTestCommands, TestCase):
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
    ipaddress_model = swapper.load_model('django_ipam', 'IpAddress')
