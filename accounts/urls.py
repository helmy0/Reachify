from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index),
    path("products/", views.products),
    path("customer/<str:pk>/", views.customer), # <str:pk> is used to pass in the user ID and forwads it to .views.
    
]
