from django.contrib import admin
from django.urls import path, include
from artistas.api import api as artistas_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('artigos/', include('artigos.urls')),
    path('accounts/', include('allauth.urls')),
    path("api/", artistas_api.urls),
    
]
