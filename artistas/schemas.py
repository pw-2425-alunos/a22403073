from ninja import Schema

class ArtistaIn(Schema):
    nome: str
    nacionalidade: str
    ano_nascimento: int

class ArtistaOut(Schema):
    id: int
    nome: str
    nacionalidade: str
    ano_nascimento: int

class ErrorSchema(Schema):
    detail: str
