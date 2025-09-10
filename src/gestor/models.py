from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en semanas")
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre