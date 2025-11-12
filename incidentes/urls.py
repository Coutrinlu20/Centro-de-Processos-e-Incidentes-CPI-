from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_incidentes, name='incidentes_list'),
    path('novo/', views.criar_incidente, name='incident_create'),
    path('<int:id>/editar/', views.editar_incidente, name='incident_edit'),
    path('<int:id>/excluir/', views.excluir_incidente, name='incident_delete'),
    path('<int:id>/', views.visualizar_incidente, name='incident_detail'),
]
