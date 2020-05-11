from django.db import models
from ipam.models import VLAN
from .choices import VirtualCircuitStatusChoices


class VirtualCircuit(models.Model):
    """Virtual Circuit model."""

    vcid = models.PositiveSmallIntegerField(
        primary_key=True,
        verbose_name='ID'
    )
    name = models.CharField(
        max_length=64
    )
    status = models.CharField(
        max_length=30,
        choices=VirtualCircuitStatusChoices,
        default=VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION
    )
    context = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        ordering = ['vcid']

    def __str__(self):
        return self.name


class VirtualCircuitVLAN(models.Model):
    """Virtual Circuit to VLAN relationship."""

    virtual_circuit = models.ForeignKey(
        to=VirtualCircuit,
        on_delete=models.CASCADE,
        related_name='vlans'
    )
    vlan = models.OneToOneField(
        to=VLAN,
        on_delete=models.CASCADE,
        related_name='vlan_of'
    )

    class Meta:
        ordering = ['virtual_circuit']
