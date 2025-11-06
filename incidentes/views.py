from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import csv

from .models import Incidente, Anexo
from .forms import IncidenteForm, AnexoForm, FiltroIncidenteForm


@login_required
def listar_incidentes(request):
    form = FiltroIncidenteForm(request.GET or None)
    incidentes = Incidente.objects.all().order_by('-created_at')

    # Filtros (RF08)
    if form.is_valid():
        start = form.cleaned_data.get('start_date')
        end = form.cleaned_data.get('end_date')
        category = form.cleaned_data.get('category')
        status = form.cleaned_data.get('status')
        assignee = form.cleaned_data.get('assignee')

        if start:
            incidentes = incidentes.filter(created_at__gte=start)
        if end:
            incidentes = incidentes.filter(created_at__lte=end)
        if category:
            incidentes = incidentes.filter(category=category)
        if status:
            incidentes = incidentes.filter(status=status)
        if assignee:
            incidentes = incidentes.filter(assignee=assignee)

    return render(request, 'incidentes/incidentes_list.html', {'page_obj': incidentes, 'filters_form': form})


@login_required
def criar_incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST)
        files_form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.save()
            # Anexos
            for f in request.FILES.getlist('file'):
                Anexo.objects.create(incidente=incidente, file=f, uploaded_by=request.user)
            messages.success(request, 'Incidente criado com sucesso!')

            # RF09 - Notificação (exemplo simples)
            if incidente.assignee and incidente.assignee.email:
                send_mail(
                    'Novo incidente atribuído',
                    f'Você foi designado para o incidente: {incidente.title}',
                    'no-reply@empresa.com',
                    [incidente.assignee.email],
                    fail_silently=True,
                )

            return redirect('incident_list')
    else:
        form = IncidenteForm()
        files_form = AnexoForm()
    return render(request, 'incidentes/incidente_form.html', {'form': form, 'attachments_form': files_form, 'titulo': 'Novo Incidente'})


@login_required
def editar_incidente(request, pk):
    incidente = get_object_or_404(Incidente, pk=pk)
    if request.method == 'POST':
        form = IncidenteForm(request.POST, instance=incidente)
        files_form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for f in request.FILES.getlist('file'):
                Anexo.objects.create(incidente=incidente, file=f, uploaded_by=request.user)
            messages.success(request, 'Incidente atualizado com sucesso!')
            return redirect('incident_detail', pk=pk)
    else:
        form = IncidenteForm(instance=incidente)
        files_form = AnexoForm()
    return render(request, 'incidentes/incidente_form.html', {'form': form, 'attachments_form': files_form, 'titulo': 'Editar Incidente'})


@login_required
def detalhe_incidente(request, pk):
    incidente = get_object_or_404(Incidente, pk=pk)
    form = AnexoForm()
    return render(request, 'incidentes/incidente_detail.html', {'incidente': incidente, 'attachments_form': form})


@login_required
def excluir_incidente(request, pk):
    incidente = get_object_or_404(Incidente, pk=pk)
    if request.method == 'POST':
        incidente.delete()
        messages.success(request, 'Incidente excluído com sucesso!')
        return redirect('incident_list')
    return render(request, 'incidentes/incidente_confirm_delete.html', {'incidente': incidente})


@login_required
def exportar_incidentes(request):
    """Exporta CSV com filtros aplicados"""
    form = FiltroIncidenteForm(request.GET or None)
    incidentes = Incidente.objects.all().order_by('-created_at')

    if form.is_valid():
        start = form.cleaned_data.get('start_date')
        end = form.cleaned_data.get('end_date')
        category = form.cleaned_data.get('category')
        status = form.cleaned_data.get('status')
        assignee = form.cleaned_data.get('assignee')

        if start:
            incidentes = incidentes.filter(created_at__gte=start)
        if end:
            incidentes = incidentes.filter(created_at__lte=end)
        if category:
            incidentes = incidentes.filter(category=category)
        if status:
            incidentes = incidentes.filter(status=status)
        if assignee:
            incidentes = incidentes.filter(assignee=assignee)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="incidentes.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Título', 'Descrição', 'Prioridade', 'Status', 'Categoria', 'Responsável', 'Criado', 'Atualizado'])
    for i in incidentes:
        writer.writerow([i.id, i.title, i.description, i.priority, i.status, i.category, i.assignee, i.created_at, i.updated_at])
    return response
