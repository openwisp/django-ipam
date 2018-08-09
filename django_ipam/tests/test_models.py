import os
from unittest import skipIf

import swapper
from django.test import TestCase

from . import CreateModelsMixin
from .base.test_models import BaseTestModel


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestModel(BaseTestModel, CreateModelsMixin, TestCase):
    ipaddress_model = swapper.load_model('django_ipam', 'IPAddress')
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
