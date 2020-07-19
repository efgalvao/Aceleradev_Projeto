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
from .serializers import EventListSerializer, EventDetailSerializer, EventCreateSerializer
from .serializers import RegisterSerializer


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
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    
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
    
    def list(self, request, *args, **kwargs):
        """
        Method for listing events 
        """
        freq_update()
        paginacao = PageNumberPagination()
        erros = Event.objects.all()
        resultado = paginacao.paginate_queryset(erros, request)
        serializer = EventListSerializer(resultado, many=True)
        return paginacao.get_paginated_response(serializer.data)

    def destroy(self, request, pk=None):
        erro = Event.objects.get(id=pk)
        erro.delete()
        return Response("Evento removido")

    def update(self, request, pk=None):
        erro = Event.objects.get(id=pk)
        serializer = EventCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            event = serializer.save()
            data['response'] = "Evento alterado com sucesso"
        else:
            data = serializer.errors
        return Response(data)

    def partial_update(self, request, pk=None):
        event = Event.objects.get(id=pk)
        serializer = EventCreateSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Events_Search_level(generics.ListAPIView):
    """
        Class used to search events in the "level" attribute
    """
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    freq_update()
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']


class Events_Search_description(generics.ListAPIView):
    """
        Class used to search events in the "description" attribute
    """
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    freq_update()
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']


class Events_Search_address(generics.ListAPIView):
    """
        Class used to search events in the "address" attribute
    """
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    freq_update()
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
        else:
            data = serializer.errors
        return Response(data)

class Filter(generics.ListAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = EventListSerializer

    def get_queryset(self):
        """
        This view should return a list of events filtered by the environment 
        as determined by the env portion of the URL.
        """
        env = self.kwargs['env']
        return Event.objects.filter(env=env)

class Level(generics.ListAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = EventListSerializer
    queryset = ''

    def get(self, request):
        """
        This view should return a list of all events ordered by level.
        """
        freq_update()
        paginacao = PageNumberPagination()
        erros = Event.objects.order_by('level')
        resultado = paginacao.paginate_queryset(erros, request)
        serializer = EventListSerializer(resultado, many=True)
        return paginacao.get_paginated_response(serializer.data)


class Freq(generics.ListAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = EventListSerializer
    queryset = ''

    def get(self, request, format=None):
        """
        This view should return a list of all events ordered by frequency.
        """
        freq_update()
        paginacao = PageNumberPagination()
        erros = Event.objects.order_by('-frequency')
        resultado = paginacao.paginate_queryset(erros, request)
        serializer = EventListSerializer(resultado, many=True)
        return paginacao.get_paginated_response(serializer.data)