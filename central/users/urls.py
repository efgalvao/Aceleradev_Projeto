from django.urls import path, include
from users.views import Cadastrar_View, User_list, Login_View, Logout_View
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView


app_name = 'users'

urlpatterns = [
    #path('cadastrar/', Cadastrar_View.as_view(), name='cadastrar'),
    path('auth', obtain_auth_token, name="auth"),
    path('logout/', Logout_View.as_view(), name='logout'),
    path('list/', User_list.as_view(), name='user_list'),
    path('register', Cadastrar_View.as_view(), name='cadastrar'),
    #path('login/', LoginView.as_view(), name='login')
]
urlpatterns = format_suffix_patterns(urlpatterns)    
