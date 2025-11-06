from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios_list.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'titulo': 'Cadastrar Usuário'})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'titulo': 'Editar Usuário'})

def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})
