from django.forms import ModelForm
from .models import *



class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__' # Create a form with all fields in Order model
        
        