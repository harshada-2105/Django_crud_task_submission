from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
from datetime import date

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    phone = PhoneNumberField(unique = True)
    email = models.EmailField(unique = True)
    address	= models.CharField(max_length = 255)
    date_of_birth = models.DateField(default = now())
    company_name = models.CharField(max_length = 255)
    job_title = models.CharField(max_length = 255)
    notes = models.TextField(null = True, blank = True)
    is_favourite = models.BooleanField(default = False)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.fullname