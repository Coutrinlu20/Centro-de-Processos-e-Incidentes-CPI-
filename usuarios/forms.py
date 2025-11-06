from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'email', 'role', 'status', 'last_login', 'incidents', 'articles']
