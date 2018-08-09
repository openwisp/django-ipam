import swapper
from django.test import TestCase

from . import CreateModelsMixin, FileMixin
from .base.test_commands import BaseTestCommands


class TestCommands(BaseTestCommands, CreateModelsMixin, TestCase, FileMixin):
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
    ipaddress_model = swapper.load_model('django_ipam', 'IpAddress')
