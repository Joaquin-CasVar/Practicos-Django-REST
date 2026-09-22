from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, TipoCombustibleViewSet, TipoTransmisionViewSet

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet, basename='marca')
router.register(r'tipos_combustible', TipoCombustibleViewSet, basename='tipo_combustible')
router.register(r'tipos_transmision', TipoTransmisionViewSet, basename='tipo_transmision')