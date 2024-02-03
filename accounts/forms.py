from django.forms import ModelForm
from django_filters import DateFilter
from .models import *



class OrderForm(ModelForm):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__' # Create a form with all fields in Order model
        exclude = ['customer', 'date_created']
        