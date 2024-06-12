from django.views.generic import CreateView, ListView
from aluno.models import Curso
from aluno.forms import CursoForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CreateCursoView (SuccessMessageMixin, CreateView):
  model = Curso
  form_class = CursoForm
  template_name = 'aluno/create/create_curso.html'
  success_url = reverse_lazy('index')
  
class ListCursoView (ListView):
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