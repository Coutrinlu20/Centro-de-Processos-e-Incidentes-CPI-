from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'descricao', 'categoria', 'versao', 'tags']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Ex: Manual de Onboarding',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'rows': 3,
                'placeholder': 'Descreva o conteúdo e objetivo deste manual...',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select rounded-3',
            }),
            'versao': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'value': '1.0',
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Ex: onboarding, rh, processo (separadas por vírgula)',
            }),
        }
