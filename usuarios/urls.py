from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.usuarios_listar, name='usuarios_listar'),
    path('novo/', views.criar_usuario, name='usuarios_criar'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    # Permissões
    path('permissoes/<int:id>/', views.gerenciar_permissoes, name='usuarios_permissoes'),


    path("desativar/<int:usuario_id>/", views.desativar_usuario, name="desativar_usuario"),
    path("excluir/<int:usuario_id>/", views.excluir_usuario, name="excluir_usuario"),
]
