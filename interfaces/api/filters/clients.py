from django_filters import rest_framework as filters

from django.db.models import Q

from apps.clients.models import Client


class ClientFilter(filters.FilterSet):
    rating_start = filters.NumberFilter(field_name='rating', lookup_expr='gte', label='Рейтинг от')
    rating_end = filters.NumberFilter(field_name='rating', lookup_expr='lte', label='Рейтинг до')
    appointments_start = filters.NumberFilter(
        field_name='appointments_count',
        lookup_expr='gte',
        label='Кол-во посещений от',
    )
    appointments_end = filters.NumberFilter(
        field_name='appointments_count',
        lookup_expr='lte',
        label='Кол-во посещений до',
    )
    search = filters.CharFilter(method='search_filter', label='Поиск по имени или номеру телефона')
    tags = filters.BaseInFilter(field_name='tags__id', lookup_expr='in', label='Теги')

    class Meta:
        model = Client
        fields = [
            'branches',
            'rating_start',
            'rating_end',
            'appointments_start',
            'appointments_end',
            'search',
            'tags',
        ]

    def search_filter(self, queryset: Client.objects, name, value: str):
        value = value.lower()
        return queryset.filter(Q(name__icontains=value) | Q(phone__icontains=value))
