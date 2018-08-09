import swapper
from django.test import TestCase

from . import CreateModelsMixin, PostDataMixin
from .base.test_api import BaseTestApi


class TestApi(BaseTestApi, CreateModelsMixin, PostDataMixin, TestCase):
    ipaddress_model = swapper.load_model('django_ipam', 'IPAddress')
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
