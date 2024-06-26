from django.contrib import admin
from django.urls import path, include

from setup.views import Login, Logout, LoginAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include('aluno.urls')),
    path('', Login.as_view(), name='index'),
    path('autenticacao-api/',LoginAPI.as_view()),
    path('logout/', Logout.as_view(), name='logout'),
]
