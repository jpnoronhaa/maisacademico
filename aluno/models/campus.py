from django.db import models

class Campus(models.Model):
  nome = models.CharField(max_length=255, unique=True, verbose_name="Nome do Campus")
  ativo = models.BooleanField(default=True, verbose_name="Ativo?")
  
  class Meta:
    verbose_name_plural = "Campi"
  
  def __str__(self):
    return self.nome