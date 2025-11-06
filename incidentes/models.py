from django.db import models
from django.contrib.auth.models import User

# Opções fixas (choices)
PRIORIDADE_CHOICES = [
    ('BAIXA', 'Baixa'),
    ('MEDIA', 'Média'),
    ('ALTA', 'Alta'),
]

STATUS_CHOICES = [
    ('ABERTO', 'Aberto'),
    ('EM_ANDAMENTO', 'Em andamento'),
    ('RESOLVIDO', 'Resolvido'),
    ('ENCERRADO', 'Encerrado'),
]

CATEGORIA_CHOICES = [
    ('TI', 'Tecnologia da Informação'),
    ('PROCESSOS', 'Processos'),
    ('ATENDIMENTO', 'Atendimento'),
    ('OUTROS', 'Outros'),
]


class Incidente(models.Model):
    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descrição")
    priority = models.CharField("Prioridade", max_length=10, choices=PRIORIDADE_CHOICES)
    status = models.CharField("Status", max_length=15, choices=STATUS_CHOICES, default='ABERTO')
    category = models.CharField("Categoria", max_length=30, choices=CATEGORIA_CHOICES)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsável")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


class Anexo(models.Model):
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to='anexos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anexo {self.id} de {self.incidente.title}"

