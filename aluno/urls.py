from django.urls import include, path
from aluno.views import HomePageView, CreateCampusView, CreateCursoView, CreateAlunoView, ListCampusView, ListCursoView, ListAlunoView
from aluno.views.aluno import AlunoAPI, DeleteAlunoView, UpdateAlunoView
from aluno.views.campus import CampusAPI, DeleteCampusView, UpdateCampusView
from aluno.views.curso import CursoAPI, DeleteCursoView, UpdateCursoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'campus', CampusAPI)
router.register(r'aluno', AlunoAPI)
router.register(r'curso', CursoAPI)

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('cadastro/campus', CreateCampusView.as_view(), name='createCampus'),
    path('cadastro/curso', CreateCursoView.as_view(), name='createCurso'),
    path('cadastro/aluno', CreateAlunoView.as_view(), name='createAluno'),
    path('listagem/campus', ListCampusView.as_view(), name='listCampus'),
    path('listagem/curso', ListCursoView.as_view(), name='listCurso'),
    path('listagem/aluno', ListAlunoView.as_view(), name='listAluno'),
    path('delete/campus/<int:pk>/', DeleteCampusView.as_view(), name='deleteCampus'),
    path('delete/curso/<int:pk>/', DeleteCursoView.as_view(), name='deleteCurso'),
    path('delete/aluno/<int:pk>/', DeleteAlunoView.as_view(), name='deleteAluno'),
    path('update/campus/<int:pk>/', UpdateCampusView.as_view(), name='updateCampus'),
    path('update/curso/<int:pk>/', UpdateCursoView.as_view(), name='updateCurso'),
    path('update/aluno/<int:pk>/', UpdateAlunoView.as_view(), name='updateAluno'),
    path('api/', include(router.urls)),
]