from django.db import models

# Create your models here.
class Cloth(models.Model):
    item_name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.FloatField()
    item_photo = models.ImageField(upload_to='cloths')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name