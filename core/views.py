# from django.http import HttpResponse
from .forms import (MensalistaForm,
                    MovRotativoForm,
                    PessoaForm,
                    VeiculoForm,
                    MovMesForm)


from .models import (Mensalista,
                     MovMensalista,
                     Movimento,
                     Pessoa,
                     Veiculo)

from django.shortcuts import redirect, render


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


def pessoaUpdate(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_pessoas')
    else:
        return render(request, 'core_templates/pessoa_update.html', data)


def listaVeiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core_templates/listar_veiculos.html', data)


def veiculoNovo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_list_veiculos')


def movRotativoLista(request):
    movimentos = Movimento.objects.all()
    form = MovRotativoForm()
    data = {'movimentos': movimentos, 'form': form}
    return render(request, 'core_templates/listar_movimento.html', data)


def movRotativoNovo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_list_movimento')


def listaMensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core_templates/listar_mensalista.html', data)


def mensalistaNovo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_list_mensalista')


def movMensalista(request):
    movimentoMensalista = MovMensalista.objects.all()
    form = MovMesForm()
    data = {'movMensalista': movimentoMensalista, 'form': form}
    return render(request, 'core_templates/listar_movmensalista.html',
                  data)


def movMesNovo(request):
    form = MovMesForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_movMes')
