from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer.user.id} - {self.customer}".title()
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    
    class Meta:
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.cart.customer} - {self.product} - quantity: {self.quantity}"