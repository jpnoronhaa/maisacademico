
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views import View
from setup import settings

class Login(View):
  
  def get(self, request):
    if request.user.is_authenticated:
      return redirect('/main')
    else:
      return render(request, 'auth.html')
  
  def post(self, request):
    user = request.POST.get('user', None)
    password = request.POST.get('password', None)

    user = authenticate(request, username=user, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return redirect('/main')
      return render(request, 'auth.html', {'mensagem': 'Usuário inativo!'})
    return render(request, 'auth.html', {'mensagem': 'Usuário ou senha incorretos!'})
  

class Logout(View):

  def get(self, request):
    logout(request)
    return redirect(settings.LOGIN_URL)
  
class LoginAPI(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data,
      context={
        'request': request
      }
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'id': user.id,
      'nome': user.nome,
      'email': user.email,
      'token': token.key
    })