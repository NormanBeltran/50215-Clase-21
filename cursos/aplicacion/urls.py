from django.urls import path, include
from .views import *

urlpatterns = [
    #__________________  Menu Principal
    path('', home, name="home"),

    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),

    # __________________ Otras páginas
    path('acerca/', acerca, name="acerca_de_mi"),

    #___________________ Formularios
    path('curso_form/', cursoForm, name="curso_form"),
    path('prof_form/', profesorForm, name="prof_form"),

    #____________________ Busqueda
    path('buscar_cursos/', buscarCursos, name="buscar_cursos"),
    path('encontrar_cursos/', encontrarCursos, name="encontrar_cursos"),
]
