from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "why_to_read", "status"]