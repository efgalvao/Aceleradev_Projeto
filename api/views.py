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
from drf_yasg.utils import swagger_auto_schema


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

         
    @swagger_auto_schema(
        request_body=EventDetailSerializer,
        query_serializer=EventDetailSerializer,
        responses={
            '200': 'Ok Request',
            '400': "Bad Request"
        },
        security=[],
        operation_id='Create Event',
        operation_description='Creation of events',
    )
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
    
    @swagger_auto_schema(
        security=['token'],
        operation_id='List of events',
        operation_description='This endpoint list all events',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='Deletion of events',
        operation_description='This endpoint delete an event'
    )
    def destroy(self, request, pk=None):
        erro = Event.objects.get(id=pk)
        erro.delete()
        return Response("Evento removido")
     
    @swagger_auto_schema(
        security=['token'],
        operation_id='Update of events',
        operation_description='Update event',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='Partial update of events',
        operation_description='Partial update of events',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='User creation',
        operation_description='Register an user',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='List of events filtered by environment',
        operation_description='This endpoint list all events filtered by environment',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='List of events ordered by level',
        operation_description='This endpoint list all events ordered by level',
    )
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

    @swagger_auto_schema(
        security=['token'],
        operation_id='List of events ordered by frequency',
        operation_description='This endpoint list all events ordered by frequency',
    )
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
