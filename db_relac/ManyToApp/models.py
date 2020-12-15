from django.db import models

from django.db.models import CASCADE

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    pessoas = models.ManyToManyField("Pessoa", related_name="filmes")

    def __str__(self):
        return self.nome

class Programador(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length = 100)
    programadores = models.ManyToManyField(Programador, related_name="linguagens", through = "ProgramadorLinguagem")

    def __str__(self):
        return self.nome

class ProgramadorLinguagem(models.Model):
    programador = models.ForeignKey(Programador, on_delete=CASCADE, related_name="programador_linguagem")
    linguagem = models.ForeignKey(Linguagem, on_delete=CASCADE, related_name="programador_linguagem")

    nivel_conhecimento = models.IntegerField()

    def __str__(self):
        return "{} - {} ({})".format(self.programador.nome, self.linguagem.nome, self.nivel_conhecimento)


