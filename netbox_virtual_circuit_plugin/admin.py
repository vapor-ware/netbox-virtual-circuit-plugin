from django.contrib import admin
from .models import VirtualCircuit, VirtualCircuitVLAN


@admin.register(VirtualCircuit)
class VirtualCircuitAdmin(admin.ModelAdmin):
    """Administrative view for VirtualCircuit."""

    list_display = ('vcid', 'name', 'status', 'context')


@admin.register(VirtualCircuitVLAN)
class VirtualCircuitVLANAdmin(admin.ModelAdmin):
    """Administrative view for VirtualCircuitVLAN."""

    list_display = ('virtual_circuit', 'vlan')
