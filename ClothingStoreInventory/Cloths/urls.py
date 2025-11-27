from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("ClothCreate/", ClothCreate.as_view(), name="ClothCreate"),
    path("ClothDelete/<int:pk>/", ClothDelete.as_view(), name="ClothDelete"),
    path("ClothList/", ClothList.as_view(), name="ClothList"),
    path("ClothUpdate/<int:pk>/", ClothUpdate.as_view(), name="ClothUpdate")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)