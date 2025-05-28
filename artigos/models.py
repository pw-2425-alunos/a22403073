from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Autor: {self.nome}"

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="artigos")
    data_publicacao = models.DateField(default=timezone.now)
    rating = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"Título: {self.titulo}"

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário por {self.nome} em {self.artigo}'



class Rating(models.Model):
    artigo = models.ForeignKey("Artigo", on_delete=models.CASCADE, related_name='ratings')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    class Meta:
        unique_together = ('artigo', 'usuario')  #cada user so pode dar rate 1 vez

    def __str__(self):
        return f"{self.usuario} → {self.artigo} ({self.rate})"

