from django.test import TestCase
from rest_framework import exceptions

from corretora import serializer
from corretora.serializer import *


class MovimentacaoUnitTest(TestCase):
    def setUp(self):
        self.movimentacao = Movimentacao.objects.create(
            tipo_ativo='V',
            cliente=1,
            tipo_transacao='A',
            quantidade=10,
            valor_unitario=9.87,
            taxa_adm=1.55,
            taxa_custodia=7.44,
            total_aplicacao=1.0,
            total_investido=10.0,
            cliente_ip='1.1.1.1',
            data_aplicacao=datetime(2021, 7, 25, hour=0, minute=0, second=0, microsecond=0, tzinfo=None),
            ativo=Ativo.objects.create(
                nome='Ativo Fictício',
                tipo='F',
                preco_mercado=9.87
            )
        )

    def test_tentativa_de_resgate_sem_ativos_na_carteira(self):
        """ Teste para validar função que impede um ativo ser resgatado sem que ele esteja na carteira do cliente """
        movimentacao = get_list_or_404(Movimentacao, cliente=self.movimentacao.cliente)
        data = {'ativo': self.movimentacao.ativo.id, 'quantidade': self.movimentacao.quantidade,
                'tipo': self.movimentacao.tipo_transacao}

        calcular_quantidade_ativos_disponiveis(data, movimentacao)
        assert serializer.errors == {'Quantidade': [
            exceptions.ErrorDetail(string='Ativo não disponível para resgate', code='invalid')
        ]}
