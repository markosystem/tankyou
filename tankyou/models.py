from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

TIPO_VEICULO = (
    (1, 'Carro Passeio'),
    (2, 'Motocicleta'),
    (3, 'Van'),
    (4, 'Ônibus')
)

TIPO_COMBUSTIVEL = (
    (1, 'Gasolina'),
    (2, 'Álcool')
)
NIVEL_ROTACAO = (
    (1, 'Baixa'),
    (2, 'Média'),
    (3, 'Alta')
)


class Marca(models.Model):
    nome = models.CharField("Nome da Marca", max_length=100)

    tipo_veiculo = models.IntegerField("Tipo do Veículo", choices=TIPO_VEICULO)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField("Nome do Modelo", max_length=100)

    cilindrada = models.IntegerField("Total de Cilindros")

    ano = models.IntegerField("Ano do Modelo")

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField("Número da Placa", max_length=7)

    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo.nome + ' (' + self.placa + ')'


class Lancamento(models.Model):
    km_inicial = models.DecimalField(
        "Km Inicial", max_digits=6, decimal_places=1)

    km_final = models.DecimalField(
        "Km Final", max_digits=6, decimal_places=1, null=True, blank=True)

    data_fechamento = models.DateField(
        "Data de Fechamento", null=True, blank=True)

    valor_por_litro = MoneyField("Valor por Litro", max_digits=14,
                                 decimal_places=2, default_currency='BRL')

    valor_total = MoneyField("Valor Total", max_digits=14,
                             decimal_places=2, default_currency='BRL')

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    nivel_rotacao = models.IntegerField(
        "Nível de Rotação", choices=NIVEL_ROTACAO)

    tipo_combustivel = models.IntegerField(
        "Tipo do Combustível", choices=TIPO_COMBUSTIVEL)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.valor_total)
