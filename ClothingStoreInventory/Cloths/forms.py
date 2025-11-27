from django import forms
from .models import *

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ["item_name", "size", "color", "price", "item_photo"]
        