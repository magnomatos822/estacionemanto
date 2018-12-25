from django.forms import ModelForm
from .models import (Pessoa,
                     Veiculo)


class PessoaForm(ModelForm):
    """Form definition for Pessoa."""

    class Meta:
        """Meta definition for Pessoaform."""

        model = Pessoa
        fields = ('__all__')


class VeiculoForm(ModelForm):
    """Form definition for Veiculo."""

    class Meta:
        """Meta definition for Veiculoform."""

        model = Veiculo
        fields = ('__all__')
