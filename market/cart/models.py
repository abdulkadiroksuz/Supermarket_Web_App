from django.db import models

# Create your models here.
class Cart(models.Model):
    customer_id = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer_id.name} - {self.id}"
    
class CartProduct(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('cart_id', 'product_id')
    
    def __str__(self):
        return f"{self.cart_id} - {self.product_id} - {self.quantity}"