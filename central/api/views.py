from django.shortcuts import render
from rest_framework import generics
from api.models import Livro, Autor, Genero
from api.serializers import UserSerializer, AgentSerializer, GroupSerializer, EventSerializer, GroupuserSerializer

# Create your views here.
   
class UserAPI_objects(generics.ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class AgentPI_objects(generics.ListCreateAPIView):
        queryset = Agent.objects.all()
        serializer_class = AgentSerializer

class GroupAPI_objects(generics.ListCreateAPIView):
        queryset = Group.objects.all()
        serializer_class = GroupSerializer
        
class EventPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Event.objects.all()
        serializer_class = EventSerializer

class GroupuserAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Groupuser.objects.all()
        serializer_class = GroupuserSerializer
