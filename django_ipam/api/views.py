import swapper
from rest_framework.decorators import api_view
from rest_framework.response import Response

Subnet = swapper.load_model('django_ipam', 'Subnet')


@api_view(['POST'])
def request_ip(request, subnet_id):
    """
    Request the next available IP address under a subnet
    """
    subnet = Subnet.objects.get(pk=subnet_id)
    return Response(subnet.request_ip())
