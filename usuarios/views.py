from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import messages
from .forms import PermissoesForm
from django.contrib.auth.decorators import user_passes_test, login_required


def _is_admin(user):
    # Use a permissão do Django para gatekeeper (ajuste conforme sua regra)
    return user.is_superuser or user.is_staff

@login_required
@user_passes_test(_is_admin)
def alterar_permissoes(request, usuario_id):
    alvo = get_object_or_404(Usuario, id=usuario_id)

    if request.method == "POST":
        form = PermissoesForm(request.POST, instance=alvo)
        if form.is_valid():
            form.save()
            messages.success(request, f"Permissões de {alvo.name} atualizadas com sucesso.")
            return redirect("listar_usuarios")
        messages.error(request, "Verifique os campos e tente novamente.")
    else:
        form = PermissoesForm(instance=alvo)

    return render(request, "usuarios/alterar_permissoes.html", {
        "alvo": alvo,
        "form": form,
    })


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios_list.html', {'usuarios': usuarios})


def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        perfil = request.POST.get('perfil')
        # Salvar no banco (exemplo)
        # Usuario.objects.create(nome=nome, email=email, perfil=perfil, status='Ativo')

        messages.success(request, f"Usuário {nome} adicionado com sucesso!")
        return redirect('listar_usuarios')

    return render(request, 'usuarios/usuario_form.html')

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.perfil = request.POST.get('perfil')
        usuario.status = request.POST.get('status')
        usuario.save()

        messages.success(request, f"Usuário {usuario.nome} atualizado com sucesso!")
        return redirect('listar_usuarios')

    return render(request, 'usuarios/usuario_edit.html', {'usuario': usuario})

def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})


def desativar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.is_active = False  # desativa o usuário
    usuario.save()
    messages.success(request, f"Usuário {usuario.username} foi desativado com sucesso.")
    return redirect('listar_usuarios')
