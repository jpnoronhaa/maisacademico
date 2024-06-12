from django.db import models
from .curso import Curso
from aluno.constants import formaIngressoChoices, situacaoChoices
from datetime import date

class Aluno(models.Model):
  nomeCompleto = models.CharField(max_length=255, verbose_name="Nome Completo do Aluno")
  ativo = models.BooleanField(default=True, verbose_name="Ativo?")
  cpf = models.PositiveIntegerField(unique=True, verbose_name="CPF do Aluno")
  dataNascimento = models.DateTimeField(verbose_name="Data de Nascimento do Aluno")
  situacao = models.CharField(max_length=50, choices=situacaoChoices, default="VINCULADO", verbose_name="Situação do Aluno")
  formaIngresso = models.CharField(max_length=50, choices=formaIngressoChoices, default="VESTIBULAR", verbose_name="Forma de Ingresso do Aluno")
  matricula = models.PositiveIntegerField(verbose_name="Matrícula do Aluno", unique=True, null=True, blank=True)
  foto = models.ImageField(null=True, blank=True, upload_to="aluno_foto/")
  curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso do Aluno")
  
  
  def __str__(self):
    return self.nomeCompleto
  
  def gerarMatricula(self):
    if self.pk is None:
      last_item = Aluno.objects.last()
      today = date.today()
      matricula_str = str(today.year)
      matricula_str += '1' if today.month < 7 else '2'
      if last_item is None or int(matricula_str) > int(str(last_item.matricula)[:5]):
        matricula_str += '0000'
      else:
        matricula_str += str(int(str(last_item.matricula)[5:]) + 1).rjust(4, "0")
      self.matricula = int(matricula_str)
      print("Matricula: ", matricula_str)
        
  def save(self, *args, **kwargs):
    self.gerarMatricula()
    super().save(*args, **kwargs)