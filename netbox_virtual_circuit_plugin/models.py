from django.db import models


class VirtualCircuit(models.Model):
    """
    Define a Virtual Circuit database model.
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
        choices=CONNECTION_STATUS
    )

    context = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ['vcid']

    def __str__(self):
        return self.name
