from django_filters import rest_framework as filters

from apps.loyalty.models import Promotion


class PromotionFilter(filters.FilterSet):
    class Meta:
        model = Promotion
        fields = ['value_type', 'is_active']
