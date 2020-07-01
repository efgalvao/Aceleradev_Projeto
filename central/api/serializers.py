from rest_framework import serializers
from .models import Agent, Event
from users.models import CustomUser, Group


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_token')
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'token', )

    def get_token(self, user):
        token = token.key
        return token

class AgentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Agent
            fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')
    
    class Meta:
        model = Event
        fields = ('level', 'data', 'arquivado', 'date', 'address', 'agent')
