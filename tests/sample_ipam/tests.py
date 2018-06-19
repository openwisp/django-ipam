import swapper
from django.test import TestCase

from django_ipam.tests.test_admin import BaseTestAdmin
from django_ipam.tests.test_api import BaseTestApi
from django_ipam.tests.test_forms import BaseTestForms, NetworkAddressTestModelForm
from django_ipam.tests.test_models import BaseTestModel

IpAddress = swapper.load_model("django_ipam", "IpAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


class TestModel(BaseTestModel, TestCase):
    ipaddress_model = IpAddress
    subnet_model = Subnet


class TestAdmin(BaseTestAdmin, TestCase):
    app_name = 'django_ipam'
    subnet_model = Subnet
    ipaddress_model = IpAddress


class TestForms(BaseTestForms, TestCase):
    form_class = NetworkAddressTestModelForm


class TestApi(BaseTestApi, TestCase):
    subnet_model = Subnet
    ipaddress_model = IpAddress
