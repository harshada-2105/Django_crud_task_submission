from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ticket
from .forms import TicketForm

class TicketList(ListView):
    model = Ticket
    template_name = "ticket/ticket_list.html"
    context_object_name = "tickets"  # use 'tickets' in template

class TicketCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket/ticket_create.html"
    success_url = reverse_lazy("TicketList")  # redirect to list after submit

class TicketUpdate(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket/ticket_create.html"
    success_url = reverse_lazy("TicketList")  # redirect to list after update

class TicketDelete(DeleteView):
    model = Ticket
    template_name = "ticket/ticket_delete.html"
    success_url = reverse_lazy("TicketList")  # redirect to list after deletes