from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultadViewSet, MateriaViewSet, FuenteViewSet, MateriaFuenteViewSet

router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'fuentes', FuenteViewSet)
router.register(r'materiasfuentes', MateriaFuenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
