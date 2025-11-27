from django.db import models
import datetime

# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=[('Active','Active'),('Inactive','Inactive'),('Maintenance','Maintenance')])
    location = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    installation_date = models.DateField(default = datetime.date.today)
    last_maintenance = models.DateField(blank=True, null=True)	
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title