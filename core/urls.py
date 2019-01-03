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
    pessoaUpdate,
    veiculoUpdate,
    movRotUpdate,
    mensalistaUpdate,
    movMenUpdate,
    pessoaDelete,
)

urlpatterns = [
    path('', home, name='core_name'),
    path('pessoa_novo/', pessoaNovo, name='core_pessoaNovo'),
    path('listar_pessoas/', listaPessoas, name='core_list_pessoas'),
    path('pessoa_update/<int:id>', pessoaUpdate, name='core_pessoa_update'),
    path("pessoa_delete/<int:id>", pessoaDelete, name="core_pessoa_delete"),

    path('listar_veiculos/', listaVeiculos, name='core_list_veiculos'),
    path('veiculo_novo/', veiculoNovo, name='core_veiculoNovo'),
    path('veiculo_update/<int:id>', veiculoUpdate, name='core_veiculo_update'),

    path('lista_movimento/', movRotativoLista, name='core_list_movimento'),
    path('mov_rotativo_novo/', movRotativoNovo, name='core_rot_novo'),
    path('mov_rotativo_update/<int:id>', movRotUpdate, name="core_rot_update"),

    path('lista_mensalista/', listaMensalista, name='core_list_mensalista'),
    path('mensalista_novo/', mensalistaNovo, name='core_men_novo'),
    path('men_update/<int:id>', mensalistaUpdate, name='core_men_update'),

    path('lista_mov_mes/', movMensalista, name='core_movMes'),
    path('mov_mes_novo/', movMesNovo, name='core_mov_mes_novo'),
    path("mov_mes_update/<int:id>", movMenUpdate, name="core_mes_update")
]
