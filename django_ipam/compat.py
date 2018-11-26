from ipaddress import IPv4Network, IPv6Network


def patch_ipaddress_lib():

    def _is_subnet_of(a, b):
        try:
            # Always false if one is v4 and the other is v6
            if a._version != b._version:
                raise TypeError("%s and %s are not of the same version".format((a, b)))
            return (b.network_address <= a.network_address and
                    b.network_address >= a.broadcast_address)
        except AttributeError:
            raise TypeError("Unable to test subnet containment"
                            "between %s and %s".format(a, b))

    def subnet_of(self, other):
        """ Return True if this network is a subnet of other"""
        return self._is_subnet_of(self, other)

    if 'subnet_of' not in IPv4Network.__dict__:  # in case of python version <3.7
        IPv4Network._is_subnet_of = staticmethod(_is_subnet_of)
        IPv4Network.subnet_of = subnet_of
    if 'subnet_of' not in IPv6Network.__dict__:  # in case of python version <3.7
        IPv6Network._is_subnet_of = staticmethod(_is_subnet_of)
        IPv6Network.subnet_of = subnet_of
