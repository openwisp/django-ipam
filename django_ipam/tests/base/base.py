from django_ipam.models import IpAddress, Subnet


class CreateModelsMixin(object):
        def _create_subnet(self, options):
            instance = Subnet(**options)
            instance.full_clean()
            instance.save()
            return instance

        def _create_ipaddress(self, options):
            instance = IpAddress(**options)
            instance.full_clean()
            instance.save()
            return instance
