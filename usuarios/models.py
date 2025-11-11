# usuarios/models.py
from django.db import models

class Usuario(models.Model):
    ROLE_CHOICES = (
        ("admin", "Administrador"),
        ("colab", "Colaborador"),
        ("view", "Visualizador"),
    )
    STATUS_CHOICES = (("Ativo", "Ativo"), ("Inativo", "Inativo"))

    name = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    role = models.CharField("Papel", max_length=20, choices=ROLE_CHOICES, default="view")
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="Ativo")
    last_login = models.CharField("Último acesso", max_length=50, blank=True, null=True)
    incidents = models.IntegerField("Incidentes", default=0)
    articles = models.IntegerField("Artigos", default=0)

    # Permissões por módulo
    can_view_incidents = models.BooleanField(default=True)
    can_edit_incidents = models.BooleanField(default=False)

    can_view_manuals = models.BooleanField(default=True)
    can_edit_manuals = models.BooleanField(default=False)

    can_manage_users = models.BooleanField(default=False)
    can_view_reports = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def permissions_list(self):
        mapa = {
            "Ver Incidentes": self.can_view_incidents,
            "Editar Incidentes": self.can_edit_incidents,
            "Ver Manuais": self.can_view_manuals,
            "Editar Manuais": self.can_edit_manuals,
            "Gerenciar Usuários": self.can_manage_users,
            "Ver Relatórios": self.can_view_reports,
        }
        return [k for k, v in mapa.items() if v]
