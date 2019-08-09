from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Store(models.Model):                                                              
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.title


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(User, on_delete = models.CASCADE)
    file = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.text


