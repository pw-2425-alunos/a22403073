from django import forms
from .models import Artigo, Comentario

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'autor', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super(ArtigoForm, self).__init__(*args, **kwargs)
        self.fields['data_publicacao'].input_formats = ['%Y-%m-%d']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3})
        }
