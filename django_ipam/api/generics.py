import csv

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from ..base.models import CsvImportException
from .serializers import ImportSubnetSerializer, IpAddressSerializer, IpRequestSerializer, SubnetSerializer


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


class BaseImportSubnetView(CreateAPIView):
    serializer_class = ImportSubnetSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def post(self, request, *args, **kwargs):
        file = request.FILES['csvfile']
        if not file.name.endswith(('.csv', '.xls', '.xlsx')):
            return Response({'error': _('File type not supported.')}, status=400)
        try:
            self.subnet_model.import_csv(self, file)
        except CsvImportException as e:
            return Response({'error': _(str(e))}, status=400)
        return Response({'detail': _('Data imported successfully.')})


class BaseExportSubnetView(CreateAPIView):
    serializer_class = serializers.Serializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ip_address.csv"'
        writer = csv.writer(response)
        self.subnet_model.export_csv(self, kwargs['subnet_id'], writer)
        return response
