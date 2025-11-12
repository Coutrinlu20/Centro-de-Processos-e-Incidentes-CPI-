from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Documento
from .forms import DocumentoForm

def listar_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/documentos_list.html', {'documentos': documentos})

def criar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manual criado com sucesso!')
            return redirect('documentos_list')
    else:
        form = DocumentoForm()

    return render(request, 'documentos/documento_form.html', {'form': form})

def editar_documento(request, id):  # <<-- nome que a URL espera
    documento = get_object_or_404(Documento, id=id)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manual atualizado com sucesso!')
            return redirect('documentos_list')
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'documentos/documento_edit.html', {'form': form, 'documento': documento})

def excluir_documento(request, id):
    documento = get_object_or_404(Documento, id=id)
    documento.delete()
    messages.success(request, 'Manual excluído com sucesso!')
    return redirect('documentos_list')

def visualizar_documento(request, id):
    documento = get_object_or_404(Documento, id=id)
    documento.visualizacoes += 1
    documento.save(update_fields=['visualizacoes'])
    return render(request, 'documentos/documento_detail.html', {'documento': documento})


