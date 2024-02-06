from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.shortcuts import render,redirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from .decorators import *

@unauthenticated_user
def registerPage(request):


    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            messages.success(request, "Account was created for "+ username )
            return redirect('login')
        
    return render(request, 'register.html', {'form': form})

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username') # Both values are fetched from login.html inputs
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'user.html', context )

@login_required(login_url='login')
 # Hard code login restriction. Should implement a file to process it later on.
@admin_only

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




@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])

def products(request):
    
    products = Product.objects.all()
    
    return render(request,'products.html', {'products':products})



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    customer_orders_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    
    orders = myFilter.qs
    
    context = {'customer':customer, 'orders':orders, 'customer_orders_count':customer_orders_count, 'myFilter':myFilter}
    return render(request,'customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)

    # form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST': # If request equal to post
        print('Printing POST', request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
        
    return render(request, 'order_form.html', context)
    



@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])

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




@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')  # Redirect to a page of your choice after deleting the order
    context = {'item': order}
    return render(request, 'delete.html', context)


