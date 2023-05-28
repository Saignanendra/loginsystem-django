from django.contrib import admin
from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', home, name="home")


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
