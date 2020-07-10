from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import CreateView, TemplateView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework import generics

from .forms import UserCreationForm
from .models import Erro, User
from .serializers import ErroListSerializer, ErroDetailSerializer
from .serializers import CadastroSerializer
#teste viewset
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db.models import Count

# Create your views here.

class ErroViewSet(ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Erro.objects.all()
    serializer_class = ErroDetailSerializer


    def list(self, request, *args, **kwargs):
        erros = Erro.objects.all()
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def dev(self, request, pk=None):        
        erros = Erro.objects.filter(env='Dev')
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def homo(self, request, pk=None):        
        erros = Erro.objects.filter(env='homologação')
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def prod(self, request, pk=None):        
        erros = Erro.objects.filter(env='Produção')
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_level(self, request, pk=None):        
        erros = Erro.objects.order_by('level')
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_freq(self, request, pk=None):   
        #filter_backends = (filters.OrderingFilter,)
        #qtd = Erro.objects.filter(description=self.description).count()
        #erros = Erro.objects.values('description').annotate(c=Count('description')).order_by('-c')        #ordering = ['frequency']
        erros = Erro.objects.all()
        for erro in erros:
            frequencia = Erro.objects.filter(description=erro.description).count()
            setattr(erro, 'freq', frequencia)
            erro.save()
        erros = Erro.objects.order_by('-freq')
        #freq = Erro.objects.filter(description=self.description).count()
        #erros = Erro.objects.annotate(freq= req).order_by('frequency')
        #erros = Erro.objects.annotate(count=Count('description'))
        serializer = ErroDetailSerializer(erros, many=True)
        return Response(serializer.data)


class TesteViewSet(ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Erro.objects.all()
    serializer_class = ErroDetailSerializer
    serializer_action_classes = {
        'list': ErroDetailSerializer,
    }
    filterset_fields = ("level", "address", "description", )
    search_fields = ("level", "description", "address" )
    ordering_fields = ("level", "frequency", )
    ordering = ("-level", )



"""
    def create(self, request, *args, **kwargs):
        serializer = ErroDetailSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            erro = serializer.save()
            data['response'] = "Erro criado com sucesso"
            data['id'] = erro.id
            data['level'] = erro.level
            #data['user'] = erro.user
            data['description'] = erro.description
            data['details'] = erro.details
            data['address'] = erro.address
            data['archived'] = erro.archived
            data['date'] = erro.date
            data['env'] = erro.env

        else:
            data = serializer.errors
        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = Erro.objects.get(pk=pk)
        return redirect('/')

    def destroy(self, request, pk=None):
        erro = Erro.objects.get(pk=pk)
        erro.delete()
        return redirect('/')
"""


class Erro_Details(RetrieveAPIView):
    lookup_field = "id"
    queryset = Erro.objects.all()
    serializer_class = ErroDetailSerializer



class Events_Agentsid(ListCreateAPIView):
    serializer_class = ErroListSerializer
        
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('agent_id')
        return Erro.objects.filter(agent_id=id)

class Events_By_Groupid(ListCreateAPIView):
    serializer_class = ErroListSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('id')
        return Erro.objects.filter(env=id)

from rest_framework import filters

class Events_Ordered_by_Level(ListCreateAPIView):
    queryset = Erro.objects.all()
    serializer_class = ErroListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['level']
    ordering = ['level']

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
        
class Events_Search_level(generics.ListAPIView):
    queryset = Erro.objects.all()
    serializer_class = ErroListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']


class Events_Search_description(generics.ListAPIView):
    queryset = Erro.objects.all()
    serializer_class = ErroListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

class Events_Search_address(generics.ListAPIView):
    queryset = Erro.objects.all()
    serializer_class = ErroListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']

class HomePageView(TemplateView):
    template_name = 'home.html'

class Cadastrar_View(CreateAPIView):
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    @csrf_exempt
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
        return Response(data)

"""
class Login_View(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        return redirect('users:login')
"""
class User_list(APIView):
    def get(self, request, format=None):
        # events = User.objects.all()
        tokens= Token.objects.all()
        return render(request, 'user_list.html', {'tokens':tokens})

