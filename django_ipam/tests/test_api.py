from django.test import TestCase

from django_ipam.models import IpAddress, Subnet

from .base.test_api import BaseTestApi


class TestApi(BaseTestApi, TestCase):
    subnet_model = Subnet
    ipaddress_model = IpAddress
