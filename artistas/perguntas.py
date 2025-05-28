from artistas.models import Artista, Album, Musica
from datetime import timedelta
from django.db.models import Count

print(" 1: Imprime os artistas ordenados alfabeticamente:")
for artista in Artista.objects.order_by('nome'):
    print(f"- {artista.nome}")

print("\n")

print(" 2: Álbuns de um artista específico (ordenados cronologicamente):")
nome_artista = "Future"
try:
    artista = Artista.objects.get(nome=nome_artista)
    for album in artista.albuns.order_by('ano_lancamento'): 
        print(f"- {album.titulo} ({album.ano_lancamento})")
except Artista.DoesNotExist:
    print(f" Artista '{nome_artista}' não encontrado.")

print("\n")

print(" 3: Imprime os álbuns lançados entre 2018 e 2024")
for album in Album.objects.filter(ano_lancamento__range=(2018, 2024)):
    print(f"- {album.titulo} ({album.ano_lancamento})")

print("\n")

print(f' 4: Existe algum álbum com o nome "MIXTAPE PLUTO" ?')
titulo_album = "MIXTAPE PLUTO"
try:
    album = Album.objects.get(titulo=titulo_album)
    print(f"Álbum '{titulo_album}' encontrado. Músicas:")
    for musica in album.musicas.all(): 
        print(f"- {musica.titulo}")
except Album.DoesNotExist:
    print(f"Álbum '{titulo_album}' não encontrado.")

print("\n")

print(" 5: Imprime os álbuns com músicas que durem mais de 5 minutos:")
albuns = Album.objects.filter(musicas__duracao__gt=timedelta(minutes=5)).distinct()
for album in albuns:
    print(f"- {album.titulo}")

print("\n")

print(" 6: Músicas sem letra:")
musicas = Musica.objects.filter(letra__isnull=True) | Musica.objects.filter(letra='')
for m in musicas:
    print(f"- {m.titulo}")

print("\n")

print(" 7: Quantas músicas tem cada artista ? ")
for artista in Artista.objects.all():
    total = Musica.objects.filter(album__artista=artista).count()
    print(f"- {artista.nome}: {total} músicas")

print("\n")

print(" 8: Quais são os 5 álbuns mais recentes:")
for album in Album.objects.order_by('ano_lancamento')[:5]:
    print(f"- {album.titulo} ({album.ano_lancamento})")

print("\n")

print(" 9: Qual é o artista com o álbum mais antigo?")
album_mais_recente = Album.objects.order_by('ano_lancamento').first()
if album_mais_recente:
    print(f"- {album_mais_recente.artista.nome} ({album_mais_recente.titulo}, {album_mais_recente.ano_lancamento})")

print("\n")

print(" 10: Imprime os álbuns ordenados por ordem crescente:")
albuns = Album.objects.order_by('titulo')
for a in albuns:
    print(f"- {a.titulo}")
