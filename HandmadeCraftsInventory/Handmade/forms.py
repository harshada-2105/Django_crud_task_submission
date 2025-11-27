from django import forms
from .models import *

class CraftForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = ["craft_name", "craft_image", "material_used", "price", "stock", "craft_description"]