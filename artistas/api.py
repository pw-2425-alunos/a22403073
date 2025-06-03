from ninja import NinjaAPI
from .models import Artista
from .schemas import ArtistaIn, ArtistaOut, ErrorSchema
from typing import List
from django.shortcuts import get_object_or_404

api = NinjaAPI(
    title="API dos Artistas",
    description="API RESTful para gerir artistas",
    version="1.0.0"
)

@api.get("artistas/", response={200: List[ArtistaOut]}, tags=["Artistas"])
def list_artistas(request):
    return 200, Artista.objects.all()

@api.get("artistas/{artista_id}/", response={200: ArtistaOut, 404: ErrorSchema}, tags=["Artistas"])
def get_artista(request, artista_id: int):
    artista = get_object_or_404(Artista, id=artista_id)
    return 200, artista

@api.post("artistas/", response={201: ArtistaOut, 400: ErrorSchema}, tags=["Artistas"])
def create_artista(request, data: ArtistaIn):
    artista = Artista.objects.create(**data.dict())
    return 201, artista

@api.put("artistas/{artista_id}/", response={200: ArtistaOut, 404: ErrorSchema}, tags=["Artistas"])
def update_artista(request, artista_id: int, data: ArtistaIn):
    artista = get_object_or_404(Artista, id=artista_id)
    for attr, value in data.dict().items():
        setattr(artista, attr, value)
    artista.save()
    return 200, artista

@api.delete("artistas/{artista_id}/", response={204: None, 404: ErrorSchema}, tags=["Artistas"])
def delete_artista(request, artista_id: int):
    artista = get_object_or_404(Artista, id=artista_id)
    artista.delete()
    return 204, None
