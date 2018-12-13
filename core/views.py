from builtins import object
from django.http import HttpResponse
from django.shortcuts import render
from core.models import (
    Mensalista, 
    Movimento, 
    Pessoa, 
    Veiculo,
)


def home(request):
    return render(request, 'core_templates/index.html')


def listaPessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core_templates/listar_pessoas.html', {'pessoas':pessoas})


def listaVeiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core_templates/listar_veiculos.html', {'veiculos':veiculos})


def movRotativoLista(request):
    movimentos = Movimento.objects.all()
    return render(request, 'core_templates/listar_movimento.html', {'movimentos':movimentos})


def listaMensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core_templates/listar_mensalista.html', {'mensalistas': mensalistas})
