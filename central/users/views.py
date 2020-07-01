from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from users.serializers import CadastroSerializer
#teste cadastrar
class HomePageView(TemplateView):
    template_name = 'home.html'

@api_view(['POST', ])
def cadastrar_view(request):
    
    if request.method == 'POST':
        serializer = CadastroSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário criado com sucesso"
            data['email'] = user.email

        else:
            data = serializer.errors
        return Response(data)
    

class Login(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login'