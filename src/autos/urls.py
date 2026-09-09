from django.urls import path
from .views import autos, autos_detail, MarcaListCreateAPIView, TipoCombustibleListCreateAPIView, TipoTransmisionListCreateAPIView

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    path('autos/<int:pk>/', autos_detail, name='autos_detail_api'),
    path('marcas/', MarcaListCreateAPIView.as_view(), name='marca_list_create_api'),
    path('tipos_combustible/', TipoCombustibleListCreateAPIView.as_view(), name='tipo_combustible_list_create_api'),
    path('tipos_transmision/', TipoTransmisionListCreateAPIView.as_view(), name='tipo_transmision_list_create_api'),

]