from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def get_total_price(self):
    """Рассчитывает общую стоимость позиции в корзине"""
    return self.product.price * self.quantity
    
def __str__(self):
    return f"{self.quantity}x {self.product.name} (${self.get_total_price()})"
