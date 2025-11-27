from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
class ContactList(ListView):
    model = Contact
    template_name = "contact/contact_list.html"
    context_object_name ="contacts"
    
class ContactCreate(CreateView):
    model = Contact
    template_name = "contact/contact_create.html"
    context_object_name = "contact"
    form_class = ContactForm
    success_url = reverse_lazy("ContactList")
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class ContactDelete(DeleteView):
    model = Contact
    template_name = "contact/contact_delete.html"
    success_url = reverse_lazy("ContactList")
    
class ContactUpdate(UpdateView):
    model = Contact
    template_name = "contact/contact_create.html" 
    form_class = ContactForm
    success_url = reverse_lazy("ContactList")
    