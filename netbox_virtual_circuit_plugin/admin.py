from django.contrib import admin
from .models import VirtualCircuit, VCVLAN


@admin.register(VirtualCircuit)
class VirtualCircuitAdmin(admin.ModelAdmin):
    """
    Administrative view for Virtual Circuit.
    """
    list_display = ('vcid', 'name', 'status', 'context')


@admin.register(VCVLAN)
class VCVLANAdmin(admin.ModelAdmin):
    """
    Administrative view for VCVLAN.
    """
    list_display = ('vc', 'vlan')
