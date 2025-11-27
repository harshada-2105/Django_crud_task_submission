from django.urls import path
from .views import *

urlpatterns = [
    path("TicketCreate/", TicketCreate.as_view(), name="TicketCreate"),
    path("<int:pk>/TicketDelete/", TicketDelete.as_view(), name="TicketDelete"),
    path("TicketList/", TicketList.as_view(), name="TicketList"),
    path("<int:pk>/TicketUpdate/", TicketUpdate.as_view(), name="TicketUpdate"),
]