from django.db import models


# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class StorageProduct(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('storage', 'product')
        
    def __str__(self):
        return f"{self.storage} - {self.product} - {self.quantity}"

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name