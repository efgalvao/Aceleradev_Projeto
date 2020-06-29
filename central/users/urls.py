from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.Cadastrar.as_view(template_name='signup.html'), name='cadastrar'),
    path('', include('django.contrib.auth.urls')),
    
]