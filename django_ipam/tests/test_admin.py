import os
from unittest import skipIf

from django.test import TestCase

from django_ipam.models import IPAddress, Subnet

from .base.test_admin import BaseTestAdmin


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestAdmin(TestCase, BaseTestAdmin):
    app_name = 'django_ipam'
    subnet_model = Subnet
    ipaddress_model = IPAddress
