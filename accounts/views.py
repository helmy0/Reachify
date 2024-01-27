from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'dashboard.html')

def products(request):
    return render(request,'products.html')

def customer(request):
    return render(request,'customer.html')
