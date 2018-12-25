# from django.http import HttpResponse
from django.shortcuts import (render,
                              redirect)
from .models import (Mensalista,
                     MovMensalista,
                     Movimento,
                     Pessoa,
                     Veiculo)

from .forms import (PessoaForm,
                    VeiculoForm)


def home(request):
    return render(request, 'core_templates/index.html')


def listaPessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core_templates/listar_pessoas.html', data)


def pessoaNovo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_list_pessoas')


def listaVeiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form':form}
    return render(request, 'core_templates/listar_veiculos.html', data)


def veiculoNovo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    return redirect('core_list_veiculos')


def movRotativoLista(request):
    movimentos = Movimento.objects.all()
    return render(request, 'core_templates/listar_movimento.html', {'movimentos': movimentos})


def listaMensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core_templates/listar_mensalista.html', {'mensalistas': mensalistas})


def movMensalista(request):
    movimentoMensalista = MovMensalista.objects.all()
    return render(request, 'core_templates/listar_movmensalista.html',
                  {'movMensalista': movimentoMensalista})
