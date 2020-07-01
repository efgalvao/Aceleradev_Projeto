from django.urls import path, include
from users.views import cadastrar_view
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'users'

urlpatterns = [
    path('cadastrar/', cadastrar_view, name='cadastrar'),
    path('login', obtain_auth_token, name="login"),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)    
