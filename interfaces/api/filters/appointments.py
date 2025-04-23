from django_filters import rest_framework as filters

from apps.appointments.models import Appointment


class AppointmentFilter(filters.FilterSet):
    start = filters.DateFilter(field_name='date', lookup_expr='gte', label='дата начала фильтрации')
    end = filters.DateFilter(field_name='date', lookup_expr='lte', label='дата конца фильтрации')
    branch = filters.NumberFilter(field_name='branch', label='фильтрация по id филиала')

    class Meta:
        model = Appointment
        fields = ['start', 'end', 'branch']
