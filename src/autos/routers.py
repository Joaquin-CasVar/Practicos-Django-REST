from rest_framework.routers import DefaultRouter

from .views import AutoViewSet, ColorViewSet, TipoDireccionViewSet

router = DefaultRouter()

router.register('autos', AutoViewSet, basename='autos-api')
router.register('colores', ColorViewSet, basename='colores-api')
router.register('tipos-direccion', TipoDireccionViewSet, basename='tipos-direccion-api')