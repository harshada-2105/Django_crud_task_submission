from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

# Create your views here.
class ClothList(ListView):
    model = Cloth
    template_name = "cloth/cloth_list.html"
    context_object_name = "cloths"
    
class ClothCreate(CreateView):
    model = Cloth
    template_name = "cloth/cloth_create.html"
    form_class = ClothForm
    success_url = reverse_lazy("ClothList")
    
class ClothDelete(DeleteView):
    model = Cloth
    template_name = "cloth/cloth_delete.html"
    success_url = reverse_lazy("ClothList")
    
class ClothUpdate(UpdateView):
    model = Cloth
    template_name = "cloth/cloth_create.html"
    form_class = ClothForm
    success_url = reverse_lazy("ClothList")