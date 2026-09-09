from django.urls import path
from .views import (
    autos, 
    autos_detail, 
    TipoDireccionListCreateAPIView, 
    TipoDireccionDetailAPIView,
    ColorListCreateAPIView,
    ColorDetailAPIView
)

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    path('autos/<int:pk>/', autos_detail, name='autos_detail_api'),
    path('direcciones/', TipoDireccionListCreateAPIView.as_view(), name='tipo_direccion_api'),
    path('direcciones/<int:pk>', TipoDireccionDetailAPIView.as_view(), name='tipo_direccion_detail_api'),
    path('colores/', ColorListCreateAPIView.as_view(), name='color_api'),
    path('colores/<int:pk>', ColorDetailAPIView.as_view(), name='color_detail_api'),
]