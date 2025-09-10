from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('cursos/', views.curso_list, name='curso_list'),
]