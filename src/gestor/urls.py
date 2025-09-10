from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para Estudiantes
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/crear/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<int:pk>/editar/', views.estudiante_edit, name='estudiante_edit'),
    path('estudiantes/<int:pk>/eliminar/', views.estudiante_delete, name='estudiante_delete'),
    
    # URLs para Cursos
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/crear/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', views.curso_edit, name='curso_edit'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),
]