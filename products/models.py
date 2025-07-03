from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self) -> str:
        return str(self.name)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='subcategories/')

    def __str__(self) -> str:
        return f"{self.name} (Категория: {self.category.name})"

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_small = models.ImageField(upload_to='products/small/')
    image_medium = models.ImageField(upload_to='products/medium/')
    image_large = models.ImageField(upload_to='products/large/')

    def __str__(self) -> str: 
        return f"{self.name} - {self.price} ₽"