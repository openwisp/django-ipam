from swapper import swappable_setting

from .base.models import AbstractIPAddress, AbstractSubnet


class IPAddress(AbstractIPAddress):
    class Meta(AbstractIPAddress.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'IPAddress')


class Subnet(AbstractSubnet):
    class Meta(AbstractSubnet.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'Subnet')
