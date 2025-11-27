from django.contrib import admin
from .models import *

@admin.register(Library)
# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    pass