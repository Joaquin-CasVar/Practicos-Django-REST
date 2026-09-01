from django.urls import path

from .views import autos

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    # path('autos/<int:pk>/', ..., name='autos_detail_api'),
]