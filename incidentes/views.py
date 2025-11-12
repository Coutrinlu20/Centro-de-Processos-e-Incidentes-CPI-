from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Incidente
from .forms import IncidenteForm

# Listar incidentes
def listar_incidentes(request):
    incidentes = Incidente.objects.all()
    return render(request, 'incidentes/incidentes_list.html', {'incidentes': incidentes})

# Criar incidente
def criar_incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Incidente criado com sucesso!")
            return redirect('incidentes_list')
    else:
        form = IncidenteForm()
    return render(request, 'incidentes/incidente_form.html', {'form': form, 'acao': 'Novo'})

# Editar incidente
def editar_incidente(request, id):
    incidente = get_object_or_404(Incidente, id=id)
    if request.method == 'POST':
        form = IncidenteForm(request.POST, instance=incidente)
        if form.is_valid():
            form.save()
            messages.success(request, "Incidente atualizado com sucesso!")
            return redirect('incidentes_list')
    else:
        form = IncidenteForm(instance=incidente)
    return render(request, 'incidentes/incidente_form.html', {'form': form, 'acao': 'Editar'})

# Excluir incidente
def excluir_incidente(request, id):
    incidente = get_object_or_404(Incidente, id=id)
    incidente.delete()
    messages.success(request, "Incidente excluído com sucesso!")
    return redirect('incidentes_list')

# Visualizar incidente
def visualizar_incidente(request, id):
    incidente = get_object_or_404(Incidente, id=id)
    return render(request, 'incidentes/incidente_detail.html', {'incidente': incidente})
