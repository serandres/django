from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)


class Enlace(models.Model):
    titulo = models.CharField(max_length = 140)
    enlace = models.URLField()
    votos = models.IntegerField(default = 0)
    categoria = models.ForeignKey(Categoria)

