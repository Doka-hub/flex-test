from django_filters import rest_framework as filters

from apps.finances.models import CashRegister, CashRegisterOperation


class CashRegisterFilter(filters.FilterSet):
    class Meta:
        model = CashRegister
        fields = ['branch', 'register_type']


class CashRegisterOperationFilter(filters.FilterSet):
    start = filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Дата начала фильтрации')
    end = filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Дата конца фильтрации')

    class Meta:
        model = CashRegisterOperation
        fields = ['start', 'end', 'operation_type', 'purpose']
