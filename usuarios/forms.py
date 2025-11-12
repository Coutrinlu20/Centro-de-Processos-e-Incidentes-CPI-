# usuarios/forms.py
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PermissoesForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "can_view_incidents", "can_edit_incidents",
            "can_view_manuals", "can_edit_manuals",
            "can_manage_users", "can_view_reports",
        ]
        widgets = {
            "can_view_incidents": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_edit_incidents": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_view_manuals": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_edit_manuals": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_manage_users": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "can_view_reports": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class UsuarioForm(UserCreationForm):
    nome_completo = forms.CharField(
        label="Nome Completo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@empresa.com'})
    )
    perfil = forms.ChoiceField(
        label="Perfil de Acesso",
        choices=[('Administrador', 'Administrador'), ('Colaborador', 'Colaborador'), ('Visualizador', 'Visualizador')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite uma senha segura'})
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'})
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'perfil', 'password1', 'password2']