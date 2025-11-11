# usuarios/forms.py
from django import forms
from .models import Usuario

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
