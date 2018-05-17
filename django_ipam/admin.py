from django.contrib import admin

from .base.admin import AbstractIpAddressAdmin, AbstractSubnetAdmin
from .models import IpAddress, Subnet


@admin.register(IpAddress)
class IPAddressAdmin(AbstractIpAddressAdmin):
    pass


@admin.register(Subnet)
class BaseSubnet(AbstractSubnetAdmin):
    pass
