# portfolio/admin.py

from django.contrib import admin
from .models import Disciplina, Projeto, ImagemProjeto, Tecnologia, Conceito, Professor, Interesse, Visitante

class ImagemProjetoInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 1

class ConceitoInline(admin.StackedInline):
    model = Conceito
    extra = 0

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'link_github', 'link_demo')
    search_fields = ('titulo', 'descricao')
    list_filter = ('disciplina',)
    inlines = [ImagemProjetoInline, ConceitoInline]
    filter_horizontal = ('tecnologias',)


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', 'descricao')


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre')
    search_fields = ('nome', 'docentes')


class ConceitoAdmin(admin.ModelAdmin):
    list_display = ('projeto',)
    search_fields = ('conceitos_aplicados', 'desafios_tecnicos')

#ESTUDAR

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'email')
    search_fields = ('nome', 'disciplina')


class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', 'descricao')




admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Conceito, ConceitoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Interesse, InteresseAdmin)
admin.site.register(Visitante)
