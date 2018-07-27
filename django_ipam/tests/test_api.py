import swapper
from django.test import TestCase

from .base.test_api import BaseTestApi


class TestApi(BaseTestApi, TestCase):
    ipaddress_model = swapper.load_model('django_ipam', 'IPAddress')
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
