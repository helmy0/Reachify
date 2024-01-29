from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index, name='home'),
    path("products/", views.products, name='products'),
    path("customer/<str:pk>/", views.customer, name='customer'), # <str:pk> is used to pass in the user ID and forwads it to .views.
    
]
