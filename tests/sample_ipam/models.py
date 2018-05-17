# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_ipam.models import AbstractIpAddress, AbstractSubnet


class IpAddress(AbstractIpAddress):
    pass


class Subnet(AbstractSubnet):
    pass
