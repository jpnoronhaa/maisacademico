from django.contrib import admin
from aluno.models import Campus

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
  list_display = ('nome', 'ativo')
  search_fields = ('nome', 'ativo')