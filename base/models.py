from django.db import models
from django.contrib.auth.models import User
# from django.db.models.deletion import CASCADE

class Category(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length= 255)
    description = models.TextField(null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.CharField(max_length= 2083)
    barcode = models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name
