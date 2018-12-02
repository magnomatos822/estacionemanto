from django.urls import path, include
from core.views import home, listaPessoas

urlpatterns = [
    path('',home ),
    path('listar_pessoas', listaPessoas)

]
