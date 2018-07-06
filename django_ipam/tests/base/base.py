from django_ipam.models import IpAddress, Subnet


class CreateModelsMixin(object):
        def _create_subnet(self, **kwargs):
            instance = Subnet(**dict(kwargs))
            instance.full_clean()
            instance.save()
            return instance

        def _create_ipaddress(self, **kwargs):
            instance = IpAddress(**dict(kwargs))
            instance.full_clean()
            instance.save()
            return instance
