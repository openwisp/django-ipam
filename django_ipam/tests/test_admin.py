import os
from unittest import skipIf

import swapper
from django.test import TestCase

from . import CreateModelsMixin, PostDataMixin
from .base.test_admin import BaseTestAdmin


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestAdmin(BaseTestAdmin, CreateModelsMixin, PostDataMixin, TestCase):
    app_name = 'django_ipam'
    ipaddress_model = swapper.load_model('django_ipam', 'IPAddress')
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
