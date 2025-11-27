from django.contrib import admin
from .models import *

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'desfription', 'completed','created_at','updated_at')
    list_filter =  ('created_at','updated_at')
    search_fields = ('title','description')