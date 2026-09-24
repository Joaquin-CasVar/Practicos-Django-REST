from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Auto, Color, Marca, TipoCombustible, TipoDireccion, TipoTransmision
from .serializers import (
    AutoSerializer, 
    AutoPublicSerializer,
    ColorSerializer,
    MarcaSerializer,
    TipoCombustibleSerializer,
    DireccionSerializer,
    TipoTransmisionSerializer
)
from .permissions import IsStaffOrReadOnly

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AutoPublicSerializer
        else:
            return AutoSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsStaffOrReadOnly]

class TipoCombustibleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoCombustible.objects.all()
    serializer_class = TipoCombustibleSerializer

class TipoDireccionViewSet(viewsets.ModelViewSet):
    queryset = TipoDireccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TipoTransmisionViewSet(viewsets.ModelViewSet):
    queryset = TipoTransmision.objects.all()
    serializer_class = TipoTransmisionSerializer
    permission_classes = [IsStaffOrReadOnly]
