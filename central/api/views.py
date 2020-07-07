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

from .forms import CustomUserCreationForm
from .models import Event, Agent, CustomUser, Group
from .serializers import EventListSerializer, EventDetailSerializer, AgentSerializer
from .serializers import CadastroSerializer
from .services import get_all_events

# Create your views here.

class Event_list(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

    
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    

class Event_List(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
   #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    #def get(self, request, format=None):

    def get_queryset(self, *args, **kwargs):
        return Event.objects.all()

    """
    Return a list of all users.
    """
        #events = [Event.data for Event in Event.objects.all()]
        #return Response(events)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            event = serializer.save()
            data['response'] = "Evento criado com sucesso"
            data['id'] = event.id
            data['level'] = event.level
            data['data'] = event.data
            data['arquivado'] = event.arquivado
            data['date'] = event.date
            data['agent'] = event.agent.id
        else:
            data = serializer.errors
        return Response(data)


class Event_details(RetrieveAPIView):
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class Agent_Create(ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
   #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    #def get(self, request, format=None):
    """
    Create an Agent instance.
    """
        #events = [Event.data for Event in Event.objects.all()]
        #return Response(events)
    def post(self, request):
        serializer = AgentSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            agent = serializer.save()
            data['response'] = "Agente criado com sucesso"
            data['id'] = agent.id
            data['name'] = agent.name
            data['user'] = agent.user.id
            data['address'] = agent.address
            data['status'] = agent.status
            data['env'] = agent.env
            data['version'] = agent.version
        else:
            data = serializer.errors
        return Response(data)

class Agent_Details(RetrieveAPIView):
    lookup_field = "pk"
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class Agent_List(generics.ListAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    
    """
    def get(self, request):
        queryset = Agent.objects.all()
        serializer = AgentSerializer(queryset, many=True)
        return Response(serializer.data)
"""

class Events_Agentsid(ListCreateAPIView):
    serializer_class = EventListSerializer
        
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('agent_id')
        return Event.objects.filter(agent_id=id)

class Events_By_Groupid(ListCreateAPIView):
    serializer_class = EventListSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('id')
        return Event.objects.filter(agent__user__group__id=id)

from rest_framework import filters

class Events_Ordered_by_Level(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['level']
    ordering = ['level']

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
        
class Events_Search_level(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = (DynamicSearchFilter,)

class Events_Search_description(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

class Events_Search_address(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['agent__address']

class HomePageView(TemplateView):
    template_name = 'home.html'

class Cadastrar_View(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    def get(self, request):
        serializer = CadastroSerializer
        return render(request, "cadastrar.html", {"serializer": serializer })
        
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
    queryset = CustomUser.objects.all()
    serializer_class = CadastroSerializer
    permission_classes = (AllowAny, )
    
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        return redirect('users:login')
"""
class User_list(APIView):
    def get(self, request, format=None):
        # events = CustomUser.objects.all()
        tokens= Token.objects.all()
        return render(request, 'user_list.html', {'tokens':tokens})

