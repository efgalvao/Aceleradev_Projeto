from rest_framework import serializers
from api.models import Livro, Autor, Genero


class LivroSerializer(serializers.ModelSerializer):
        class Meta:
            model = Livro
            fields = '__all__'
    
class AutorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Autor
            fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genero
            fields = '__all__'