from django.views.generic import CreateView, ListView
from aluno.models import Campus
from aluno.forms import CampusForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CreateCampusView (SuccessMessageMixin, CreateView):
  model = Campus
  form_class = CampusForm
  template_name = 'aluno/create/create_campus.html'
  success_url = reverse_lazy('index')
  
class ListCampusView (ListView):
  model = Campus
  template_name = 'aluno/list/list_campus.html'
  
  def get_queryset(self):
    queryset = super().get_queryset()
    items_per_page = self.request.GET.get('items_per_page', 10)
    self.paginate_by = items_per_page
    nome = self.request.GET.get('nome')
    if nome:
      queryset = queryset.filter(nome__icontains=nome)
    return queryset
