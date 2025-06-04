# schemas.py
from ninja import Schema

class ArtistaIn(Schema):
    nome: str
    nacionalidade: str
    ano_inicio: int  

class ArtistaOut(Schema):
    id: int
    nome: str
    nacionalidade: str
    ano_inicio: int  

class ErrorSchema(Schema):
    detail: str

