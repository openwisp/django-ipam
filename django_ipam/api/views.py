import swapper
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import IpAddressSerializer, IpRequestSerializer

Subnet = swapper.load_model('django_ipam', 'Subnet')


@api_view(['GET'])
def get_first_available_ip(request, subnet_id):
    """
    Get the next available IP address under a subnet
    """
    subnet = get_object_or_404(Subnet, pk=subnet_id)
    return Response(subnet.get_first_available_ip())


class RequestIPView(CreateAPIView):
    """
    Request and create a record for the next available IP address under a subnet
    """
    serializer_class = IpRequestSerializer

    def post(self, request, *args, **kwargs):
        subnet = get_object_or_404(Subnet, pk=kwargs["subnet_id"])
        ip_address = subnet.request_ip(dict(description=request.data.get("description")))
        if ip_address:
            serializer = IpAddressSerializer(ip_address)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(None)
