from rest_framework import serializers
from .models import Auto, Marca, TipoCombustible, TipoTransmision

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


class AutoSerializer(serializers.ModelSerializer):
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    combustible_detalle = TipoCombustibleSerializer(source='combustible', read_only=True)
    transmision_detalle = TipoTransmisionSerializer(source='transmision', read_only=True)

    class Meta:
        model = Auto
        fields = [
            'id',
            'nombre',
            'anio',
            'nuevo',
            'kilometros',
            'patente',
            'puertas',
            'marchas',
            'activo',
            'marca',
            'combustible',
            'transmision',
            'direccion',
            'color',
            'marca_detalle',
            'combustible_detalle',
            'transmision_detalle',
        ]
        read_only_fields = ['id', 'activo']
