from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import * 
from .serializers import *

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        watched = self.request.query_params.get('watched', None)
        
        if watched is not None:
            watched_bool = watched.lower() == "true"
            queryset = queryset.filter(watched = watched_bool)
        return queryset
    
    @action(detail=False, methods=['get'])
    def watched(self, request):
        watched_movie = self.get_queryset().filter(watched = True)
        serializer = self.get_serializer(watched_movie, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        pending_movie = self.get_queryset().filter(watched = False)
        serializer = self.get_serializer(pending_movie, many = True)
        return Response(serializer.data)