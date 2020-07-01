from django.shortcuts import render
from rest_framework import generics
from django.views import View
from .models import Event
from .serializers import EventSerializer
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
    """
    def get(self, request, format=None):
        events = get_all_events()
        return render(request, 'api/event_list.html', {'events':events})
    """
    def get(self, request):
        events = get_all_events()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, 'api/event_list.html')



class EventAPI_objects(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
   #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    #def get(self, request, format=None):
    """
    Return a list of all users.
    """
        #events = [Event.data for Event in Event.objects.all()]
        #return Response(events)

class EventAPI_objects_details(generics.RetrieveAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

