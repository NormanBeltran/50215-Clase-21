from django.shortcuts import render

from .models import *
from .forms import * 

# Copyright Norman Beltran

def home(request):
    return render(request, "aplicacion/index.html") 

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto) 

def profesores(request):
    contexto = {'profesores': Profesor.objects.all()}
    return render(request, "aplicacion/profesores.html", contexto) 

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html") 

def entregables(request):
    return render(request, "aplicacion/entregables.html") 

#________________________________________ Adicionales
def acerca(request):
    return render(request, "aplicacion/acerca.html") 

#________________________________________ Forms
def cursoForm(request):
    # __ Si ingresa en el if es la 2da o enesima vez que llega el formulario
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_comision = miForm.cleaned_data.get("comision")
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()

            contexto = {'cursos': Curso.objects.all()}
            return render(request, "aplicacion/cursos.html", contexto) 

    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = CursoForm()

    return render(request, "aplicacion/cursoForm.html", {"form": miForm} )

def profesorForm(request):
    # __ Si ingresa en el if es la 2da o enesima vez que llega el formulario
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            prof_nombre = miForm.cleaned_data.get("nombre")
            prof_apellido = miForm.cleaned_data.get("apellido")
            prof_email = miForm.cleaned_data.get("email")
            prof_profesion = miForm.cleaned_data.get("profesion")

            profesor = Profesor(nombre=prof_nombre, 
                             apellido=prof_apellido,
                             email=prof_email,
                             profesion=prof_profesion)
            profesor.save()
            
            contexto = {'profesores': Profesor.objects.all()}
            return render(request, "aplicacion/profesores.html", contexto) 

    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = ProfesorForm()

    return render(request, "aplicacion/cursoForm.html", {"form": miForm} )

#________________________ Buscar

def buscarCursos(request):
    return render(request, "aplicacion/buscar.html")

def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
        return render(request, "aplicacion/cursos.html", contexto)
    

    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto) 