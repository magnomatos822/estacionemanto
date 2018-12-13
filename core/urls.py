from django.urls import path
from core.views import (
    home, 
    listaPessoas, 
    listaVeiculos, 
    movRotativoLista,
    listaMensalista,
)

urlpatterns = [
    path('',home, name='core_name'),
    path('listar_pessoas/', listaPessoas, name='core_lista_pessoas'),
    path('listar_veiculos/', listaVeiculos, name='core_lista_veiculos'),
    path('lista_movimento/', movRotativoLista, name='core_lista_movimento'),
    path('lista_mensalista/', listaMensalista, name='core_lista_mensalista'),

]
