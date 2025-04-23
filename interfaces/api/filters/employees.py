from django.db.models import Q, Count
from django_filters import rest_framework as filters

from apps.employees.models import Employee, EmployeeSchedule, EmployeeService, Service


class EmployeeFilter(filters.FilterSet):
    rating_start = filters.NumberFilter(
        field_name='rating', lookup_expr='gte', label='Рейтинг от')
    rating_end = filters.NumberFilter(
        field_name='rating', lookup_expr='lte', label='Рейтинг до')

    search = filters.CharFilter(
        method='search_filter', label='Поиск по имени или номеру телефона')

    services = filters.ModelMultipleChoiceFilter(
        field_name='services__service',
        queryset=Service.objects.all(),
        conjoined=True,
        label='Услуги'
    )

    def search_filter(self, queryset, name, value):
        parts = value.split()
        condition = (
            Q(name__icontains=parts[0]) & Q(surname__icontains=parts[1])
            if len(parts) == 2 else
            Q(name__icontains=value) | Q(surname__icontains=value) | Q(phone__icontains=value)
        )
        return queryset.filter(condition)

    class Meta:
        model = Employee
        fields = [
            'branches',
            'services',
            'position',
            'search',
            'rating_start',
            'rating_end',
            'is_active',
        ]


class EmployeeScheduleFilter(filters.FilterSet):
    start = filters.DateFilter(
        field_name='date', lookup_expr='gte', label='дата начала фильтрации')
    end = filters.DateFilter(
        field_name='date', lookup_expr='lte', label='дата конца фильтрации')

    class Meta:
        model = EmployeeSchedule
        fields = ['branch', 'employee', 'start', 'end']
