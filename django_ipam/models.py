from swapper import swappable_setting

from .base.models import AbstractIpAddress, AbstractSubnet


class Subnet(AbstractSubnet):
    class Meta(AbstractSubnet.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'Subnet')


class IpAddress(AbstractIpAddress):
    class Meta(AbstractIpAddress.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'IpAddress')
