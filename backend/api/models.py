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
        db_table = 'Materia'

class Fuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255, null=False)
    resumen = models.TextField()
    fecha_publicacion = models.DateTimeField()
    tipo_id = models.ForeignKey('TipoFuente', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'Fuente'

class TipoFuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'TipoFuente'


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'Persona'

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    biografia = models.CharField(max_length=255, null=False)
    persona_id = models.ForeignKey('Persona', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'Autor'

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=255, null=False)
    valor_documento = models.CharField(max_length=255, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    persona_id = models.ForeignKey('Persona', on_delete=models.CASCADE)
    facultad_id = models.ForeignKey('Facultad', on_delete=models.CASCADE)
    cargo_id = models.ForeignKey('Cargo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Usuario'


class Cargo(models.Model):
    id = models.BigAutoField(primary_key=True)
    detalle = models.CharField(max_length=255, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cargo'

class MateriaFuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    materia_id = models.ForeignKey('Materia', on_delete=models.CASCADE)
    fuente_id = models.ForeignKey('Fuente', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'materia_fuente'


class AutorFuente(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor_id = models.ForeignKey('Autor', on_delete=models.CASCADE)
    fuente_id = models.ForeignKey('Fuente', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'autor_fuente'
