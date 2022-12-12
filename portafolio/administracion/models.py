from django.db import models

class Proyecto(models.Model):
    foto = models.ImageField(upload_to='albums/images/')
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    tags = models.CharField(max_length=100)
    url_github = models.URLField()

    def __str__(self):
        return self.titulo + " " + self.descripcion
