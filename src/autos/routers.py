from rest_framework.routers import DefaultRouter

from .views import (
    AutoViewSet,
    ColorViewSet,
    MarcaViewSet,
    TipoCombustibleViewSet,
    TipoDireccionViewSet,
    TipoTransmisionViewSet
)
router = DefaultRouter()

router.register('autos', AutoViewSet, basename='autos-api')
router.register('colores', ColorViewSet, basename='colores-api')
router.register(r'marcas', MarcaViewSet, basename='marca-api')
router.register(r'tipos-combustible', TipoCombustibleViewSet, basename='tipo-combustible-api')
router.register('tipos-direccion', TipoDireccionViewSet, basename='tipos-direccion-api')
router.register(r'tipos-transmision', TipoTransmisionViewSet, basename='tipo-transmision-api')
