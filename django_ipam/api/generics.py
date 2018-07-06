from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from .serializers import IpAddressSerializer, IpRequestSerializer, SubnetSerializer


class BaseIpAddressListCreateView(ListCreateAPIView):
    serializer_class = IpAddressSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        subnet = get_object_or_404(self.subnet_model, pk=self.kwargs["subnet_id"])
        return subnet.ipaddress_set.all()


class BaseSubnetListCreateView(ListCreateAPIView):
    serializer_class = SubnetSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)


class BaseSubnetView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubnetSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)


class BaseIpAddressView(RetrieveUpdateDestroyAPIView):
    serializer_class = IpAddressSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)


class BaseRequestIPView(CreateAPIView):
    serializer_class = IpRequestSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def post(self, request, *args, **kwargs):
        subnet = get_object_or_404(self.subnet_model, pk=kwargs["subnet_id"])
        ip_address = subnet.request_ip(dict(description=request.data.get("description")))
        if ip_address:
            serializer = IpAddressSerializer(ip_address)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(None)
