from django import forms
from .models import Incidente


class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['title', 'description', 'priority', 'status', 'category', 'assignee']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'assignee': forms.Select(attrs={'class': 'form-select'}),
        }


class AnexoForm(forms.Form):
    """Formulário que permite upload múltiplo de arquivos (Django 5+)."""
    files = forms.FileField(
        label="Anexos (imagens ou documentos)",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control'},
        )
    )

    # ⚙️ Novo método necessário no Django 5 para permitir múltiplos arquivos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['files'].widget.allow_multiple_selected = True


class FiltroIncidenteForm(forms.Form):
    """Formulário de filtros de relatório/listagem."""
    start_date = forms.DateField(
        label="Data inicial",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        label="Data final",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    category = forms.ChoiceField(
        label="Categoria", required=False, choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ChoiceField(
        label="Status", required=False, choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    assignee = forms.ModelChoiceField(
        label="Responsável", required=False, queryset=None,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        from django.contrib.auth.models import User
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Todas')] + list(
            Incidente._meta.get_field('category').choices
        )
        self.fields['status'].choices = [('', 'Todos')] + list(
            Incidente._meta.get_field('status').choices
        )
        self.fields['assignee'].queryset = User.objects.all()
