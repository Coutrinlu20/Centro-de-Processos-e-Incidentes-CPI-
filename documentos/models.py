from django.db import models
from django.conf import settings

class Documento(models.Model):
    CATEGORIAS = [
        ('TI', 'TI'),
        ('RH', 'RH'),
        ('Comercial', 'Comercial'),
        ('Atendimento', 'Atendimento'),
        ('Financeiro', 'Financeiro'),
    ]
    

    def lista_tags(self):
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(',')]
    
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    tags = models.CharField(max_length=200, blank=True, help_text="Separadas por vírgula (,)")
    arquivo = models.FileField(upload_to='documentos/')
    versao = models.CharField(max_length=10, default='v1.0')
    visualizacoes = models.PositiveIntegerField(default=0)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
