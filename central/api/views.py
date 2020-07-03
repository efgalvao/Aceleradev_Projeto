from django.shortcuts import render
from rest_framework import generics
from django.views import View
from .models import Event, Agent
from .serializers import EventSerializer, EventViewSerializer, EventDetailSerializer, AgentSerializer
from .services import get_all_events
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#teste cadastrar
from rest_framework.views import APIView

# Create your views here.

class Event_list(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        events = get_all_events()
        serializer = EventViewSerializer(events, many=True)
        return Response(serializer.data)



class EventAPI_objects(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventViewSerializer
   #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    #def get(self, request, format=None):
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


class Event_details(generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class Agent_Create(generics.CreateAPIView):
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

class Agent_Details(generics.RetrieveAPIView):
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