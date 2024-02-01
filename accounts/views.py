from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

# Create your views here.
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
        }
    
    return render(request,'dashboard.html', context)

def products(request):
    
    products = Product.objects.all()
    
    return render(request,'products.html', {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    customer_orders_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'customer_orders_count':customer_orders_count}
    return render(request,'customer.html', context)

def createOrder(request):
    form = OrderForm
    context = {'form':form}
    
    if request.method == 'POST': # If request equal to post
        print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
        
    if request.method == 'POST': # If request equal to post
        print('Printing POST', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')  # Redirect to a page of your choice after deleting the order
    context = {'item': order}
    return render(request, 'delete.html', context)