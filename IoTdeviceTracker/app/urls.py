from django.urls import path
from .views import *

urlpatterns = [
    path("device_list/", device_list, name = "device_list"),
    path("device_create/", device_create, name = "device_create"),
    path("<int:pk>/device_update/", device_update, name = "device_update"),
    path("<int:pk>/device_delete/", device_delete, name = "device_delete")
]