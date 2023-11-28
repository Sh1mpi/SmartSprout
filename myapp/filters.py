import django_filters
from .models import InGreenhouse

class InGreenhouseFilter(django_filters.FilterSet):
    class Meta:
        model = InGreenhouse
        fields = {
            'user': ['exact'],
            'cell': ['startswith'],
            'planting_date': ['gte'],
        }