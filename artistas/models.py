from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    ano_inicio = models.IntegerField()
    foto = models.ImageField(upload_to='artistas_fotos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='artistas/', null=True, blank=True)
    ficheiro = models.FileField(upload_to='app/ficheiros', null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albuns', default=1)
    ano_lancamento = models.IntegerField()
    capa = models.ImageField(upload_to='capas_albuns/', blank=True, null=True)

    def __str__(self):
        return f'Álbum: {self.titulo} ({self.ano_lancamento}) Artista: {self.artista.nome}'

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    duracao = models.DurationField()
    letra = models.TextField(blank=True, null=True)
    link_streaming = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Música: {self.titulo} Álbum {self.album.titulo}'
