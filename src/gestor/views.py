from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Estudiante, Curso
from .forms import EstudianteForm, CursoForm

def home(request):
    total_estudiantes = Estudiante.objects.count()
    total_cursos = Curso.objects.count()
    context = {
        'total_estudiantes': total_estudiantes,
        'total_cursos': total_cursos,
    }
    return render(request, 'gestor/home.html', context)

# CRUD Estudiantes
def estudiante_list(request):
    query = request.GET.get('q')
    if query:
        estudiantes = Estudiante.objects.filter(
            Q(nombre__icontains=query) | 
            Q(email__icontains=query) |
            Q(curso__nombre__icontains=query)
        )
    else:
        estudiantes = Estudiante.objects.all().select_related('curso')
    
    context = {
        'estudiantes': estudiantes,
        'query': query,
    }
    return render(request, 'gestor/estudiante_list.html', context)

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    
    return render(request, 'gestor/estudiante_form.html', {'form': form, 'title': 'Crear Estudiante'})

def estudiante_edit(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    
    return render(request, 'gestor/estudiante_form.html', {'form': form, 'title': 'Editar Estudiante'})

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiante_list')
    
    return render(request, 'gestor/estudiante_confirm_delete.html', {'estudiante': estudiante})

# CRUD Cursos
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'gestor/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    
    return render(request, 'gestor/curso_form.html', {'form': form, 'title': 'Crear Curso'})

def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'gestor/curso_form.html', {'form': form, 'title': 'Editar Curso'})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    
    return render(request, 'gestor/curso_confirm_delete.html', {'curso': curso})