from django.shortcuts import render
from incidentes.models import Incidente
from django.db.models import Count


def index(request):
    # Busca os 5 incidentes mais recentes — campo correto é 'criado_em'
    incidentes = Incidente.objects.order_by('-criado_em')[:5]

    # Conta quantos incidentes há por categoria
    categorias_qs = Incidente.objects.values('categoria').annotate(total=Count('categoria'))
    categorias = {item['categoria']: item['total'] for item in categorias_qs}

    return render(request, 'index.html', {
        'incidentes': incidentes,
        'categorias': categorias
    })
