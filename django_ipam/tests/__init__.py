import json
import os

import swapper

IpAddress = swapper.load_model("django_ipam", "IPAddress")
Subnet = swapper.load_model("django_ipam", "Subnet")


class FileMixin(object):
    def _get_path(self, file):
        d = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(d, file)


class CreateModelsMixin(object):
    def _get_extra_fields(self, **kwargs):
        # For adding mandatory extra fields
        options = dict()
        options.update(**kwargs)
        return options

    def _create_subnet(self, **kwargs):
        options = dict(
            subnet='',
            description='',
        )
        options.update(self._get_extra_fields())
        options.update(kwargs)
        instance = Subnet(**options)
        instance.full_clean()
        instance.save()
        return instance

    def _create_ipaddress(self, **kwargs):
        options = dict(
            ip_address='',
            description='',
        )
        options.update(self._get_extra_fields())
        options.update(kwargs)
        instance = IpAddress(**options)
        instance.full_clean()
        instance.save()
        return instance


class PostDataMixin(object):
    def _post_data(self, **kwargs):
        return json.dumps(dict(kwargs))
