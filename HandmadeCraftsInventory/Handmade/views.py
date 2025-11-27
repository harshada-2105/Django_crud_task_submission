from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
class CraftList(ListView):
    model = Craft
    template_name = "craft/craft_list.html"
    context_object_name = "crafts"
    
class CraftCreate(CreateView):
    model = Craft
    template_name = "craft/craft_create.html"
    form_class = CraftForm
    success_url = reverse_lazy("CraftList")
    
class CraftUpdate(UpdateView):
    model = Craft
    template_name = "craft/craft_create.html"
    form_class = CraftForm
    success_url = reverse_lazy("CraftList")
    
class CraftDelete(DeleteView):
    model = Craft
    template_name = "craft/craft_delete.html"
    success_url = reverse_lazy("CraftList")