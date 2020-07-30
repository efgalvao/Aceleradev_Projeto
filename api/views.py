from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import generics, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from .models import Event
from .serializers import EventDetailSerializer, EventCreateSerializer
from .serializers import RegisterSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

def freq_update():
    erros = Event.objects.all()
    for erro in erros:
        frequencia = Event.objects.filter(description=erro.description).count()
        setattr(erro, 'frequency', frequencia)
        erro.save()


class EventViewSet(ModelViewSet):
    """
        Viewset for Events
    """    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('env',)
    search_fields = ['level', 'description', 'address']
    ordering_fields = ('frequency',)

         
    def create(self, request, *args, **kwargs):
        """
            Method for creation of events 
        """
        freq_update()
        serializer = EventCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            event = serializer.save()
            data['response'] = "Evento criado com sucesso"
        else:
            data = serializer.errors
        return Response(data)



class Register_View(CreateAPIView):
    """
        Class used to register user
    """
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário criado com sucesso"
        else:
            data = serializer.errors
        return Response(data)

