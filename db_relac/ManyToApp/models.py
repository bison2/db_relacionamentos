from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.urls import reverse
# Create your models here.
#ManyToMany simples

class PessoaManager(models.Manager):

    def tudo(self):
        return self.get_queryset().order_by('nome')

    def p_car(self):
        return self.get_queryset().prefetch_related('carro').all()
    

class CarroManager(models.Manager):
    
    def car(self):
        return self.get_queryset().order_by('nome')
    
class LinguagemManager(models.Manager):

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

    objects = CarroManager()

    def __str__(self):
        return self.nome
    
class Linguagem(models.Model):
    nome = models.CharField(max_length = 100)
    pessoa = models.ManyToManyField("Pessoa", related_name="linguagem")

    objects = LinguagemManager()

    def __str__(self):
        return self.nome