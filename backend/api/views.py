from rest_framework import viewsets
from .models import Facultad, Materia, Fuente, MateriaFuente, Persona, Autor, Usuario, Cargo, TipoFuente, AutorFuente
from .serializers import FacultadSerializer, MateriaSerializer, FuenteSerializer, MateriaFuenteSerializer, PersonaSerializer, AutorSerializer, UsuarioSerializer, CargoSerializer, TipoFuenteSerializer, AutorFuenteSerializer
class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class FuenteViewSet(viewsets.ModelViewSet):
    queryset = Fuente.objects.all()
    serializer_class = FuenteSerializer

class TipoFuenteViewSet(viewsets.ModelViewSet):
    queryset = TipoFuente.objects.all()
    serializer_class = TipoFuenteSerializer


class MateriaFuenteViewSet(viewsets.ModelViewSet):
    queryset = MateriaFuente.objects.all()
    serializer_class = MateriaFuenteSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class AutorFuenteViewSet(viewsets.ModelViewSet):
    queryset = AutorFuente.objects.all()
    serializer_class = AutorFuenteSerializer
