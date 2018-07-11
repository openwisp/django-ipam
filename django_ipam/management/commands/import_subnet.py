import swapper

from . import BaseImportSubnetCommand


class Command(BaseImportSubnetCommand):
    subnet_model = swapper.load_model('django_ipam', 'Subnet')
