from django.contrib import admin
from .models import Aluno, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula')  # mostra o usuário e a matrícula

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user', 'titulação', 'area_pesquisa')  # mostra o usuário e os campos
