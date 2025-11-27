from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("CraftList/", CraftList.as_view(), name="CraftList"),
    path("CraftCreate/", CraftCreate.as_view(), name="CraftCreate"),
    path("CraftUpdate/<int:pk>/", CraftUpdate.as_view(), name="CraftUpdate"),
    path("CraftDelete/<int:pk>/", CraftDelete.as_view(), name="CraftDelete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

