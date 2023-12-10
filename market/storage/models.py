from django.db import models
from django.core.validators import MinValueValidator
from item.models import Product
from core.models import Company
# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Storage(models.Model):
    company = models.ForeignKey(Company, default=1 ,on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.company.name} - {self.area}"
    
class StorageProduct(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=100, validators=[MinValueValidator(0)])
    
    class Meta:
        unique_together = ('storage', 'product')
        
    def __str__(self):
        return f"{self.storage} - {self.product} - {self.quantity}"
