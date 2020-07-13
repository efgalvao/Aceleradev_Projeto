from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import generics, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer, EventCreateSerializer
from .serializers import RegisterSerializer


class EventViewSet(ModelViewSet):
    """
        Viewset for Events
    """    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    
    def create(self, request, *args, **kwargs):
        """
            Method for creation of events 
        """
        serializer = EventCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            event = serializer.save()
        erros = Event.objects.all()
        for erro in erros:
            frequencia = Event.objects.filter(description=erro.description).count()
            setattr(erro, 'frequency', frequencia)
            erro.save()
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        """
        Method for listing events 
        """
        erros = Event.objects.all()
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False )
    def dev(self, request, pk=None):
        """
        Method used to filter events by the env "Dev"
        """
        erros = Event.objects.filter(env='Dev')
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def homo(self, request, pk=None):
        """
            Method used to filter events by the env "Homologação"
        """
        erros = Event.objects.filter(env='Homologação')
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def prod(self, request, pk=None):
        """
            Method used to filter events by the env "Produção"
        """
        erros = Event.objects.filter(env='Produção')
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_level(self, request, pk=None):
        """
            Method used to order the events by "level"
        """
        erros = Event.objects.order_by('level')
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def order_freq(self, request, pk=None):
        """
            Method used to order the events by "frequency"
        """
        erros = Event.objects.all()
        erros = Event.objects.order_by('-frequency')
        serializer = EventListSerializer(erros, many=True)
        return Response(serializer.data)


class Events_Search_level(generics.ListAPIView):
    """
        Class used to search events in the "level" attribute
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']


class Events_Search_description(generics.ListAPIView):
    """
        Class used to search events in the "description" attribute
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']


class Events_Search_address(generics.ListAPIView):
    """
        Class used to search events in the "address" attribute
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']


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
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
