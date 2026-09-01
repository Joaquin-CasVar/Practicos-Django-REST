from django.contrib import admin

from .models import Auto,Color,Marca,TipoCombustible,TipoDireccion,TipoTransmision
# Register your models here.
admin.site.register(Auto)
admin.site.register(Color)
admin.site.register(Marca)
admin.site.register(TipoCombustible)
admin.site.register(TipoDireccion)
admin.site.register(TipoTransmision)