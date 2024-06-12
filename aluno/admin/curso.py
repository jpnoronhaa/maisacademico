from django.contrib import admin
from aluno.models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
  list_display = ('nome', 'ativo', 'display_campus_nome')
  search_fields = ('nome', 'ativo', 'campus__nome')
  
  def display_campus_nome(self, curso):
    return curso.campus.nome
  display_campus_nome.short_description = 'Campus'