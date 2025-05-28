from django.contrib import admin

# Register your models here.
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    lista_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    search_fields = ("nome",)

admin.site.register(Pessoa, PessoaAdmin)
