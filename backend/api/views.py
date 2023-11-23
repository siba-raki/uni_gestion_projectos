from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Facultad
from .serializers import FacultadSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

    @action(detail=True, methods=['put'])
    def update_facultad(self, request, pk=None):
        facultad = self.get_object()
        serializer = FacultadSerializer(facultad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_facultad(self, request, pk=None):
        facultad = self.get_object()
        facultad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
