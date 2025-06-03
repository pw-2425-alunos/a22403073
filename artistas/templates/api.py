from ninja import NinjaAPI
from artistas.models import Artista
from typing import List
from ninja.orm import create_schema

api = NinjaAPI(title="API de Artistas")

ArtistaSchema = create_schema(Artista)

@api.get("/artistas", response=List[ArtistaSchema])
def listar_artistas(request):
    return Artista.objects.all()
