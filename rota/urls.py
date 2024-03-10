from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('rota_onibus/', include('rota_onibus.urls')),
]
