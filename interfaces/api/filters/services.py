from django_filters import rest_framework as filters
from apps.services.models import Service, ServiceCategory
from apps.branches.models import Branch


class ServiceFilter(filters.FilterSet):
    frequency_start = filters.NumberFilter(field_name='frequency', lookup_expr='gte', label='Частота заказов от')
    frequency_end = filters.NumberFilter(field_name='frequency', lookup_expr='lte', label='Частота заказов до')

    cost_start = filters.NumberFilter(field_name='cost', lookup_expr='gte', label='Стоимость от')
    cost_end = filters.NumberFilter(field_name='cost', lookup_expr='lte', label='Стоимость до')

    duration_start = filters.DurationFilter(
        field_name='duration', lookup_expr='gte', label='Длительность от (в секундах)'
    )
    duration_end = filters.DurationFilter(
        field_name='duration', lookup_expr='lte', label='Длительность до (в секундах)'
    )

    category = filters.ModelMultipleChoiceFilter(
        field_name='category',
        queryset=ServiceCategory.objects.all(),
        to_field_name='id',
        label='Категория'
    )

    branch = filters.ModelChoiceFilter(
        field_name='category__branches',
        queryset=Branch.objects.all(),
        to_field_name='id',
        label='Филиал'
    )

    class Meta:
        model = Service
        fields = [
            'branch',
            'category',
            'frequency_start',
            'frequency_end',
            'cost_start',
            'cost_end',
            'duration_start',
            'duration_end',
        ]
