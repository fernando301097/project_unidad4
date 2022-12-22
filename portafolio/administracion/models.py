from django.db import models

class Proyecto(models.Model):
    foto = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    tags = models.CharField(max_length=100)
    url_github = models.URLField()

    def __str__(self):
        return self.titulo + " " + self.descripcion