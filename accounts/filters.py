import django_filters 
from django_filters import DateFilter,CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    start_data = DateFilter(field_name="data_created", lookup_expr="gte")
    
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'data_created']
        