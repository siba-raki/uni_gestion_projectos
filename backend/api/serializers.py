from rest_framework import serializers
from .models import Facultad, Materia, Fuente, TipoFuente, MateriaFuente, Persona, Autor, Usuario, Cargo, AutorFuente

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
    tipo_fuente_descripcion = serializers.ReadOnlyField(source='tipo_id.descripcion')
    class Meta:
        model = Fuente
        fields = '__all__'

class TipoFuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFuente
        fields = '__all__'

class MateriaFuenteSerializer(serializers.ModelSerializer):
    materia_nombre = serializers.ReadOnlyField(source='materia_id.descripcion')
    fuente_nombre = serializers.ReadOnlyField(source='fuente_id.titulo')

    class Meta:
        model = MateriaFuente
        fields = '__all__'

class AutorFuenteSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.ReadOnlyField(source='autor_id.persona_id.nombre')
    autor_apellido = serializers.ReadOnlyField(source='autor_id.persona_id.apellido')
    fuente_nombre = serializers.ReadOnlyField(source='fuente_id.titulo')

    class Meta:
        model = AutorFuente
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    persona_nombre = serializers.ReadOnlyField(source='persona_id.nombre')
    persona_apellido = serializers.ReadOnlyField(source='persona_id.apellido')
    class Meta:
        model = Autor
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    facultad_nombre = serializers.ReadOnlyField(source='facultad_id.descripcion')
    cargo_tipo = serializers.ReadOnlyField(source='cargo_id.detalle')
    persona_nombre = serializers.ReadOnlyField(source='persona_id.nombre')
    persona_apellido = serializers.ReadOnlyField(source='persona_id.apellido')
    class Meta:
        model = Usuario
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
