import swapper
from django.test import TestCase

from django_ipam.tests.test_admin import BaseTestAdmin
from django_ipam.tests.test_forms import BaseTestForms, NetworkAddressTestModelForm
from django_ipam.tests.test_models import BaseTestModel, CreateModelsMixin

IpAddress = swapper.load_model("django_ipam", "IpAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


class TestModel(TestCase, BaseTestModel, CreateModelsMixin):
    ipaddress_model = IpAddress
    subnet_model = Subnet


class TestAdmin(TestCase, BaseTestAdmin):
    app_name = 'django_ipam'
    subnet_model = Subnet
    ipaddress_model = IpAddress


class TestForms(TestCase, BaseTestForms):
    form_class = NetworkAddressTestModelForm
