from rest_framework import serializers
from .models import Auto

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'
        # fields = [
        #     'id',
        #     'nombre',
        #     'anio',
        #     'nuevo',
        #     'kilometros',
        #     'patente',
        #     'puertas',
        #     'marchas',
        #     'activo',
        # ]
        read_only_fields = ['id', 'activo']
