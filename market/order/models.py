from django.db import models


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    total_price = models.IntegerField()
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.user.id} - {self.customer}".title()
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('order', 'product')
    
    def __str__(self):
        return f"{self.order} - {self.product.name} - {self.quantity}"