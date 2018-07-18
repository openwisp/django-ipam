import swapper
from rest_framework import serializers

IpAddress = swapper.load_model('django_ipam', 'IpAddress')
Subnet = swapper.load_model('django_ipam', 'Subnet')


class IpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ('subnet', 'description')
        read_only_fields = ('created', 'modified')


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = '__all__'
        read_only_fields = ('created', 'modified')


class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'
        read_only_fields = ('created', 'modified')


class ImportSubnetSerializer(serializers.Serializer):
    csvfile = serializers.FileField()
