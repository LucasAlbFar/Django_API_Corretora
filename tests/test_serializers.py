from django.test import TestCase
from corretora.serializer import *


class AtivoSerializerTestCase(TestCase):
    def setUp(self):
        self.ativo = Ativo(
            nome='Ativo Fictício',
            tipo='F',
            preco_mercado=9.87
        )
        self.serialized = AtivoSerializer(instance=self.ativo)

    def test_verifica_campos_serializados(self):
        """ Teste que verifica os campos que estão sendo serializados """
        data = self.serialized.data
        self.assertEqual(set(data.keys()), {'id', 'nome', 'tipo', 'preco_mercado'})

    def test_verifica_conteudo_ativo_serializado(self):
        """ Teste para validar que os campos serializados são os mesmo indentificados na função setUP """
        data = self.serialized.data
        self.assertEqual(data['nome'], self.ativo.nome)
        self.assertEqual(data['tipo'], self.ativo.tipo)
        self.assertEqual(data['preco_mercado'], self.ativo.preco_mercado)


class MovimentacaoSerializerTestCase(TestCase):
    def setUp(self):
        self.movimentacao = Movimentacao(
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
            data_aplicacao=datetime(2021, 7, 25, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
        )
        self.serialized = MovimentacaoSerializer(instance=self.movimentacao)

    def test_verifica_campos_serializados(self):
        """ Teste para verificar os campos que estão sendo serializados """
        data = self.serialized.data
        self.assertEqual(set(data.keys()), {'id', 'tipo_ativo', 'taxa_custodia', 'data_aplicacao', 'valor_unitario',
                                            'taxa_adm', 'total_investido', 'quantidade', 'cliente_ip',
                                            'total_aplicacao', 'tipo_transacao', 'cliente', 'ativo'})

    def test_verifica_conteudo_movimentacao_serializado(self):
        """ Teste para validar que os campos serializados são os mesmos identificados na função setUP """
        data = self.serialized.data
        self.assertEqual(data['tipo_ativo'], self.movimentacao.tipo_ativo)
        self.assertEqual(data['cliente'], self.movimentacao.cliente)
        self.assertEqual(data['tipo_transacao'], self.movimentacao.tipo_transacao)
        self.assertEqual(data['quantidade'], self.movimentacao.quantidade)
        self.assertEqual(data['valor_unitario'], self.movimentacao.valor_unitario)
        self.assertEqual(data['taxa_adm'], self.movimentacao.taxa_adm)
        self.assertEqual(data['taxa_custodia'], self.movimentacao.taxa_custodia)
        self.assertEqual(data['total_aplicacao'], self.movimentacao.total_aplicacao)
        self.assertEqual(data['total_investido'], self.movimentacao.total_investido)
        self.assertEqual(data['cliente_ip'], self.movimentacao.cliente_ip)
