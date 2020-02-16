from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Category(models.Model):
    levels = (
        ("PRODUCT","PRODUCT"),
        ("SERVICE","SERVICE"),
    )
    category_name = models.CharField(max_length=50)
    category_level = models.CharField(max_length=10,choices=levels)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_description = models.TextField(max_length=100)
    product_seller = models.ForeignKey(User,on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=8,decimal_places=2)
    is_negotiable = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to='media')
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
