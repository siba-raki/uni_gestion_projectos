from django.db import models

class Facultad(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)


    class Meta:
        db_table = 'Facultad'

    def __str__(self):
        return self.descripcion
