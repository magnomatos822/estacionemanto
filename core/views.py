# from django.http import HttpResponse
from .forms import (MensalistaForm,
                    MovMesForm,
                    MovRotativoForm,
                    PessoaForm,
                    VeiculoForm)

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


def pessoaDelete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_list_pessoas')
    else:
        return render(request, 'core_templates/delete_confirm.html', 
        {'pessoa': pessoa})


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


def veiculoUpdate(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_veiculos')
    else:
        return render(request, 'core_templates/veiculo_update.html', data)


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


def movRotUpdate(request, id):
    data = {}
    movRot = Movimento.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movRot)
    data['movRot'] = movRot
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('core_list_movimento')
    else:
        return render(request, 'core_templates/mov_rot_update.html', data)


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


def mensalistaUpdate(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('core_list_mensalista')
    else:
        return render(request, 'core_templates/mensalista_update.html', data)


def movMensalista(request):
    movimentoMensalista = MovMensalista.objects.all()
    form = MovMesForm()
    data = {'movMensalista': movimentoMensalista, 'form': form}
    return render(request, 'core_templates/listar_movmensalista.html', data)


def movMesNovo(request):
    form = MovMesForm(request.POST or None)
    if form.is_valid():
        form.save()

    return redirect('core_movMes')


def movMenUpdate(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMesForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('core_movMes')
    else:
        return render(request, 'core_templates/mov_mensalista_update.html',
                      data)
