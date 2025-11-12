from django.contrib import admin
from django.urls import path, include
from setup import views  # ✅ importa do app principal (setup)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login e logout
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Páginas principais
    path('index/', views.index, name='index'),

    # Apps do sistema
    path('usuarios/', include('usuarios.urls')),
    path('incidentes/', include('incidentes.urls')),
    path('documentos/', include('documentos.urls')),
    path('', views.index, name='index'),   # ← Página inicial

]
