from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultadViewSet, MateriaViewSet, FuenteViewSet, MateriaFuenteViewSet, PersonaViewSet, AutorViewSet, UsuarioViewSet, CargoViewSet, TipoFuenteViewSet, AutorFuenteViewSet

router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'fuentes', FuenteViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'materia_fuentes', MateriaFuenteViewSet)
router.register(r'tipo_fuentes', TipoFuenteViewSet)
router.register(r'autor_fuentes', AutorFuenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
