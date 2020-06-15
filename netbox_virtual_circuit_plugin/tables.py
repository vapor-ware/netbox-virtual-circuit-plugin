import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn

from .models import VirtualCircuit


class VirtualCircuitTable(BaseTable):
    pk = ToggleColumn()
    vcid = tables.LinkColumn(
        viewname='plugins:netbox_virtual_circuit_plugin:virtual_circuit',
        args=[Accessor('vcid')]
    )

    class Meta(BaseTable.Meta):
        model = VirtualCircuit
        fields = (
            'pk',
            'vcid',
            'name',
            'status',
            'context',
        )
