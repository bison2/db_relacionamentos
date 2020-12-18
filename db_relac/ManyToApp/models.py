from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.urls import reverse
# Create your models here.
#ManyToMany simples

class PessoaManager(models.Manager):

    def tudo(self):
        return self.get_queryset().order_by('nome')

    def car(self):
        return self.get_queryset().order_by('nome')

    def linguagem(self):
        return self.get_queryset().order_by('nome')

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)

    objects = PessoaManager() 

    def __str__(self):
        return self.nome





class Carro(models.Model):
    nome = models.CharField(max_length = 30)
    pessoa = models.ForeignKey("Pessoa", on_delete=CASCADE, related_name="carro")

    objects = PessoaManager()

    def __str__(self):
        return self.nome
    
class Linguagem(models.Model):
    nome = models.CharField(max_length = 100)
    pessoa = models.ManyToManyField("Pessoa", related_name="linguagem")

    objects = PessoaManager()

    def __str__(self):
        return self.nome