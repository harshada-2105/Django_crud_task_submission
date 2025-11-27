from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["firstname", "lastname", "phone", "email", "address", "date_of_birth", "company_name", "job_title", "notes", "is_favourite"]
        
        