from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_documentos, name='documentos_list'),
    path('novo/', views.criar_documento, name='documento_create'),
    path('<int:id>/editar/', views.editar_documento, name='documento_edit'),
    path('<int:id>/excluir/', views.excluir_documento, name='documento_delete'),
    path('<int:id>/', views.visualizar_documento, name='documento_detail'),
]
