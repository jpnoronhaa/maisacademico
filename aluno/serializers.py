from rest_framework import serializers
from .models import Campus, Aluno, Curso

class CampusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Campus
    fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = '__all__'