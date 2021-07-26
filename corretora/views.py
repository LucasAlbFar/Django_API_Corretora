from rest_framework import viewsets, generics, filters
from corretora.serializer import AtivoSerializer, \
    MovimentacaoSerializer, ConsultaSaldoSerializer, ConsultaCarteiraSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from corretora.functions import *


class AtivosViewSets(viewsets.ModelViewSet):
    """
    Exibir e registrar os ativos cadastrados na corretora
    """

    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer
    http_method_names = ['get', 'post', 'put', 'path']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'preco_mercado',]
    search_fields = ['nome', 'codigo', 'tipo',]


class MovimentacoesViewSets(viewsets.ModelViewSet):
    """
    Exibir e registrar as movimentções de aplicação/resgate na corretora
    """

    def get_queryset(self):
        return Movimentacao.objects.filter(cliente=self.request.user.id)

    serializer_class = MovimentacaoSerializer
    http_method_names = ['get', 'post']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ativo', 'data_aplicacao', 'total_aplicacao', 'valor_unitario',
                       'total_investido', 'tipo_transacao', 'tipo_ativo', ]
    search_fields = ['ativo', 'data_aplicacao', 'tipo_transacao', 'tipo_ativo', ]


class ConsultaSaldoViewSets(generics.ListAPIView):
    """
    Calcular o saldo na carteira de investimentos do usuário
    """

    def get_queryset(self):
        queryset = Movimentacao.objects.filter(cliente=self.request.user.id)
        return queryset

    def get(self, request, **kwargs):
        dados = calcular_saldos(request)
        results = ConsultaSaldoSerializer(dados, many=True).data
        return Response(results)

    serializer_class = ConsultaSaldoSerializer


class ConsultaCarteiraViewSets(generics.ListAPIView):
    """
    Verificar ativos na carteira de investimentos do usuário e suas quantidades
    """

    def get_queryset(self):
        queryset = Movimentacao.objects.filter(cliente=self.request.user.id)
        return queryset

    def get(self, request, **kwargs):
        dados = verificar_carteira(request)
        results = ConsultaCarteiraSerializer(dados, many=True).data
        return Response(results)

    serializer_class = ConsultaCarteiraSerializer


class ConsultaAplicacoesViewSets(generics.ListAPIView):
    """
    Listar as aplicações da corretora por tipo de aplicação
    """

    def get_queryset(self):
        queryset = Ativo.objects.filter(tipo=self.kwargs['tipo'])
        return queryset

    serializer_class = AtivoSerializer


