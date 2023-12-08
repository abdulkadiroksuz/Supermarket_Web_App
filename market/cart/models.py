from django.db import models


# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer.name} - {self.id}"
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.cart} - {self.product} - {self.quantity}"