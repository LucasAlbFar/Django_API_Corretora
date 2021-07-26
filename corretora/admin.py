from django.contrib import admin
from corretora.models import Ativo, Movimentacao


class Ativos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo', 'preco_mercado')
    list_display_links = ('id', 'nome', 'tipo')
    search_fields = ('nome', 'tipo',)
    list_per_page = 10
    ordering = ('nome', 'tipo',)


admin.site.register(Ativo, Ativos)


class Movimentacoes(admin.ModelAdmin):
    list_display = ('id', 'ativo', 'cliente', 'tipo_transacao', 'tipo_ativo', 'quantidade', 'total_investido',
                    'total_aplicacao', 'data_aplicacao', 'cliente_ip')
    list_display_links = ('id','ativo', 'cliente', 'tipo_transacao', 'tipo_ativo', )
    list_per_page = 20
    ordering = ('tipo_transacao','ativo', 'cliente', 'tipo_ativo', )


admin.site.register(Movimentacao, Movimentacoes)








