from django.db import models
class Facultad(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)


    class Meta:
        db_table = 'Facultad'

    def __str__(self):
        return self.descripcion

class Materia(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField(max_length=100, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    facultad_id = models.ForeignKey('Facultad', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'materia'

class Fuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255, null=False)
    resumen = models.TextField()
    fecha_publicacion = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # TODO tipo = models.ForeignKey('TipoFuente', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'fuente'

class MateriaFuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    materia_id = models.ForeignKey('Materia', on_delete=models.CASCADE)
    fuente_id = models.ForeignKey('Fuente', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'materia_fuente'
