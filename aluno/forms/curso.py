from django import forms
from aluno.models import Curso, Campus

class CursoForm(forms.ModelForm):  
  class Meta:  
    model = Curso
    fields = ['nome', 'campus', 'ativo']
    widgets = {
      "nome": forms.TextInput(attrs={"class": 'form-control form-control-user'}),
      "campus": forms.Select(attrs={"class": 'dropdown form-control'}),
      "ativo": forms.CheckboxInput(attrs={"class": 'custom-control-input'}),
    }

