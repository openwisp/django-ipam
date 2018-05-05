import swapper
from django.db import models
from openwisp_utils.base import TimeStampedEditableModel


class AbstractSubnet(TimeStampedEditableModel):
    name = models.CharField(max_length=100, blank=True)  # Add a default value
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractIPAddress(TimeStampedEditableModel):
    ip_address = models.GenericIPAddressField()
    description = models.CharField(max_length=100, blank=True)
    subnet = models.ForeignKey(swapper.get_model_name("django_ipam", "Subnet"),
                               on_delete=models.CASCADE,
                               blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.ip_address
