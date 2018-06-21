import swapper
from rest_framework import serializers

IpAddress = swapper.load_model("django_ipam", "IpAddress")


class IpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ('subnet', 'description')


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ('ip_address', 'subnet', 'description')
