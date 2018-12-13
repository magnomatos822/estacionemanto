from django.db import models
import math

class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
       return self.nome

    class Meta:
        db_table = 'pessoas'
        managed = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Marca(models.Model):
    """Model definition for Marca."""

    marca = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Marca."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marca."""
        return self.marca


class Veiculo(models.Model):
    """Model definition for Veiculo."""

    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    obs = models.TextField()


    class Meta:
        """Meta definition for Veiculo."""

        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        """Unicode representation of Veiculo."""
        return self.nome+' - '+self.placa


class Parametro(models.Model):
    """Model definition for Parametro."""

    valorHora = models.DecimalField(max_digits=5, decimal_places=2)
    valorMes = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        """Meta definition for Parametro."""

        verbose_name = 'Parametro'
        verbose_name_plural = 'Parametros'

    def __str__(self):
        return 'Valores'


class Movimento(models.Model):
    """Model definition for Movimento."""

    chekin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pagamento = models.BooleanField(default=False)


    class Meta:
        """Meta definition for Movimento."""

        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentos'

    def __str__(self):
        """Unicode representation of Movimento."""
        return self.veiculo.placa
        
    
    def total_horas(self):
        return math.ceil((self.checkout - self.chekin).total_seconds()/3600)

    def total(self):
        return self.valor_hora * self.total_horas()

class Mensalista(models.Model):
    """Model definition for Mensalista."""

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2) 
    pago = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Mensalista."""

        verbose_name = 'Mensalista'
        verbose_name_plural = 'Mensalistas'

    def __str__(self):
        """Unicode representation of Mensalista."""
        return str(self.veiculo)+ ' - ' +str(self.inicio)


class MovMensalista(models.Model):

    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.mensalista)+' - '+str(self.dt_pgto)

    class Meta:
        verbose_name = 'MovMensalista'
        verbose_name_plural = 'MovMensalistas'
