from django.urls import path
from aluno.views import HomePageView, CreateCampusView, CreateCursoView, CreateAlunoView, ListCampusView, ListCursoView, ListAlunoView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('cadastro/campus', CreateCampusView.as_view(), name='createCampus'),
    path('cadastro/curso', CreateCursoView.as_view(), name='createCurso'),
    path('cadastro/aluno', CreateAlunoView.as_view(), name='createAluno'),
    path('listagem/campus', ListCampusView.as_view(), name='listCampus'),
    path('listagem/curso', ListCursoView.as_view(), name='listCurso'),
    path('listagem/aluno', ListAlunoView.as_view(), name='listAluno'),
]