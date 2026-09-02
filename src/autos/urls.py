from django.urls import path
from .views import autos, autos_detail

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    path('autos/<int:pk>/', autos_detail, name='autos_detail_api'),
]