from django.contrib import admin

from .base.admin import AbstractIPAddressAdmin, AbstractSubnetAdmin
from .models import IPAddress, Subnet


@admin.register(IPAddress)
class IPAddressAdmin(AbstractIPAddressAdmin):
    pass


@admin.register(Subnet)
class BaseSubnet(AbstractSubnetAdmin):
    pass
