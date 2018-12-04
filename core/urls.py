from django.urls import path
from core.views import home, listaPessoas, listaVeiculos

urlpatterns = [
    path('',home, name='core_name'),
    path('listar_pessoas/', listaPessoas, name='core_lista_pessoas'),
    path('listar_veiculos/', listaVeiculos, name='core_lista_veiculos'),

]
