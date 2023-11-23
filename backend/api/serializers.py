from rest_framework import serializers
from .models import Facultad

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ['id', 'descripcion', 'fecha_creacion', 'fecha_modificacion', 'activo']
