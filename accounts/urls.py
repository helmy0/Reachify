from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index, name='home'),
    path("products/", views.products, name='products'),
    path("customer/<str:pk>/", views.customer, name='customer'), # <str:pk> is used to pass in the user ID and forwads it to .views.
     
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    
    path('logout/', views.logoutUser, name="logout"),



]

