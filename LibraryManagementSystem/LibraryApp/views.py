from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializer import *

# Create your views here.
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer