from django.db import models
from .models import *

class noticias(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)

    class meta:
        verbose_name_plural = "noticias"

    def __str__(self):
        return self.titulo
