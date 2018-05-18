import os
from unittest import skipIf

from django.forms import ModelForm
from django.test import TestCase

from django_ipam.models import Subnet

from .base.test_forms import BaseTestForms


class NetworkAddressTestModelForm(ModelForm):
    class Meta:
        model = Subnet
        fields = ("subnet",)


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestForms(BaseTestForms, TestCase):
    form_class = NetworkAddressTestModelForm
