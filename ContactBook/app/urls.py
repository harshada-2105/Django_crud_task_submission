from django.urls import path
from .views import *

urlpatterns = [
    path("ContactCreate/", ContactCreate.as_view(), name = "ContactCreate"),
    path("ContactList/", ContactList.as_view(), name = "ContactList"),
    path("<int:pk>/ContactDelete/", ContactDelete.as_view(), name = "contact_delete"),
    path("<int:pk>/ContactUpdate/", ContactUpdate.as_view(), name = "contact_edit")
]