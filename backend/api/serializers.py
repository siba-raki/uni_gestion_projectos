from rest_framework import serializers
from .models import Facultad, Materia, Fuente, MateriaFuente

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    facultad_nombre = serializers.ReadOnlyField(source='facultad_id.descripcion')
    class Meta:
        model = Materia
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el serializador

class FuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuente
        fields = '__all__'

class MateriaFuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaFuente
        fields = '__all__'
