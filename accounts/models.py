from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    #ID is created by default
    #Creating a Customer table with four fields name, phone, email ,and data-created. 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='defaultProfile.png',null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True) # Allows us to create the date and time when an instance of this class is created in the database.
    
    def __str__(self):
        return self.name if self.name else 'No name'
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
       
class Product(models.Model):
    
    
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    description = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    
    def __str__(self):
        return self.name



class Order(models.Model):
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered')
    )
    
    customer = models.ForeignKey(Customer, null = True, on_delete=models.CASCADE) # One-to-many to product
    product = models.ForeignKey(Product, null = True, on_delete=models.CASCADE) 
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices = STATUS)
    note = models.CharField(max_length=1000, null=True)

    
    
    def __str__(self):
        return self.product.name