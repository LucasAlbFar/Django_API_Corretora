from django.shortcuts import get_object_or_404, get_list_or_404
from corretora.models import Ativo, Movimentacao
from rest_framework import serializers
from datetime import datetime


def recuperar_movimentacoes(usuario: int):
    """
    Retornar lista das movimentações filtradas pelo usuário ativo
    """
    movimentacoes = get_list_or_404(Movimentacao, cliente=usuario)
    return movimentacoes


def recuperar_ativo(ativo_id: id):
    """
    Retornar objeto do modelo Ativo, selecionado através do ativo_id
    """

    ativo = get_object_or_404(Ativo, pk=ativo_id)
    return ativo


def tipo_aplicacao(aplicacao: str):
    """
    Retornar TRUE ou FALSE caso o parâmetro de entrada for igual à 'A' (aplicação)
    """
    return aplicacao == 'A'


def recuperar_cliente(self: object, data: dict):
    """
    Recuperar ID do usuário e retorna a informação para o modelo
    """

    data['cliente'] = self.context['request'].user.id
    return data


def calcular_quantidade_ativos_disponiveis(data: dict, movimentacoes: list):
    """
    Calcular a quantidade de ativos adquiridos pelo usuário;
    Retorna erro em caso do ativo não fazer parte da carteira de investimentos do cliente;
    Caso a quantidade a ser resgatada for maior que a possuída, a função retornará para o modelo
    somente a quantidade disponível para a venda.
    """

    quantidade_disponivel = 0

    for item in movimentacoes:
        if item.ativo == data['ativo']:
            if tipo_aplicacao(item.tipo_transacao):
                quantidade_disponivel = quantidade_disponivel + item.quantidade
            else:
                quantidade_disponivel = quantidade_disponivel - item.quantidade

    if quantidade_disponivel == 0:
        raise serializers.ValidationError({'Quantidade': 'Ativo não disponível para resgate'})
    else:
        if data['quantidade'] > quantidade_disponivel:
            data['quantidade'] = quantidade_disponivel

    return data


def recuperar_preco_mercado(valor_unitario: float, ativo: object):
    """
    Recupera o preço do mercado do ativo a ser aplicado ou resgatado;
    Caso o valor unitário informado no resgate for maior que o preço de mercado,
    o modelo desconsiderará do valor unitário informado no POST, e será utilizado
    o preço de mercado atual do ativo para realização do resgate
    """

    if (valor_unitario > ativo.preco_mercado) or (valor_unitario == 0.0):
        valor_unitario = ativo.preco_mercado

    return valor_unitario


def salvar_preco_mercado(data: dict, ativo: object):
    """
    Atualizar o preço de mercado do ativo no momento da aplicação
    """

    ativo.preco_mercado = data['valor_unitario']
    ativo.save()


def recuperar_tipo_ativo(data: dict, ativo: object):
    """
    Recuperar o tipo do ativo da transação
    """

    data['tipo_ativo'] = ativo.tipo
    return data


def calcular_total_aplicacao(data: dict):
    """
    Calcular o valor total da aplicação/resgate e do investivmento através do valor unitário do ativo,
    a quantidade de ativos desejados, somados às taxa de administração e taxa de custódia
    """
    data['total_investido'] = data['valor_unitario'] * data['quantidade']
    data['total_aplicacao'] = data['total_investido'] + (data['taxa_adm'] + data['taxa_custodia'])

    return data


def salvar_cliente_ip(self: object, data: dict):
    """
    Recuperar IP do usuário e retorna a informação para o modelo
    """

    data['cliente_ip'] = self.context['request'].META.get("REMOTE_ADDR", )
    return data


def salvar_datahora_aplicacao(data: dict):
    """
    Salvar data da aplicação
    """

    data['data_aplicacao'] = datetime.now()
    return data


def calcular_saldos(request: object):
    """
    Calcular os saldos de aplicação, restagate e o saldo total na carteira do usuário
    """

    movimentacoes = recuperar_movimentacoes(request.user.id)
    saldo_resgate, saldo_aplicacoes = 0, 0

    for item in movimentacoes:
        ativo = recuperar_ativo(item.ativo.id)

        if tipo_aplicacao(item.tipo_transacao):
            saldo_aplicacoes = (ativo.preco_mercado * item.quantidade) + saldo_aplicacoes
        else:
            saldo_resgate = (ativo.preco_mercado * item.quantidade) - saldo_resgate

    saldo_carteira = saldo_aplicacoes - saldo_resgate
    dados = [{'saldo_aplicacoes': saldo_aplicacoes, "saldo_resgaste": saldo_resgate,
              "saldo_carteira": saldo_carteira}]

    return dados


def verificar_carteira(request: object):
    """
    Retornar quais ativos da carteira do usuário, suas quantidades e a performance do ativo
    """

    movimentacoes = recuperar_movimentacoes(request.user.id)
    dict_carteira = {}

    for item in movimentacoes:
        if tipo_aplicacao(item.tipo_transacao):
            if not ativo_no_dicionario(item.ativo, dict_carteira):
                ativo = recuperar_ativo(item.ativo.id)
                preco_mercado = recuperar_preco_mercado(0.0, ativo)
                inserir_novo_ativo_carteira(preco_mercado, item, dict_carteira)
            else:
                atualizar_carteira(item, dict_carteira)
        else:
            if ativo_no_dicionario(item.ativo, dict_carteira):
                atualizar_carteira(item, dict_carteira)

    remover_ativos_zerados(dict_carteira)
    calcular_performance(dict_carteira)

    dados = [{'carteira': dict_carteira}]

    return dados


def atualizar_carteira(item: list, dict_carteira: dict):
    """
    Atualizar dados da requisição para visualizar a carteira de ativos do cliente
    """
    if tipo_aplicacao(item.tipo_transacao):
        dict_carteira[item.ativo]['valor_negociado'] = item.valor_unitario
        dict_carteira[item.ativo]['quantidade'] = dict_carteira[item.ativo]['quantidade'] + \
                                                  item.quantidade
    else:
        dict_carteira[item.ativo]['valor_negociado'] = item.valor_unitario
        dict_carteira[item.ativo]['quantidade'] = dict_carteira[item.ativo]['quantidade'] - \
                                                  item.quantidade
    return dict_carteira


def inserir_novo_ativo_carteira(preco_mercado: float, item: list, dict_carteira: dict):
    """
    Insere ativo na carteira, com seu preço de mercado
    """
    novo_ativo = {item.ativo: {'quantidade': item.quantidade, 'valor_negociado': item.valor_unitario,
                               'preco-mercado': preco_mercado}}

    dict_carteira.update(novo_ativo)
    return dict_carteira


def ativo_no_dicionario(ativo: str, dict_carteira: dict):
    """
    Varificar se o ativo está na carteira de investimentos do cliente
    """
    return ativo in dict_carteira


def remover_ativos_zerados(dict_carteira: dict):
    """
    Remover ativos da carteira que foram negociados
    """

    lista_keys = []
    for key, value in dict_carteira.items():
        if dict_carteira[key]['quantidade'] == 0:
            lista_keys.append(key)

    for key in lista_keys:
        del dict_carteira[key]

    return dict_carteira


def calcular_performance(dict_carteira: dict):
    """
    Avaliar performance do ativo, calculado à partir do última negociação realizada e do preço de mercado do ativo
    """

    for key, value in dict_carteira.items():
        dict_carteira[key]['performance (%)'] = round(((value['preco-mercado'] / value['valor_negociado']) - 1)
                                                      * 100, 2)
    return dict_carteira
