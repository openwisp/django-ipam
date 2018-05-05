# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django_ipam.models import AbstractIPAddress, AbstractSubnet


class IPAddress(AbstractIPAddress):
    pass


class Subnet(AbstractSubnet):
    pass
