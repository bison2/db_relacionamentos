from django.db import models

from django.db.models import CASCADE

# Create your models here.
#ManyToMany simples
class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    pessoas = models.ManyToManyField("Pessoa", related_name="filmes")

    def __str__(self):
        return self.nome

#ManyToMany usando uma nova tabela que tem novos campos

class Programador(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length = 100)
    programadores = models.ManyToManyField("Programador", related_name="linguagens", through = "ProgramadorLinguagem")

    def __str__(self):
        return self.nome

class ProgramadorLinguagem(models.Model):
    programador = models.ForeignKey("Programador", on_delete=CASCADE, related_name="programador_linguagem")
    linguagem = models.ForeignKey("Linguagem", on_delete=CASCADE, related_name="programador_linguagem")

    nivel_conhecimento = models.IntegerField()

    def __str__(self):
        return "{} - {} ({})".format(self.programador.nome, self.linguagem.nome, self.nivel_conhecimento)

#OneToOne: o relacionamento fica na classe que não exist sem a outra

class DocumentoCpf(models.Model):
    numero = models.CharField(max_length = 20)
    pessoa = models.OneToOneField("Pessoa")

#OneToMany usa a ForeignKey no lado do "muitos" no relacionamento

class Carro(models.Model):
    nome = models.CharField(max_length = 30)
    pessoa = models.ForeignKey("Pessoa")
    