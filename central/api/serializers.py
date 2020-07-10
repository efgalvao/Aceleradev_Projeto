from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import Erro, User

class CadastroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
                email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

class ErroDetailSerializer(serializers.ModelSerializer):
    #freq = serializers.IntegerField(source='frequency')     
    #frequency = serializers.IntegerField(read_only=True)

    class Meta:
        model = Erro
        #fields = ('id', 'level', 'description', 'details', 'address', 'archived', 'date', 'env', 'frequency')
        fields = '__all__'

class ErroListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Erro
        fields = ('level', 'description', 'address', 'date', 'freq')


        