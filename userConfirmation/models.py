from django.db import models


class Usuario(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id_user = models.CharField(max_length = 100, blank = False, unique = True)
    password = models.CharField(max_length = 100, blank = False)


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


class ImgUpload(models.Model):
    filename = models.CharField(max_length=200, blank=False)
    picture = models.ImageField(upload_to="photos", null=True, blank=True)

