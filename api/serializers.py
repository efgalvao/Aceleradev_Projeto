from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Event, User


class RegisterSerializer(serializers.ModelSerializer):
    """
        Serializer for user register
    """
    email = serializers.EmailField(required=True,
            validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(email=self.validated_data['email'], )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class EventCreateSerializer(serializers.ModelSerializer):
    """
        Serializer for Event creation
    """
    frequency = serializers.IntegerField(read_only=True)
    address = serializers.CharField(max_length=100)

    class Meta:
        model = Event
        fields = '__all__'

    
class EventDetailSerializer(serializers.ModelSerializer):
    """
        Serializer for Event details
    """
    frequency = serializers.IntegerField(read_only=True)


    class Meta:
        model = Event
        fields = '__all__'

