from django import forms
from aluno.models import Aluno

class AlunoForm(forms.ModelForm):  
  class Meta:  
    model = Aluno
    fields = ['nomeCompleto', 'cpf', 'dataNascimento', 'situacao', 'formaIngresso', 'foto', 'curso', 'matricula', 'ativo']
    exclude = ('matricula',)
    widgets = {
      "nomeCompleto": forms.TextInput(attrs={"class": 'form-control'}),
      "cpf": forms.TextInput(attrs={"class": 'form-control'}),
      "dataNascimento": forms.widgets.DateInput(format=('%DD/%MM/%YYYY'), attrs={"class": 'form-control dateinput', 'type': 'date'}),
      "situacao": forms.Select(attrs={"class": 'dropdown form-control'}),
      "formaIngresso": forms.Select(attrs={"class": 'dropdown form-control'}),
      "curso": forms.Select(attrs={"class": 'dropdown form-control'}),
      "foto": forms.ClearableFileInput(),
      "ativo": forms.CheckboxInput(attrs={"class": 'custom-control-input'}),
    }

