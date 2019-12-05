from django.db import models

class TipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.descripcion


class Usuario(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id_user = models.CharField(max_length = 100, blank = False, unique = True)
    password = models.CharField(max_length = 100, blank = False)
    id_tipouser = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE, null= True)
    def __str__(self):
        return self.id_user

class Inventario(models.Model):
    codigo = models.CharField(max_length = 100, blank = False, unique = True)
    denominacion = models.CharField(max_length = 100, blank = False)
    marca = models.CharField(max_length = 100, blank = False)
    modelo = models.CharField(max_length = 100, blank = False)
    tipo = models.CharField(max_length = 100, blank = False)
    color = models.CharField(max_length = 100, blank = False)
    serie = models.CharField(max_length = 100, blank = False)
    e = models.CharField(max_length = 100, blank = False)
    id_inventario = models.CharField(max_length = 100, blank = False)
    filename = models.CharField(max_length=100, blank = False, null=True)

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

class ImgUpload(models.Model):
    filename = models.CharField(max_length=200, blank=False)
    picture = models.ImageField(upload_to="photos", null=True, blank=True)

