import os
from unittest import skipIf

from django.test import TestCase

from django_ipam.models import IpAddress, Subnet

from .base.test_admin import BaseTestAdmin


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestAdmin(BaseTestAdmin, TestCase):
    app_name = 'django_ipam'
    subnet_model = Subnet
    ipaddress_model = IpAddress
