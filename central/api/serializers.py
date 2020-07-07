from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import Agent, Event, CustomUser, Group


"""
class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_token')
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'token', )

    def get_token(self, user):
        token = token.key
        return token


class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'
"""

class AgentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Agent
            fields = '__all__'

class EventDetailSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')
    
    class Meta:
        model = Event
        fields = '__all__'

class EventListSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')

    class Meta:
        model = Event
        fields = ('level', 'description', 'address', 'date')

class CadastroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = CustomUser(
                email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
        