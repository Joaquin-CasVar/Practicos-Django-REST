from rest_framework import serializers
from .models import Auto, TipoDireccion, Color

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDireccion
        fields = '__all__'
        read_only_fields = ['id']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        read_only_fields = ['id']

class AutoPublicSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Auto
        fields = [
            'id',
            'nombre',
            'anio',
            'nuevo',
            'kilometros',
            'color',
            'marca',
        ]
        read_only_fields = ['id', 'activo']


class AutoSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=True)
    direccion = DireccionSerializer(read_only=True)

    class Meta:
        model = Auto
        fields = '__all__'
        read_only_fields = ['id', 'activo']
