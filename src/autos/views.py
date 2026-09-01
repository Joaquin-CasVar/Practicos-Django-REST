from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .models import Auto
from .serializers import AutoSerializer

@api_view(['GET', 'POST'])
def autos(request):
    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Auto creado'}, status=status.HTTP_201_CREATED)

        return Response({'mensaje': 'Datos invalidos'}, status=status.HTTP_400_BAD_REQUEST)

