from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
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

class TipoDireccionViewSet(viewsets.ModelViewSet):
    queryset = TipoDireccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class MarcaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class MarcaListUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class TipoCombustibleListCreateAPIView(generics.ListCreateAPIView):
    queryset = TipoCombustible.objects.all()
    serializer_class = TipoCombustibleSerializer

class TipoCombustibleListUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoCombustible.objects.all()
    serializer_class = TipoCombustibleSerializer


class TipoTransmisionListCreateAPIView(generics.ListCreateAPIView):
    queryset = TipoTransmision.objects.all()
    serializer_class = TipoTransmisionSerializer

class TipoTransmisionListUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoTransmision.objects.all()
    serializer_class = TipoTransmisionSerializer
