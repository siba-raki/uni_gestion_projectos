from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultadViewSet

router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
