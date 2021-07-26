from django.db import models
from datetime import datetime


class Ativo(models.Model):
    TIPO = (
        ('F', 'Fixa'),
        ('V', 'Variável'),
        ('C', 'Cripto')
    )
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)
    preco_mercado = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    TIPO_TRANSACAO = (
        ('A', 'Aplicação'),
        ('R', 'Resgate')
    )

    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    cliente = models.IntegerField()
    tipo_transacao = models.CharField(max_length=1, choices=TIPO_TRANSACAO, blank=False, null=False, default='A')
    quantidade = models.FloatField(blank=False, null=False)
    valor_unitario = models.FloatField(blank=False, null=False)
    taxa_adm = models.FloatField(blank=False, null=False)
    taxa_custodia = models.FloatField(blank=False, null=False)
    total_aplicacao = models.FloatField(null=True)
    total_investido = models.FloatField(null=True)
    tipo_ativo = models.CharField(max_length=1, blank=False, null=False)
    cliente_ip = models.GenericIPAddressField(null=True)
    data_aplicacao = models.DateTimeField(default=datetime.now, blank=True)











