from django.views.generic import TemplateView
from aluno.models import Aluno
from aluno.models.campus import Campus
from aluno.models.curso import Curso
from setup.libs import LoginRequired

class HomePageView(LoginRequired, TemplateView):
  template_name = 'aluno/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['total_alunos'] = Aluno.objects.count()
    context['total_cursos'] = Curso.objects.count()
    context['total_campus'] = Campus.objects.count()
    return context