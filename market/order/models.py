from django.db import models

# Create your models here.
class Order(models.Model):
    customer_id = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending')
    total_price = models.IntegerField()
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_id.name} - {self.id}"
    
class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('order_id', 'product_id')
    
    def __str__(self):
        return f"{self.order} - {self.product.name} - {self.quantity}"