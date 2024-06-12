from django.views.generic import CreateView, ListView
from aluno.models import Aluno
from aluno.forms import AlunoForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CreateAlunoView (SuccessMessageMixin, CreateView):
  model = Aluno
  form_class = AlunoForm
  template_name = 'aluno/create/create_aluno.html'
  success_url = reverse_lazy('index')
  
class ListAlunoView (ListView):
  model = Aluno
  paginate_by = 10
  template_name = 'aluno/list/list_aluno.html'