import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from .models import VirtualCircuit


class VirtualCircuitTable(BaseTable):
    pk = ToggleColumn()

    class Meta(BaseTable.Meta):
        model = VirtualCircuit
        fields = (
            'pk',
            'vcid',
            'name',
            'status',
            'context',
        )
