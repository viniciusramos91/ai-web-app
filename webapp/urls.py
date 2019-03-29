from django.contrib import admin
from django.urls import path
from webapp.views import index

# Lista contendo todos os caminhos da sua aplicação
urlpatterns = [
    # Sim, o Django já vem com uma área de administrador por padrão!
    # Acesse: https://docs.djangoproject.com/en/2.0/intro/tutorial02/#introducing-the-django-admin
    path('admin/', admin.site.urls),
    
    # Rota que encaminha as requisições do caminho raíz para nossa view index()
    path('', index, name='index')
]
