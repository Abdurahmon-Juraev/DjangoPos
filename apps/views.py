from django.contrib.auth.models import User
from django.views.generic import TemplateView

from django.shortcuts import redirect

def home(request):
    return redirect('auth_login')

class LoginTemplateView(TemplateView):
    queryset = User.objects.all()
    template_name = 'login.html'
    context_object_name = 'user'


class RegisterTemplateView(TemplateView):
    queryset = User.objects.all()
    template_name = 'register.html'
