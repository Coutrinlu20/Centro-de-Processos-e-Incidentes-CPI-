from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_incidentes, name='incidentes_listar'),
    path('novo/', views.criar_incidente, name='incidente_create'),
    path('<int:id>/', views.detalhar_incidente, name='incidente_detail'),
    path('<int:id>/editar/', views.editar_incidente, name='incidente_edit'),
    path('<int:id>/excluir/', views.excluir_incidente, name='incidente_delete'),
]