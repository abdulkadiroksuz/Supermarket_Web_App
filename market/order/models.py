from django.db import models


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    total_price = models.IntegerField()
    address = models.ForeignKey('user.Adress' , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order ID: {self.pk} - Customer: {self.customer}"
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    
    class Meta:
        unique_together = ('order', 'product')
    
    def row_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.order} - Product: {self.product.name} - Quantity: {self.quantity}"