from ipaddress import ip_address, ip_network

import swapper
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from openwisp_utils.base import TimeStampedEditableModel

from .fields import NetworkField


class AbstractSubnet(TimeStampedEditableModel):
    subnet = NetworkField(db_index=True,
                          help_text=_('Subnet in CIDR notation, eg: "10.0.0.0/24" '
                                      'for IPv4 and "fdb6:21b:a477::9f7/64" for IPv6'))
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
            if self.id != subnet["id"] and ip_network(self.subnet).overlaps(subnet["subnet"]):
                raise ValidationError({'subnet': _('Subnet overlaps with %s') % (subnet["subnet"])})

    def get_first_available_ip(self):
        ipaddress_set = [ip.ip_address for ip in self.ipaddress_set.all()]
        for host in self.subnet.hosts():
            if str(host) not in ipaddress_set:
                return str(host)
        return None

    def request_ip(self, options=None):
        if options is None:
            options = {}
        ip = self.get_first_available_ip()
        if ip:
            ip_address = swapper.load_model("django_ipam", "IpAddress")(
                                            ip_address=ip,
                                            subnet=self,
                                            **options)
            ip_address.full_clean()
            ip_address.save()
            return ip_address
        return None


class AbstractIpAddress(TimeStampedEditableModel):
    ip_address = models.GenericIPAddressField()
    description = models.CharField(max_length=100, blank=True)
    subnet = models.ForeignKey(swapper.get_model_name("django_ipam", "Subnet"),
                               on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.ip_address

    def clean(self):
        if self.subnet_id and ip_address(self.ip_address) not in self.subnet.subnet:
            raise ValidationError({'ip_address': _('IP address does not belong to the subnet')})
        for ipaddr in swapper.load_model("django_ipam", "IpAddress").objects.filter().values():
            if self.id != ipaddr["id"] and ip_address(self.ip_address) == ip_address(ipaddr["ip_address"]):
                raise ValidationError({'ip_address': _('IP address already used.')})
