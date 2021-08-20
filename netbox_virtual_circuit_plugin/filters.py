import django_filters
from django.db.models import Q

from .models import VirtualCircuit


class VirtualCircuitFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = VirtualCircuit
        fields = [
            'vcid',
            'status',
            'context',
            'description',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(vcid__icontains=value)
            | Q(name__icontains=value)
            | Q(status__icontains=value)
            | Q(context__icontains=value)
            | Q(description__icontains=value)
        )

        return queryset.filter(qs_filter)
