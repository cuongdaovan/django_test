from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    category_description=models.TextField(max_length=1000)
class Product(models.Model):
    category=models.ForeignKey(Category,name="cat",on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    product_description=models.TextField(max_length=1000)
    product_cost=models.FloatField()
    product_image=models.ImageField("image")