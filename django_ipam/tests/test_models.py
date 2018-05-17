import os
from unittest import skipIf

from django.test import TestCase

from django_ipam.models import IpAddress, Subnet

from .base.test_models import BaseTestModel


class CreateModelsMixin:
        def create_subnet(self, options):
            instance = Subnet(**options)
            instance.full_clean()
            instance.save()
            return instance

        def create_ipaddress(self, options):
            instance = IpAddress(**options)
            instance.full_clean()
            instance.save()
            return instance


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestModel(BaseTestModel, TestCase, CreateModelsMixin):
    ipaddress_model = IpAddress
    subnet_model = Subnet
