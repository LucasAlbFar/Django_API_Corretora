from corretora.validator import *
from corretora.functions import *


class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = '__all__'

    def create(self, data):
        data['nome'] = data['nome'].upper()

        return Ativo.objects.create(**data)


class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = '__all__'
        read_only_fields = ('cliente', 'cliente_ip', 'total_aplicacao', 'total_investido', 'tipo_ativo')

    def validate(self, data):
        if not valor_valido(data['quantidade']):
            raise serializers.ValidationError({'Quantidade': 'Quantidade de ativos deve conter valor maior que zero'})

        if not valor_valido(data['valor_unitario']):
            raise serializers.ValidationError({'Valor Unitário': 'Valor unitário deve ser maior que zero'})

        return data

    def create(self, data):
        recuperar_cliente(self, data)
        ativo = recuperar_ativo(data['ativo'].id)

        if tipo_aplicacao(data['tipo_transacao']):
            salvar_preco_mercado(data, ativo)
        else:
            movimentacoes = recuperar_movimentacoes(data['cliente'])
            calcular_quantidade_ativos_disponiveis(data, movimentacoes)
            data['valor_unitario'] = recuperar_preco_mercado(data['valor_unitario'], ativo)
            salvar_preco_mercado(data, ativo)

        recuperar_tipo_ativo(data, ativo)
        calcular_total_aplicacao(data)
        salvar_cliente_ip(self, data)
        salvar_datahora_aplicacao(data)

        return Movimentacao.objects.create(**data)


class ConsultaSaldoSerializer(serializers.Serializer):
    saldo_aplicacoes = serializers.FloatField()
    saldo_resgaste = serializers.FloatField()
    saldo_carteira = serializers.FloatField()


class ConsultaCarteiraSerializer(serializers.Serializer):
    carteira = serializers.DictField()
