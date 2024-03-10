from django.urls import path
from .views import rota_onibus

urlpatterns = [
    path('', rota_onibus, name='rota_onibus'),
]
