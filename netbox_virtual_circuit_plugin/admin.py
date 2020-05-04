from django.contrib import admin

from .models import VirtualCircuit


@admin.register(VirtualCircuit)
class VirtualCircuitAdmin(admin.ModelAdmin):
    """
    Administrative view for the VirtualCircuit model.
    """
    list_display = ('vcid', 'name', 'status', 'context')
