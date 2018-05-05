# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import swapper
from django.contrib import admin

from django_ipam.admin import AbstractIPAddressAdmin, AbstractSubnetAdmin

IPAddress = swapper.load_model("django_ipam", "IPAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


@admin.register(IPAddress)
class IPAddressAdmin(AbstractIPAddressAdmin):
    pass


@admin.register(Subnet)
class SubnetAdmin(AbstractSubnetAdmin):
    pass
