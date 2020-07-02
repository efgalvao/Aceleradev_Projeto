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
from rest_framework.generics import CreateAPIView
from django.shortcuts import redirect
#teste cadastrar
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_user(request):
        user = request.user
        token = Token.objects.get(user=user).key
    

class Cadastrar_View(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    def get(self, request):
        serializer = CadastroSerializer
        return render(request, "cadastrar.html", {"serializer": serializer })

    def post(self, request):
        serializer = CadastroSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário criado com sucesso"
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return redirect('login/')

class Login_View(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        return redirect('users:login')

class User_list(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        events = CustomUser.objects.all()
        tokens= Token.objects.all()
        return render(request, 'user_list.html', {'tokens':tokens})

class Logout_View(APIView):
    def get(self, request):
        data = "Tchau"
        return Response(data)


