from django.db import models
from django import forms
# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    
    def __str__(self):
      return self.nome 

class Playlists(models.Model):
    nome_musica = models.CharField(max_length=50)
    nome_artista = models.CharField(max_length=30)
    album_musica = models.CharField(max_length=20)
    link = models.CharField(max_length=60)

    def __str__(self):
      return self.nome_musica
    

class Midia(models.Model):
    tipo = models.CharField(max_length=45)
    capa = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)

    def __str__(self):
      return self.titulo 

class Trilhas(models.Model):
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE)

    def __str__(self):
      return self.midia.titulo 

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=45)

    def __str__(self):
      return self.nome_categoria

class Musicas(models.Model):
    nome_musica = models.CharField(max_length=45)
    artista_musica = models.CharField(max_length=45)
    album_musica = models.CharField(max_length=45)  
    
    def __str__(self):
      return self.nome_musica


class Feedback_usuarios(models.Model):
    comentario = models.CharField(max_length=500)
    pontuacao = models.CharField(max_length=5)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
      return self.comentario

class Trilhas_das_musicas(models.Model):
    trilhas = models.ForeignKey(Trilhas, on_delete=models.CASCADE)
    musica = models.ForeignKey( Musicas, on_delete=models.CASCADE)

    def __str__(self):
      return self.musica.nome_musica