from django import forms
from aluno.models import Campus

class CampusForm(forms.ModelForm):  
  class Meta:  
    model = Campus
    fields = ['nome', 'ativo']
    widgets = {
      "nome": forms.TextInput(attrs={"class": 'form-control form-control-user'}),
      "ativo": forms.CheckboxInput(attrs={"class": 'custom-control-input'}),
    }