from django.test import TestCase
from corretora.models import *


class AtivoModelTestCase(TestCase):
    def setUp(self):
        self.ativo = Ativo(
            nome='Ativo Fictício',
            tipo='F',
            preco_mercado=9.87
        )

    def test_verifica_valor_numerico_para_campo_preco_mercado(self):
        """ Teste para validar que o campo preço de mercado contenha sempre valores numéricos """
        self.assertEqual(self.ativo.preco_mercado, float('9.87'))


class MovimentacaoModelTestCase(TestCase):
    def setUp(self):
        self.movimentacao = Movimentacao(
            tipo_ativo='V',
            cliente=1,
            tipo_transacao='R',
            quantidade=10,
            valor_unitario=9.87,
            taxa_adm=1.55,
            taxa_custodia=7.44,
            total_aplicacao=1.0,
            total_investido=10.0,
            cliente_ip='1.1.1.1',
            data_aplicacao=datetime(2021, 7, 25, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
        )

    def test_verifica_formato_de_campos_data(self):
        """ Teste para validar que o data_aplicacao seja do formato tipo datetime """
        self.assertEqual(self.movimentacao.data_aplicacao, datetime(2021, 0o7, 25, 0, 0))
