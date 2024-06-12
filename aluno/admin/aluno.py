from django.contrib import admin
from aluno.models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
  list_display = ('matricula', 'nomeCompleto', 'ativo', 'display_curso_nome', 'display_campus_nome', 'cpf', 'situacao')
  search_fields = ('matricula', 'nomeCompleto', 'ativo', 'curso__nome', 'curso__campus__nome', 'cpf', 'situacao')
    
  def display_curso_nome(self, aluno):
    return aluno.curso.nome
  display_curso_nome.short_description = 'Curso'
  
  def display_campus_nome(self, aluno):
    return aluno.curso.campus.nome
  display_campus_nome.short_description = 'Campus'