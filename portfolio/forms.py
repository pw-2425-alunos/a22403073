from django import forms
from .models import Projeto, Interesse

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'

