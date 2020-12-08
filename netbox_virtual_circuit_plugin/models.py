from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from ipam.models import VLAN
from extras.models import ChangeLoggedModel

from .choices import VirtualCircuitStatusChoices


class VirtualCircuit(ChangeLoggedModel):
    """Virtual Circuit model."""

    vcid = models.BigIntegerField(
        primary_key=True,
        verbose_name='ID',
        validators=[
            MaxValueValidator(4294967295),
            MinValueValidator(1),
        ],
    )
    name = models.CharField(
        max_length=64,
    )
    status = models.CharField(
        max_length=30,
        choices=VirtualCircuitStatusChoices,
        default=VirtualCircuitStatusChoices.STATUS_PENDING_CONFIGURATION,
    )
    context = models.CharField(
        max_length=100,
        blank=True,
    )
    description = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ['vcid']
        verbose_name = 'Virtual Circuit'
        verbose_name_plural = 'Virtual Circuits'

    def __str__(self):
        return f'{self.vcid} ({self.name})'

    def get_absolute_url(self):
        return reverse('plugins:netbox_virtual_circuit_plugin:virtual_circuit', args=[self.vcid])

class VirtualCircuitVLAN(ChangeLoggedModel):
    """Virtual Circuit to VLAN relationship."""

    virtual_circuit = models.ForeignKey(
        to=VirtualCircuit,
        on_delete=models.CASCADE,
        related_name='vlans',
        verbose_name='Virtual Circuit',
    )
    vlan = models.OneToOneField(
        to=VLAN,
        on_delete=models.CASCADE,
        related_name='virtual_circuit',
        verbose_name='VLAN',
    )

    class Meta:
        ordering = ['virtual_circuit']
        verbose_name = 'Virtual-Circuit-to-VLAN connection'
        verbose_name_plural = 'Virtual-Circuit-to-VLAN connections'

    def get_absolute_url(self):
        return reverse('plugins:netbox_virtual_circuit_plugin:virtual_circuit', args=[self.virtual_circuit.vcid])
