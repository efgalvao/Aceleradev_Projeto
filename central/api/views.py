from django.shortcuts import render
from rest_framework import generics
from .models import User, Agent, Group, Event
from .serializers import UserSerializer, AgentSerializer, GroupSerializer, EventSerializer

# Create your views here.
   
class UserAPI_objects(generics.ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class UserAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class AgentAPI_objects(generics.ListCreateAPIView):
        queryset = Agent.objects.all()
        serializer_class = Agent

class AgentAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Agent.objects.all()
        serializer_class = AgentSerializer

class GroupAPI_objects(generics.ListCreateAPIView):
        queryset = Group.objects.all()
        serializer_class = GroupSerializer
        
class GroupAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Group.objects.all()
        serializer_class = GroupSerializer

class EventAPI_objects(generics.ListCreateAPIView):
        queryset = Event.objects.all()
        serializer_class = EventSerializer

class EventPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Event.objects.all()
        serializer_class = EventSerializer
