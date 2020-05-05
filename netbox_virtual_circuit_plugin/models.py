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
        ('NP', 'Interface H/W Not Present'),
        ('EI', 'Encapsulation Invalid'),
        ('EM', 'Encapsulation Mismatch'),
        ('VM', 'VLAN ID Mismatch'),
        ('BK', 'Backup Connection'),
        ('ST', 'Standby Connection'),
        ('LD', 'Local Site Signaled Down'),
        ('HS', 'Hot-standby Connection')
    ]
    status = models.CharField(
        max_length=2,
        choices=CONNECTION_STATUS,
        blank=True
    )

    context = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ['vcid']

    def __str__(self):
        return self.name


class VCVLAN(models.Model):
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

