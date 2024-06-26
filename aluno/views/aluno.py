from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from aluno.models import Aluno
from aluno.forms import AlunoForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets

from aluno.serializers import AlunoSerializer
from setup.libs import LoginRequired

class CreateAlunoView (LoginRequired, SuccessMessageMixin, CreateView):
  model = Aluno
  form_class = AlunoForm
  template_name = 'aluno/create/create_aluno.html'
  success_url = reverse_lazy('index')
  
class ListAlunoView (LoginRequired, ListView):
  model = Aluno
  paginate_by = 10
  template_name = 'aluno/list/list_aluno.html'
  
  def get_queryset(self):
    queryset = super().get_queryset()
    items_per_page = self.request.GET.get('items_per_page', 10)
    self.paginate_by = items_per_page
    nome = self.request.GET.get('nome')
    if nome:
      queryset = queryset.filter(nome__icontains=nome)
    return queryset

class DeleteAlunoView (LoginRequired, DeleteView):
  model = Aluno
  template_name = 'aluno/delete/delete_aluno.html'
  success_url = reverse_lazy('listAluno')

class UpdateAlunoView (LoginRequired, UpdateView):
  model = Aluno
  form_class = AlunoForm
  template_name = 'aluno/update/update_aluno.html'
  success_url = reverse_lazy('listAluno')

class AlunoAPI(viewsets.ModelViewSet):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer