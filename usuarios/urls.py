from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    # Permissões
    path("permissoes/<int:usuario_id>/", views.alterar_permissoes, name="alterar_permissoes"),

    path("desativar/<int:usuario_id>/", views.desativar_usuario, name="desativar_usuario"),
    path("excluir/<int:usuario_id>/", views.excluir_usuario, name="excluir_usuario"),
]
