from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
