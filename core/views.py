from django.shortcuts import render
from django.http import HttpResponse
from core.models import Pessoa

def home(request):
    
    return render(request, 'core_templates/index.html')

def listaPessoas(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'core_templates/listar_pessoas.html', {'pessoa':pessoa})

