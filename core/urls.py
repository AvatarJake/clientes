from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   # path('api/clientes/', include('apps.cliente.urls')),
    path('clientes/', include('apps.cliente.urls')),
    path('admin/', admin.site.urls),
    
    
]