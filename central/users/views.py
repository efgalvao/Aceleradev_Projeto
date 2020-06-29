from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class Cadastrar(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Login(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'login.html'