from django.shortcuts import render
from django.http import HttpResponse
from core.models import Pessoa, Veiculo

def home(request):
    return render(request, 'core_templates/index.html')

def listaPessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core_templates/listar_pessoas.html', {'pessoas':pessoas})

def listaVeiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core_templates/listar_veiculos.html', {'veiculos':veiculos})
