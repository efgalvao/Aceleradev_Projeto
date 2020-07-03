from django.urls import path, include
from users.views import Cadastrar_View, User_list
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView


app_name = 'users'

urlpatterns = [
    path('list/', User_list.as_view(), name='user_list'),
    path('cadastrar/', Cadastrar_View.as_view(), name='cadastrar'),

]
urlpatterns = format_suffix_patterns(urlpatterns)    
