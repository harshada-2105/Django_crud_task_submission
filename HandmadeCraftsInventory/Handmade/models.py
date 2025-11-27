from django.db import models

# Create your models here.
class Craft(models.Model):
    craft_name = models.CharField(max_length=255)
    craft_image = models.ImageField(upload_to="crafts")
    material_used = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    craft_description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.craft_name