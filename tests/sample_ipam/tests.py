import os
from unittest import skipUnless

import swapper
from django.test import TestCase

from django_ipam.tests.test_admin import BaseTestAdmin
from django_ipam.tests.test_api import BaseTestApi
from django_ipam.tests.test_forms import BaseTestForms, NetworkAddressTestModelForm
from django_ipam.tests.test_models import BaseTestModel

IpAddress = swapper.load_model("django_ipam", "IpAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django-ipam models')
class TestModel(BaseTestModel, TestCase):
    ipaddress_model = IpAddress
    subnet_model = Subnet


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django-ipam models')
class TestAdmin(BaseTestAdmin, TestCase):
    app_name = 'sample_ipam'
    subnet_model = Subnet
    ipaddress_model = IpAddress


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django-ipam models')
class TestForms(BaseTestForms, TestCase):
    form_class = NetworkAddressTestModelForm


@skipUnless(os.environ.get('SAMPLE_APP', False), 'Running tests on standard django-ipam models')
class TestApi(BaseTestApi, TestCase):
    subnet_model = Subnet
    ipaddress_model = IpAddress
