from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 

class LoginRequired(LoginRequiredMixin, View):
  redirect_field_name = 'redirect'
  login_url = '/'