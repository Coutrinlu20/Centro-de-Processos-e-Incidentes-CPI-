from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['titulo', 'descricao', 'categoria', 'prioridade', 'status', 'assignee']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite o título do incidente'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Descreva o incidente',
                'rows': 4
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Categoria do incidente'
            }),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'assignee': forms.Select(attrs={'class': 'form-select'}),
        }
