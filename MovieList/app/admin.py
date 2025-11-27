from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre', 'release_date', 'rating', 'watched')
    search_fields = ('title', 'director', 'genre')
    list_filter = ('watched', 'genre', 'release_date')
    
    