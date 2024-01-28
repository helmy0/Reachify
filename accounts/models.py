from django.db import models

# Create your models here.

class Customer(models.Model):
    #ID is created by default
    #Creating a Customer table with four fields name, phone, email ,and data-created. 
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True) # Allows us to create the date and time when an instance of this class is created in the database.
    
    def __str__(self):
        return self.name # Returns customer object's name to be viewed as such in the admin site
    
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
    
    def __str__(self):
        return self.name


class Order(models.Model):
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for deliver', 'Out for deliver'),
        ('Delivered','Delivered')
    )
    
    customer = models.ForeignKey(Customer, null = True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null = True, on_delete=models.CASCADE) 
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices = STATUS)
    
    def __str__(self):
        return self.customer.name + "'s Order"