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
from .models import Event, User
from .serializers import EventListSerializer, EventDetailSerializer
from .serializers import CadastroSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.db.models import Count
from rest_framework import filters



class EventViewSet(ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    def list(self, request, *args, **kwargs):
        erros = Event.objects.all()
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def dev(self, request, pk=None):        
        erros = Event.objects.filter(env='Dev')
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def homo(self, request, pk=None):        
        erros = Event.objects.filter(env='Homologação')
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def prod(self, request, pk=None):        
        erros = Event.objects.filter(env='Produção')
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_level(self, request, pk=None):        
        erros = Event.objects.order_by('level')
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_freq(self, request, pk=None):   
        erros = Event.objects.all()
        for erro in erros:
            frequencia = Event.objects.filter(description=erro.description).count()
            setattr(erro, 'frequency', frequencia)
            erro.save()
        erros = Event.objects.order_by('-frequency')
        serializer = EventDetailSerializer(erros, many=True)
        return Response(serializer.data)
class Event_Details(RetrieveAPIView):
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class Events_Agentsid(ListCreateAPIView):
    serializer_class = EventListSerializer
        
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('agent_id')
        return Event.objects.filter(agent_id=id)

class Events_By_Groupid(ListCreateAPIView):
    serializer_class = EventListSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('id')
        return Event.objects.filter(env=id)

from rest_framework import filters

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
        
class Events_Search_level(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']


class Events_Search_description(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

class Events_Search_address(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
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

class User_list(APIView):
    def get(self, request, format=None):
        # events = User.objects.all()
        tokens= Token.objects.all()
        return render(request, 'user_list.html', {'tokens':tokens})
