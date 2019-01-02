from django.forms import ModelForm
from .models import (Pessoa, Veiculo, Movimento, Mensalista, MovMensalista)


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


class MovRotativoForm(ModelForm):
    """Form definition for MovRotativo."""

    class Meta:
        """Meta definition for MovRotativoform."""

        model = Movimento
        fields = ('__all__')


class MensalistaForm(ModelForm):
    """Form definition for Mensalista."""

    class Meta:
        """Meta definition for Mensalistaform."""

        model = Mensalista
        fields = ('__all__')


class MovMesForm(ModelForm):
    """Form definition for MovMes."""

    class Meta:
        """Meta definition for MovMesform."""

        model = MovMensalista
        fields = ('__all__')
