from django.contrib import admin
from django.urls import path
from .views import home, restapi
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', home, name="home"),
    path ("restapi/", restapi, name="restapi")


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
