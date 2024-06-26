from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from aluno.models import Campus
from aluno.forms import CampusForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets

from aluno.serializers import CampusSerializer
from setup.libs import LoginRequired

class CreateCampusView (LoginRequired, SuccessMessageMixin, CreateView):
  model = Campus
  form_class = CampusForm
  template_name = 'aluno/create/create_campus.html'
  context_object_name = 'object_list'
  success_url = reverse_lazy('listCampus')
  
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

class DeleteCampusView (LoginRequired, DeleteView):
  model = Campus
  template_name = 'aluno/delete/delete_campus.html'
  success_url = reverse_lazy('listCampus')

class UpdateCampusView (LoginRequired, UpdateView):
  model = Campus
  form_class = CampusForm
  template_name = 'aluno/update/update_campus.html'
  success_url = reverse_lazy('listCampus')

class CampusAPI(viewsets.ModelViewSet):
  queryset = Campus.objects.all()
  serializer_class = CampusSerializer