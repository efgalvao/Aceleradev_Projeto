from django.shortcuts import render
from rest_framework import generics
from api.models import Livro, Autor, Genero
from api.serializers import LivroSerializer, AutorSerializer, GeneroSerializer

# Create your views here.
   
class LivroAPI_objects(generics.ListCreateAPIView):
        queryset = Livro.objects.all()
        serializer_class = LivroSerializer

class AutorAPI_objects(generics.ListCreateAPIView):
        queryset = Autor.objects.all()
        serializer_class = AutorSerializer

class GeneroAPI_objects(generics.ListCreateAPIView):
        queryset = Genero.objects.all()
        serializer_class = GeneroSerializer
class LivroAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Livro.objects.all()
        serializer_class = LivroSerializer

class AutorAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Autor.objects.all()
        serializer_class = AutorSerializer

class GeneroAPI_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Genero.objects.all()
        serializer_class = GeneroSerializer
