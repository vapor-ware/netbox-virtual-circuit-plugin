from django.db import models
from ipam.models import VLAN


class VirtualCircuit(models.Model):
    """
    Virtual Circuit model.
    """
    vcid = models.AutoField(
        primary_key=True,
        verbose_name='ID'
    )

    name = models.CharField(
        max_length=64
    )

    CONNECTION_STATUS = [
        ('PC', 'Pending Configuration'),
        ('CF', 'Configured'),
        ('PD', 'Pending Deletion'),
        ('CE', 'Configuration Error')
    ]
    status = models.CharField(
        max_length=2,
        choices=CONNECTION_STATUS,
        blank=True,
        default='PC'
    )

    context = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ['vcid']

    def __str__(self):
        return self.name


class VirtualCircuitVLAN(models.Model):
    """
    Virtual Circuit to VLAN relationship.
    """
    vc = models.ForeignKey(
        to=VirtualCircuit,
        on_delete=models.CASCADE
    )

    vlan = models.OneToOneField(
        to=VLAN,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['vc']

