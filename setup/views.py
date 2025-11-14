from django.shortcuts import render
from incidentes.models import Incidente
from documentos.models import Documento
from django.utils import timezone
from django.db.models import F, ExpressionWrapper, DurationField, Avg
from datetime import timedelta

def index(request):
    hoje = timezone.now().date()
    semana_passada = hoje - timedelta(days=7)

    # ===== MÉTRICAS =====
    incidentes_abertos = Incidente.objects.filter(status="aberto").count()

    resolvidos_hoje = Incidente.objects.filter(
        status="resolvido",
        atualizado_em__date=hoje
    ).count()

    # ===== TEMPO MÉDIO DE RESOLUÇÃO =====
    # Calcula duração: atualizado_em - criado_em
    incidentes_resolvidos = Incidente.objects.filter(status="resolvido").annotate(
        duracao=ExpressionWrapper(
            F("atualizado_em") - F("criado_em"),
            output_field=DurationField()
        )
    )

    tempo_medio_resolucao = incidentes_resolvidos.aggregate(
        media=Avg("duracao")
    )["media"]

    # Se não houver incidentes resolvidos, evita erro
    if tempo_medio_resolucao:
        horas_medias = round(tempo_medio_resolucao.total_seconds() / 3600, 1)
    else:
        horas_medias = 0

    # ===== MANUAIS =====
    manuais_publicados = Documento.objects.filter(
        criado_em__month=hoje.month
    ).count()

    # ===== RECENTES =====
    incidentes_recentes = Incidente.objects.order_by("-criado_em")[:3]
    documentos_recentes = Documento.objects.order_by("-criado_em")[:3]

    return render(request, "index.html", {
        "incidentes_abertos": incidentes_abertos,
        "resolvidos_hoje": resolvidos_hoje,
        "tempo_medio_resolucao": horas_medias,
        "manuais_publicados": manuais_publicados,
        "incidentes_recentes": incidentes_recentes,
        "documentos_recentes": documentos_recentes,
    })
