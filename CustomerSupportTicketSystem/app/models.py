from django.db import models

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=[("Open", "Open"), ("In Progress", "In Progress"), ("Closed", "Closed")], default="Open")
    priority = models.CharField(max_length=255, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], default="High")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title