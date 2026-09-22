from django.urls import include, path
from .views import autos, autos_detail
from .routers import router

urlpatterns = [
    path('autos/', autos, name='autos_api'),
    path('autos/<int:pk>/', autos_detail, name='autos_detail_api'),
    path('', include(router.urls)),
]