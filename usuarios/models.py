from django.db import models

class Usuario(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('COLAB', 'Colaborador'),
        ('VIEW', 'Visualizador'),
    ]

    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
        ('SUSPENSO', 'Suspenso'),
    ]

    name = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail", unique=True)
    role = models.CharField("Papel", max_length=50, choices=ROLE_CHOICES, default='COLAB')
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='ATIVO')
    last_login = models.CharField("Último acesso", max_length=50, blank=True, null=True)
    incidents = models.IntegerField("Incidentes", default=0)
    articles = models.IntegerField("Artigos", default=0)

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"
