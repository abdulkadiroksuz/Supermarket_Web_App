from django.db import models

# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    area_id = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class StorageProduct(models.Model):
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product_id = models.ForeignKey('item.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('storage_id', 'product_id')
        
    def __str__(self):
        return f"{self.storage_id} - {self.product_id} - {self.quantity}"

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name