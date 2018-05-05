import os
from unittest import skipIf

from django.test import TestCase

from django_ipam.models import IPAddress, Subnet

from .base.test_models import BaseTestIpAddress, BaseTestSubnet


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestIpAddress(BaseTestIpAddress, TestCase):
    ipaddress_model = IPAddress


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestSubnet(BaseTestSubnet, TestCase):
    subnet_model = Subnet
