from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
# Create your models here.
#ManyToMany simples
class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    nome = models.CharField(max_length = 30)
    pessoa = models.ForeignKey("Pessoa", on_delete=CASCADE, related_name="carro")

    def __str__(self):
        return self.nome