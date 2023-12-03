from rest_framework import viewsets
from .models import Facultad, Materia, Fuente, MateriaFuente
from .serializers import FacultadSerializer, MateriaSerializer, FuenteSerializer, MateriaFuenteSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class FuenteViewSet(viewsets.ModelViewSet):
    queryset = Fuente.objects.all()
    serializer_class = FuenteSerializer


class MateriaFuenteViewSet(viewsets.ModelViewSet):
    queryset = MateriaFuente.objects.all()
    serializer_class = MateriaFuenteSerializer