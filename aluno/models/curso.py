from django.db import models
from .campus import Campus

class Curso(models.Model):
  nome = models.CharField(max_length=255, unique=True, verbose_name="Nome do Curso")
  ativo = models.BooleanField(default=True, verbose_name="Ativo?")
  campus = models.ForeignKey(Campus, verbose_name="Campus do Curso", on_delete=models.PROTECT)
  
  def __str__(self):
    return self.nome + " - " + self.campus.nome