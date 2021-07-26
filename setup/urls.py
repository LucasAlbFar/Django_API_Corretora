from django.contrib import admin
from django.urls import path, include
from corretora.views import AtivosViewSets, MovimentacoesViewSets, \
    ConsultaSaldoViewSets, ConsultaAplicacoesViewSets, ConsultaCarteiraViewSets
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Corretora Noob",
      default_version='v1',
      description="Simula uma corretora com cadastro de investimentos e compra/venda de ativos",
      terms_of_service="#",
      contact=openapi.Contact(email="lucasalbfar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('ativos', AtivosViewSets, basename='ativos')
router.register('movimentacoes', MovimentacoesViewSets, basename='movimentacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('saldo/', ConsultaSaldoViewSets.as_view(), name='saldo'),
    path('carteira/', ConsultaCarteiraViewSets.as_view(), name='carteira'),
    path('tipo/<str:tipo>/', ConsultaAplicacoesViewSets.as_view(), name='tipo'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
