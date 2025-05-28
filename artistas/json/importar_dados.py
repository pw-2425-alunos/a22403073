import os
import json
from datetime import timedelta
from artistas.models import Artista, Album, Musica


def parse_duracao(dur_str):
    minutos, segundos = map(int, dur_str.split(":"))
    return timedelta(minutes=minutos, seconds=segundos)
    
#Esta funçao parse_duracao usei para dar uma estetica melhor a duracao na api, se nao a quiser usar basta mudar a "DurationField" no models

def importar_artistas(ficheiro):
    caminho = os.path.join(os.path.dirname(__file__), ficheiro)
    with open(caminho, encoding='utf-8') as f:
        dados = json.load(f)["artistas"]
        for item in dados:
            Artista.objects.get_or_create(
                nome=item["nome"],
                defaults={
                    "nacionalidade": item["nacionalidade"],
                    "ano_inicio": item["ano_inicio"]
                }
            )

def importar_albuns(ficheiro):
    caminho = os.path.join(os.path.dirname(__file__), ficheiro)
    with open(caminho, encoding='utf-8') as f:
        dados = json.load(f)["albuns"]
        for item in dados:
            try:
                artista = Artista.objects.get(nome=item["artista"])
            except Artista.DoesNotExist:
                print(f"⚠️ Artista '{item['artista']}' não encontrado. Ignorar álbum '{item['titulo']}'")
                continue

            album, _ = Album.objects.get_or_create(
                titulo=item["titulo"],
                ano_lancamento=item["ano_lancamento"],
                artista=artista
            )

            for musica_data in item["musicas"]:
                Musica.objects.get_or_create(
                    titulo=musica_data["titulo"],
                    duracao=parse_duracao(musica_data["duracao"]),
                    album=album
                )

#Criei esta funçao para poupar trabalho quando quiser importar tudo

def importar_todos():
    importar_artistas("artistas.json")
    importar_albuns("albuns.json")
    print("✅ Todos os dados foram importados com sucesso." )