from django.contrib import admin
from django.urls import path

from apps.views import RegisterTemplateView, LoginTemplateView,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',RegisterTemplateView.as_view () , name='auth_register' ),
    path('login',LoginTemplateView.as_view() , name='auth_login' ),
    path('', home, name='home'),
]
