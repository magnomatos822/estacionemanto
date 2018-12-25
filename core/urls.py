from django.urls import path
from core.views import (
    home,
    listaPessoas,
    listaVeiculos,
    movRotativoLista,
    listaMensalista,
    movMensalista,
    pessoaNovo,
    veiculoNovo,
    movRotativoNovo,
    mensalistaNovo,
    movMesNovo,
)

urlpatterns = [
    path('', home, name='core_name'),
    path('pessoa_novo/', pessoaNovo , name='core_pessoaNovo'),
    path('listar_pessoas/', listaPessoas, name='core_list_pessoas'),

    path('listar_veiculos/', listaVeiculos, name='core_list_veiculos'),
    path('veiculo_novo/', veiculoNovo, name='core_veiculoNovo'),

    path('lista_movimento/', movRotativoLista, name='core_list_movimento'),
    path('mov_rotativo_novo/', movRotativoNovo, name='core_rot_novo'),

    path('lista_mensalista/', listaMensalista, name='core_list_mensalista'),
    path('mensalista_novo/', mensalistaNovo, name='core_men_novo'),
    
    path('lista_mov_mes/', movMensalista, name='core_movMes'),
    path('mov_mes_novo/', movMesNovo, name='core_mov_mes_novo'),

]
