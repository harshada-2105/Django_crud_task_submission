from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializer  import *
 
# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    