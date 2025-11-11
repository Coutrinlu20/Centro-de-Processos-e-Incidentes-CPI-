from django.urls import path
from . import views

urlpatterns = [
    path('incidentes/', views.listar_incidentes, name='incidentes_list'),
    path('incidentes/novo/', views.criar_incidente, name='incident_create'),
    path('incidentes/<int:pk>/', views.detalhe_incidente, name='incident_detail'),
    path('incidentes/editar/<int:pk>/', views.editar_incidente, name='incident_update'),
    path('incidentes/excluir/<int:pk>/', views.excluir_incidente, name='incident_delete'),
    path('incidentes/exportar/', views.exportar_incidentes, name='incident_export'),
]
