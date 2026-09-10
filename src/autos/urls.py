from django.urls import path
from .views import (
    autos,
    autos_detail,
    MarcaListCreateAPIView,
    MarcaListUpdateDestroyAPIView,
    TipoCombustibleListCreateAPIView,
    TipoCombustibleListUpdateDestroyAPIView,
    TipoTransmisionListCreateAPIView,
    TipoTransmisionListUpdateDestroyAPIView,
)

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    path('autos/<int:pk>/', autos_detail, name='autos_detail_api'),
    path('marcas/', MarcaListCreateAPIView.as_view(), name='marca_list_create_api'),
    path('marcas/<int:pk>/', MarcaListUpdateDestroyAPIView.as_view(), name='marca_detail_api'),
    path('tipos_combustible/', TipoCombustibleListCreateAPIView.as_view(), name='tipo_combustible_list_create_api'),
    path('tipos_combustible/<int:pk>/', TipoCombustibleListUpdateDestroyAPIView.as_view(), name='tipo_combustible_detail_api'),
    path('tipos_transmision/', TipoTransmisionListCreateAPIView.as_view(), name='tipo_transmision_list_create_api'),
    path('tipos_transmision/<int:pk>/', TipoTransmisionListUpdateDestroyAPIView.as_view(), name='tipo_transmision_detail_api'),
]