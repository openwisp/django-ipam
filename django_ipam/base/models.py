from ipaddress import ip_address, ip_network

import swapper
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from openwisp_utils.base import TimeStampedEditableModel

from .fields import NetworkField

HELP_TEXT = 'Enter valid CIDR network field, for example - IPv4: 10.0.0.0/24 or IPv6: fdb6:21b:a477::9f7/64'


class AbstractSubnet(TimeStampedEditableModel):
    subnet = NetworkField(help_text=HELP_TEXT, db_index=True)
    description = models.CharField(max_length=100, blank=True)
    master_subnet = models.ForeignKey('self', on_delete=models.CASCADE,
                                      blank=True, null=True,
                                      related_name="child_subnets")

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['subnet'], name='subnet_idx')
        ]

    def __str__(self):
        return str(self.subnet)

    def clean(self):
        for subnet in swapper.load_model("django_ipam", "Subnet").objects.filter().values():
            if self.id != subnet["id"]:
                if ip_network(self.subnet).overlaps(subnet["subnet"]):
                    raise ValidationError({'subnet': _('Subnet overlaps with %s') % (subnet["subnet"])})


class AbstractIpAddress(TimeStampedEditableModel):
    ip_address = models.GenericIPAddressField()
    description = models.CharField(max_length=100, blank=True)
    subnet = models.ForeignKey(swapper.get_model_name("django_ipam", "Subnet"),
                               on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.ip_address

    def clean(self):
        if self.subnet_id and ip_address(self.ip_address) not in self.subnet.subnet:
            raise ValidationError({'ip_address': _('IP address does not belong to the subnet')})
        for ipaddr in swapper.load_model("django_ipam", "IpAddress").objects.filter().values():
            if self.id != ipaddr["id"]:
                if ip_address(self.ip_address) == ip_address(ipaddr["ip_address"]):
                    raise ValidationError({'ip_address': _('IP address already used.')})
