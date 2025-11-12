from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.usuarios_listar, name='usuarios_listar'),
    path('novo/', views.criar_usuario, name='usuarios_criar'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    # Permissões
    path("permissoes/<int:usuario_id>/", views.alterar_permissoes, name="alterar_permissoes"),

    path("desativar/<int:usuario_id>/", views.desativar_usuario, name="desativar_usuario"),
    path("excluir/<int:usuario_id>/", views.excluir_usuario, name="excluir_usuario"),
]
