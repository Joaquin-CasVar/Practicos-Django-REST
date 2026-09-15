from rest_framework import serializers
from .models import Auto, Color, Marca, TipoCombustible, TipoDireccion, TipoTransmision

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']
        read_only_fields = ['id']

class TipoCombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCombustible
        fields = ['id', 'nombre']
        read_only_fields = ['id']

class TipoTransmisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransmision
        fields = ['id', 'nombre']
        read_only_fields = ['id']

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
    marca_detalle = MarcaSerializer(source='marca', read_only=True)

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
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    combustible_detalle = TipoCombustibleSerializer(source='combustible', read_only=True)
    direccion = DireccionSerializer(read_only=True)
    transmision_detalle = TipoTransmisionSerializer(source='transmision', read_only=True)

    class Meta:
        model = Auto
        fields = '__all__'
        read_only_fields = ['id', 'activo']
