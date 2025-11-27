from django.db import models

# Create your models here
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"