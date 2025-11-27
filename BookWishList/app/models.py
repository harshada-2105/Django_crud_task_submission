from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    why_to_read = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=[("Read", "Read"), ("Reading", "Reading"), ("Completed", "Completed")], default="Reading")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title