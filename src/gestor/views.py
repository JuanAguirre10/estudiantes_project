from django.shortcuts import render
from .models import Estudiante, Curso

def home(request):
    total_estudiantes = Estudiante.objects.count()
    total_cursos = Curso.objects.count()
    context = {
        'total_estudiantes': total_estudiantes,
        'total_cursos': total_cursos,
    }
    return render(request, 'gestor/home.html', context)

def estudiante_list(request):
    estudiantes = Estudiante.objects.all().select_related('curso')
    return render(request, 'gestor/estudiante_list.html', {'estudiantes': estudiantes})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'gestor/curso_list.html', {'cursos': cursos})