from django.contrib import admin
from .models import Autor, Artigo, Comentario, Rating

class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_publicacao")
    search_fields = ("titulo", "autor__nome")
    ordering = ("data_publicacao",)
    list_filter = ("autor", "data_publicacao")

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "artigo", "data_comentario")
    search_fields = ("nome", "artigo__titulo")
    list_filter = ("data_comentario",)


class RatingAdmin(admin.ModelAdmin):
    list_display = ("artigo", "rate", "usuario")
    list_filter = ("rate",)
    search_fields = ("artigo__titulo", "usuario")

admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Rating, RatingAdmin)
