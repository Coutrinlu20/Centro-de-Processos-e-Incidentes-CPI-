from django.shortcuts import render
from incidentes.models import Incidente
from django.db.models import Count
from documentos.models import Documento


def index(request):
    incidentes = Incidente.objects.order_by('-criado_em')[:5]
    documentos = Documento.objects.order_by('-criado_em')[:5]

    # Exemplo de categorias simuladas
    categorias = {
        'TI': 45,
        'Processos': 32,
        'Atendimento': 28,
        'RH': 18,
    }

    return render(request, 'index.html', {
        'incidentes': incidentes,
        'documentos': documentos,
        'categorias': categorias
    })