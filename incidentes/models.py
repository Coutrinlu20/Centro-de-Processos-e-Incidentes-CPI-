from django.db import models
from django.conf import settings

class Incidente(models.Model):
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em Andamento'),
        ('resolvido', 'Resolvido'),
        ('encerrado', 'Encerrado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100, blank=True, null=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aberto')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
