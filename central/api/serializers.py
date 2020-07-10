from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Event, User

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

class EventDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'

class EventListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('level', 'description', 'address', 'date', 'frequency')
