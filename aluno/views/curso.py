from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from aluno.models import Curso
from aluno.forms import CursoForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets

from aluno.serializers import CursoSerializer
from setup.libs import LoginRequired

class CreateCursoView (LoginRequired, SuccessMessageMixin, CreateView):
  model = Curso
  form_class = CursoForm
  template_name = 'aluno/create/create_curso.html'
  success_url = reverse_lazy('index')
  
class ListCursoView (LoginRequired, ListView):
  model = Curso
  template_name = 'aluno/list/list_curso.html'
  
  def get_queryset(self):
    queryset = super().get_queryset()
    items_per_page = self.request.GET.get('items_per_page', 10)
    self.paginate_by = items_per_page
    nome = self.request.GET.get('nome')
    if nome:
      queryset = queryset.filter(nome__icontains=nome)
    return queryset
  
class DeleteCursoView (LoginRequired, DeleteView):
  model = Curso
  template_name = 'aluno/delete/delete_curso.html'
  success_url = reverse_lazy('listCurso')

class UpdateCursoView (LoginRequired, UpdateView):
  model = Curso
  form_class = CursoForm
  template_name = 'aluno/update/update_curso.html'
  success_url = reverse_lazy('listCurso')

class CursoAPI(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer