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
from users.models import CustomUser
from rest_framework.renderers import TemplateHTMLRenderer
#teste cadastrar
class HomePageView(TemplateView):
    template_name = 'home.html'

class Cadastrar_View(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cadastrar.html'

    def get(self, request):
        serializer = CadastroSerializer
        return render(request, "cadastrar.html", {"serializer": serializer })

    def post(self, request):
        serializer = CadastroSerializer(data=request.data)
        data = {}
        if serializer.is_valid():            
            user = serializer.save()
            print(data)
            data['response'] = "Usuário criado com sucesso"
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    

class Login(TemplateView):
    form_class = CadastroSerializer
    success_url = reverse_lazy('home')
    template_name = 'login.html'

class User_list(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        events = CustomUser.objects.all()
        tokens= Token.objects.all()
        return render(request, 'user_list.html', {'tokens':tokens})

