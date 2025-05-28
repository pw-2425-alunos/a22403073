from django.contrib import admin
from .models import Artista, Album, Musica

class AlbumInline(admin.TabularInline):
    model = Album

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade", "ano_inicio")
    ordering = ("nome",)
    search_fields = ("nome", "nacionalidade")
    list_filter = ("ano_inicio", "nacionalidade")
    prepopulated_fields = {"descricao": ("nome",)}
    inlines = [AlbumInline]

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "ano_lancamento")
    ordering = ("ano_lancamento",)
    search_fields = ("titulo", "artista__nome")
    list_filter = ("ano_lancamento", "artista")

class MusicaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "album", "duracao")
    ordering = ("titulo",)
    search_fields = ("titulo", "album__titulo")
    list_filter = ("album",)
    list_editable = ("duracao",)

admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)